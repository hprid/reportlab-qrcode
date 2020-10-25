import qrcode
from reportlab.lib.units import mm
from reportlab.platypus import Flowable


class QRCodeImage(Flowable):
    def __init__(self, data=None, size=25 * mm, fill_color='blue',
                 back_color='yellow', border=4, **kwargs):
        Flowable.__init__(self)
        self.x = 0
        self.y = 0
        self.width = size
        self.height = size
        self.size = size
        self.border = 4
        self.fill_color = fill_color
        self.back_color = back_color
        kwargs['box_size'] = 1
        kwargs['border'] = 0
        self._qr = qrcode.QRCode(**kwargs)
        if data is not None:
            self._qr.add_data(data)

    def add_data(self, data, optimize=20):
        self._qr.add_data(data, optimize)

    def clear(self):
        self._qr.clear()

    def draw(self):
        matrix = self._qr.get_matrix()
        active_positions = []
        for y, row in enumerate(matrix):
            for x, is_active in enumerate(row):
                if is_active:
                    active_positions.append((y, x))
        box_size = self.size / (len(matrix) + 2 * self.border)
        self.canv.saveState()
        if self.back_color is not None:
            self.canv.setFillColor(self.back_color)
            self.canv.rect(self.x, self.y, self.size, self.size, stroke=0, fill=1)
        self.canv.setFillColor(self.fill_color)
        for row, col in active_positions:
            xr = (col + self.border) * box_size
            yr = (row + self.border) * box_size
            xr, yr = yr, -xr
            yr += self.size - box_size
            self.canv.rect(xr + self.x, yr + self.y, box_size, box_size, stroke=0, fill=1)
        self.canv.restoreState()

