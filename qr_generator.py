from PIL import Image
import qrcode as qr
user = input("Enter the link to create Qr")
img = qr.make(user)
img.save("qr.png")