import os
import qrcode

path = os.path.join("../..", "files", "qr_kaizen.png")

# pngファイルの生成
img = qrcode.make('https://github.com/makinokoudai/python_teamB_2023518/blob/main/koshiba/pricedown_kaizen.py')
img.save(path)
