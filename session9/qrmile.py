import qrcode
import os
qr=qrcode.QRCode(version=1,
                 box_size=20,
                 border=2)
qr.add_data('silver18mp@gmail.com')
qr.make(fit=True)
img = qr.make_image(fill_color="red",back_color="white")
img.save('namepo')
