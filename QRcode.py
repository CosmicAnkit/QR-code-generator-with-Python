import pyqrcode
import png
from pyqrcode import QRCode
x = "This is ankit maurya"
qr = pyqrcode.create(x)
qr.svg("qr1.svg",scale = 8)
qr.png("qr.png",scale = 6)
qr.show()
