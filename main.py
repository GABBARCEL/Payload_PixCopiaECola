import qrcode
from pathlib import Path
import Link

url = Link.genLink()
file_path = Path.home() / "Downloads" / "QRCode.png"

def genQrCode(url):
    qr = qrcode.QRCode()
    qr.add_data(url)
    img = qr.make_image()
    img.save(file_path)
    return f"The QRcode was saved along the path:{file_path}"

genQrCode(url)