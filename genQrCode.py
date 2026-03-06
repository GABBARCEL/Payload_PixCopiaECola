import qrcode
from PIL import Image

def genQrCode(url):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    pil_img = img.get_image().convert("RGB")
    return pil_img
