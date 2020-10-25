import os
import subprocess
import tempfile

from PIL import Image
from pyzbar import pyzbar
from pytest import approx


def test_simple():
    run_example('simple')


def test_advanced():
    # page size is A4 (297x210 mm) and QR code at (30, 50) mm
    # The QR code has 21x21 boxes and is 2.5 cm large (including
    # 4 boxes border)
    total_size = 25
    border = 4
    box_size = total_size / (21 + 2 * border)
    border_size = border * box_size
    size = box_size * 21
    orig_pos_x = 30
    orig_pos_y = 50

    # reportlabs coordinate system starts from bottom left
    top = (297 - orig_pos_y - border_size - size)
    left = (orig_pos_x + border_size)
    left_end = left + size

    top_rel = top / 297
    left_rel = left / 210
    left_end_rel = left_end / 210

    run_example('advanced', (top_rel, left_rel, left_end_rel))


def test_flow():
    run_example('flow')


def run_example(example_name, position=None):
    pdf_file = example_name + '.pdf'
    source_code = _get_example_code(example_name + '.py')
    with tempfile.TemporaryDirectory() as d, WithCwd(d):
        exec(source_code)
        assert pdf_file in os.listdir()
        image_file = pdf_file + '.jpg'
        args = ['convert', '-density', '300', pdf_file + '[0]', image_file]
        subprocess.run(args, check=True)
        assert image_file in os.listdir()
        with Image.open(image_file) as img:
            img_width, img_height = img.size
            result = pyzbar.decode(img)
        assert len(result) == 1
        assert result[0].data == 'Some data here'.encode('ascii')
        if position:
            rect = result[0].rect
            img_top = rect.top / img_height
            img_left = rect.left / img_width
            img_left_end = (rect.left + rect.width) / img_width
            top, left, left_end = position
            assert rect.width == approx(rect.height, abs=2)
            assert left == approx(img_left, rel=0.02)
            assert top == approx(img_top, rel=0.02)
            assert left_end == approx(img_left_end, rel=0.02)


def _get_example_code(name):
    filename = os.path.join(os.path.dirname(__file__), '../examples', name)
    with open(filename) as f:
        return f.read()


class WithCwd:
    def __init__(self, new_dir):
        self._new_dir = new_dir
        self._old_dir = None

    def __enter__(self):
        self._old_dir = os.getcwd()
        os.chdir(self._new_dir)

    def __exit__(self, exc_type, exc_value, exc_tb):
        os.chdir(self._old_dir)

