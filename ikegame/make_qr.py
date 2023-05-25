import qrcode
import os

path = os.path.join("../..","files","qrcode.png")
qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=2,
    border=8
)
qr.add_data("https://www.amazon.co.jp/meet-alexa/b?ie=UTF8&node=5485773051")
img = qr.make_image(fill_color="black",back_color="white")
img.save(path)
img.show()