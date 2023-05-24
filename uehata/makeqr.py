import os 
import qrcode

dir_path = os.path.join("..","..","files","mynavi.png")
img = qrcode.make("https://www.mynavi.jp/")

img.save(dir_path)
