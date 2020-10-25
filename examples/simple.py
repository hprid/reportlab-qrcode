from reportlab.pdfgen.canvas import Canvas
from reportlab_qrcode import QRCodeImage

doc = Canvas('simple.pdf')
qr = QRCodeImage('Some data here')
qr.drawOn(doc, 0, 0)
doc.showPage()
doc.save()
