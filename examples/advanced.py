from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas
from reportlab_qrcode import QRCodeImage
import qrcode

doc = Canvas('advanced.pdf')
qr = QRCodeImage(
    size=25 * mm,
    fill_color='blue',
    back_color='yellow',
    border=4,
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
)
qr.add_data('Some data here')
qr.drawOn(doc, 30 * mm, 50 * mm)
doc.showPage()
doc.save()
