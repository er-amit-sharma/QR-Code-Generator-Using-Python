import pyqrcode
import png

link = "https://www.linkedin.com/in/eramitsharma"
qr_code = pyqrcode.create(link)
qr_code.png("qrcode.png", scale=5)