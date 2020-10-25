reportlab-qrcode
================

reportlab-qrcode implements a QR code flowable for the ReportLab PDF library
using the [qrcode package](https://pypi.org/project/qrcode/).


Installation
------------

reportlab-qrcode can be installed via pip:

    pip install reportlab-qrcode


Usage
-----

Simply use the *QRCodeImage* class with your data. All non-recognized keyword
arguments will be passed to the *qrcode.QRCode* class from the qrcode package.

    from reportlab.lib.units import mm
    from reportlab.pdfgen.canvas import Canvas
    from reportlab_qrcode import QRCodeImage

    doc = Canvas('simple.pdf')
    qr = QRCodeImage('Some data here', size=30 * mm)
    qr.drawOn(doc, 0, 0)
    doc.showPage()
    doc.save()

For further examples, including setting fill and back colors, QR code size,
error correction level, as well as using the QR code as ReportLab Flowable
object, see the [examples directory](https://github.com/hprid/reportlab-qrcode/tree/master/examples).


Maintenance note
----------------

This package is considered completed. So please do not wonder if you see no
further commits. Despite the lack of new commits, this package is still
maintained, i. e., I plan to keep this package compatible with the newest
Python, qrcode and ReportLab version. If you find a bug, please open an issue
in the issue tracker.


License
-------

reportlab-qrcode is licensed under the MIT license. See LICENSE file for
details.

