import qrcode
from PIL import  Image
#to take data and make changes like borders,functionalities
qr=qrcode.QRCode(version=1, 
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=12,border=5,)
qr.add_data("https://github.com/HarshitaNahata")
qr.make(fit=True)
img=qr.make_image(fill_color="yellow",back_color="blue")
img.save("github.png")