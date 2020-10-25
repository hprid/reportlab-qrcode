from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab_qrcode import QRCodeImage

doc = SimpleDocTemplate('flow.pdf')
style = getSampleStyleSheet()
qr_flowable = QRCodeImage('Some data here')
flowables = [
    Paragraph('Lorem ipsum', style['BodyText']),
    qr_flowable,
    Paragraph('dolor sit amet', style['BodyText'])
]
doc.build(flowables)
