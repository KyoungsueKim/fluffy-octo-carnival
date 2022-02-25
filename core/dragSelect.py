from PySide6 import QtWidgets
from PySide6 import QtGui, QtCore
from core.common import pil2pixmap
import pyautogui as gui
import pygetwindow as gw

class DragSelect(QtWidgets.QWidget):
    def __init__(self, type, parent_view):
        super(DragSelect, self).__init__()
        self.parent_view = parent_view
        self.type = type

        self.items = []
        self.start = QtCore.QPointF()
        self.end = QtCore.QPointF()

        self.setupUi()

    def setupUi(self):
        # 1. qGraphicsView 화면 구성
        self.qView = QtWidgets.QGraphicsView(self)
        # self.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.qView.mouseMoveEvent = lambda event: self.mouseMoveEvent(event)

        # 2. 프로세스의 스크린샷 촬영 후 위젯 사이즈 조정
        windows = gw.getWindowsWithTitle('Z9★ 온라인')[0]
        self.image = gui.screenshot(region=(*windows.topleft, *windows.bottomright))
        self.resize(*windows.size)

        # 3. qGraphicsView에 스크린샷 이미지 집어넣기
        self.qScene = QtWidgets.QGraphicsScene()
        self.qScene.addPixmap(pil2pixmap(self.image))
        self.qView.setScene(self.qScene)
        self.qView.resize(*self.image.size)


    def mousePressEvent(self, event:QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.LeftButton:
            # 시작 / 끝 좌표 초기화
            self.start = event.pos()
            self.end = event.pos()


    def mouseMoveEvent(self, event:QtGui.QMouseEvent) -> None:
        if event.buttons() & QtCore.Qt.LeftButton:
            self.end = event.pos()
            pen = QtGui.QPen(QtGui.Qt.red, 1, QtGui.Qt.SolidLine)
            rect = QtCore.QRectF(self.start, self.end)
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))

            if len(self.items) > 0:
                self.qScene.removeItem(self.items[-1])
                del(self.items[-1])

            self.items.append(self.qScene.addRect(rect, pen, brush))

    def keyPressEvent(self, event:QtGui.QKeyEvent) -> None:
        if event.key() == 16777220: # 엔터키를 눌렀다면
            # 그냥 실수로 클릭만 해서 시작과 끝의 좌표가 같다면
            if self.start.__pos__() == self.end.__pos__():
                return

            # 선택 영역대로 이미지 크롭
            self.image = self.image.crop((self.start.x(), self.start.y(), self.end.x(), self.end.y()))

            # qScene에 pixmap을 넣고 view에 걸어둠.
            self.qScene = QtWidgets.QGraphicsScene()
            self.qScene.addPixmap(pil2pixmap(self.image))
            self.parent_view.setScene(self.qScene)

            # 이미지 저장
            self.image.save(f'core/templates/{self.type}.png')

            # 위젯 종료
            self.close()




