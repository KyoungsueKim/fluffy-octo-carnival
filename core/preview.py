import threading
import cv2
import numpy as np
import pyautogui as gui
import pygetwindow as gw
from core.templateMatch import get_farmpos, get_playerPos, get_seedPos, get_fertPos, get_waterPos

def preview():
    thread = Preview()
    thread.daemon = True
    thread.start()

class Preview(threading.Thread):
    def __init__(self):
        super(Preview, self).__init__()

    def run(self) -> None:
        windows = gw.getWindowsWithTitle('Z9★ 온라인')[0]
        while True:
            image = gui.screenshot(region=(0, 0, *windows.bottomright))
            norm_points, gold_points = get_farmpos(image)
            player_points = get_playerPos(image)
            water_points = get_waterPos(image)
            fert_points = get_fertPos(image)
            seed_points = get_seedPos(image)

            # pil img -> cv2.img
            image = np.array(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # 농지 영역 표시
            for point in norm_points:
                cv2.circle(image, point, radius=1, color=(255, 0, 0), thickness=2)

            for point in gold_points:
                cv2.circle(image, point, radius=1, color=(0, 0, 255), thickness=2)

            # 플레이어 영역 표시
            cv2.circle(image, player_points, radius=1, color=(255, 0, 0), thickness=2)

            # 물뿌리게 영역 표시
            for point in water_points:
                cv2.circle(image, point, radius=1, color=(0, 255, 0), thickness=2)

            # 비료 영역 표시
            for point in fert_points:
                cv2.circle(image, point, radius=1, color=(255, 0, 0), thickness=2)

            # 비료 영역 표시
            for point in seed_points:
                cv2.circle(image, point, radius=1, color=(0, 0, 255), thickness=2)

            cv2.imshow('result', image)
            if cv2.waitKey(1) == ord('q'):
                break

        cv2.destroyAllWindows()