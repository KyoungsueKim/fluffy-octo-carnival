from PIL import Image
from PySide6 import QtWidgets
from PySide6.QtWidgets import QGraphicsScene
from core.form import Ui_Widget
from core.dragSelect import DragSelect
from core.common import pil2pixmap
from core.preview import preview
import pyautogui as gui


class MainWindow(Ui_Widget):

    def setupUi(self, parent):
        super(MainWindow, self).setupUi(parent)

        self.setupViews()

        self.pushButton_3.clicked.connect(lambda: preview())

        # 더블 클릭 이벤트 연결
        self.graphicsView_seedItem.mouseDoubleClickEvent = lambda event: self.dragSelect('seed', self.graphicsView_seedItem)
        self.graphicsView_waterItem.mouseDoubleClickEvent = lambda event: self.dragSelect('water', self.graphicsView_waterItem)
        self.graphicsView_fertItem.mouseDoubleClickEvent = lambda event: self.dragSelect('fertil', self.graphicsView_fertItem)
        self.graphicsView_player.mouseDoubleClickEvent = lambda event: self.dragSelect('player', self.graphicsView_player)
        self.graphicsView_goldland.mouseDoubleClickEvent = lambda event: self.dragSelect('gold_land', self.graphicsView_goldland)
        self.graphicsView_normalland.mouseDoubleClickEvent = lambda event: self.dragSelect('normal_land', self.graphicsView_normalland)

    def setupViews(self):
        # tmeplates 미리 설정
        qScene = QGraphicsScene()
        qScene.addPixmap(pil2pixmap(Image.open('core/templates/water.png')))
        self.graphicsView_waterItem.setScene(qScene)

        qScene = QGraphicsScene()
        qScene.addPixmap(pil2pixmap(Image.open('core/templates/fertilizer.png')))
        self.graphicsView_fertItem.setScene(qScene)

        qScene = QGraphicsScene()
        qScene.addPixmap(pil2pixmap(Image.open('core/templates/player.png')))
        self.graphicsView_player.setScene(qScene)

        qScene = QGraphicsScene()
        qScene.addPixmap(pil2pixmap(Image.open('core/templates/gold_land.png')))
        self.graphicsView_goldland.setScene(qScene)

        qScene = QGraphicsScene()
        qScene.addPixmap(pil2pixmap(Image.open('core/templates/normal_land.png')))
        self.graphicsView_normalland.setScene(qScene)

        qScene = QGraphicsScene()
        qScene.addPixmap(pil2pixmap(Image.open('core/templates/seed.png')))
        self.graphicsView_seedItem.setScene(qScene)


    def dragSelect(self, type, view: QtWidgets.QGraphicsView):
        if type == 'seed':
            self.graphicsView_seedItem.dragWidget = DragSelect(type, view)
            self.graphicsView_seedItem.dragWidget.show()
        elif type == 'water':
            self.graphicsView_waterItem.dragWidget = DragSelect(type, view)
            self.graphicsView_waterItem.dragWidget.show()
        elif type == 'fertil':
            self.graphicsView_fertItem.dragWidget = DragSelect(type, view)
            self.graphicsView_fertItem.dragWidget.show()
        elif type == 'player':
            self.graphicsView_player.dragWidget = DragSelect(type, view)
            self.graphicsView_player.dragWidget.show()
        elif type == 'gold_land':
            self.graphicsView_goldland.dragWidget = DragSelect(type, view)
            self.graphicsView_goldland.dragWidget.show()
        elif type == 'normal_land':
            self.graphicsView_normalland.dragWidget = DragSelect(type, view)
            self.graphicsView_normalland.dragWidget.show()
        else:
            return



if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    # 메인 다이얼로그 셋팅
    main_dialog = QtWidgets.QMainWindow()
    ui = MainWindow().setupUi(main_dialog)
    main_dialog.show()

    # # 오버레이 화면 셋팅
    # overlay = Overlay()

    sys.exit(app.exec())
