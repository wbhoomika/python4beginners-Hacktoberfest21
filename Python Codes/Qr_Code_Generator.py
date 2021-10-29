#pip install qrcode
import qrcode

link = input("Enter txt to encode in QR")
img = qrcode.make("link)
img.save("QR.jpg")
