import os
import qrcode

path = os.path.join("../..", "files", "qr_first.png")

# pngファイルの生成
img = qrcode.make('QRコードです!')
img.save(path)
