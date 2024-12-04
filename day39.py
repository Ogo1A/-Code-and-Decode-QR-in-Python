#QR CODE
import pyqrcode
import png
link= "https://www.youtube.com/"
qr_code=pyqrcode.create(link)
qr_code.png("youtube1,png",scale=5)

#DECODE A QRCODE
from pyzbar.pyzbar import decode
from PIL import Image
decocdeQR=decode(image.open(youtube1.png))
print(decocdeQR[0].data.decoder('ascii'))
