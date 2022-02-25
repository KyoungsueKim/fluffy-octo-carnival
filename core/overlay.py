"""
Deprecated: 한동안 쓸 일 없을 듯 ..
"""
import io
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QImage, QPixmap
from core.common import pil2pixmap


class Overlay(QtWidgets.QWidget):
    def __init__(self):
        super(Overlay, self).__init__()
        self.setupUi()
        self.show()

    def setupUi(self):
        # 오버레이 윈도우 옵션 설정
        self.resize(300, 300)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)

        # 이미지 집어넣을 라벨 생성
        label = QtWidgets.QLabel(self)
        image = Image.new(mode='RGBA', size=(300, 300), color=(0, 0, 0, 1))

        # 이미지에 사각형 그리기
        drawObject = ImageDraw.Draw(image)
        drawObject.rectangle(xy = ((100, 100), (200, 200)), outline=(255, 0, 0), width=3)

        # 이미지 셋팅
        qtImage = pil2pixmap(image)
        label.setPixmap(qtImage)


if __name__ == '__main__':
    pass
