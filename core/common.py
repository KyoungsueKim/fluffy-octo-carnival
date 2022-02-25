import io
from PySide6.QtGui import QImage, QPixmap

def pil2pixmap(image):
    bytes_img = io.BytesIO()
    image.save(bytes_img, format='PNG')

    qimg = QImage()
    qimg.loadFromData(bytes_img.getvalue())

    return QPixmap.fromImage(qimg)