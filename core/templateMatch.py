import cv2
import numpy as np
from PIL import Image
import pyautogui as gui
import pygetwindow as gw

def get_farmpos(screenImage: Image):
    # 1. 이미지 로드
    screen = np.array(screenImage)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    gold_path = 'core/templates/gold_land.png' if __name__ != '__main__' else 'templates/gold_land.png'
    norm_path = 'core/templates/normal_land.png' if __name__ != '__main__' else 'templates/normal_land.png'
    gold_templ: np.ndarray = cv2.imread(gold_path)
    norm_templ: np.ndarray = cv2.imread(norm_path)
    gold_templ = cv2.cvtColor(gold_templ, cv2.COLOR_BGR2GRAY)
    norm_templ = cv2.cvtColor(norm_templ, cv2.COLOR_BGR2GRAY)

    # 2. 템플릿매칭
    gold_result: np.ndarray = cv2.matchTemplate(screen, gold_templ, cv2.TM_CCOEFF_NORMED)
    norm_result: np.ndarray = cv2.matchTemplate(screen, norm_templ, cv2.TM_CCOEFF_NORMED)

    # 3. threshold 적용
    threshold = 0.995
    gold_location = set(zip(*np.where(gold_result >= threshold)[::-1]))
    norm_location = set(zip(*np.where(norm_result >= threshold)[::-1]))

    # 4. 농지 위치 계산 (숫자는 오프셋)
    norm_farm = [[((x - 56) + (32 * index) + 16, y - 90) for index in range(5)] for x, y in norm_location]
    gold_farm = [[((x - 56) + (32 * index) + 16, y - 90) for index in range(5)] for x, y in gold_location]

    # 5. unpacking
    norm_farm = sum(norm_farm, [])
    gold_farm = sum(gold_farm, [])
    return norm_farm, gold_farm


def get_playerPos(screenImage: Image):
    # 1. 이미지 로드
    screen = np.array(screenImage)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    path = 'core/templates/player.png' if __name__ != '__main__' else 'templates/player.png'
    player_templ: np.ndarray = cv2.imread(path)
    player_templ = cv2.cvtColor(player_templ, cv2.COLOR_BGR2GRAY)

    # 2. 템플릿메칭
    player_result: np.ndarray = cv2.matchTemplate(screen, player_templ, cv2.TM_CCOEFF_NORMED)

    # 3. threshold 적용
    _, _, _, player_location = cv2.minMaxLoc(player_result)

    # 4. 좌표를 중심으로 변경
    player_location = (
    int(player_location[0] + (player_templ.shape[1] / 2)), int(player_location[1] + (player_templ.shape[0] / 2)))
    return player_location


def get_waterPos(screenImage: Image):
    # 1. 이미지 로드
    screen = np.array(screenImage)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    water_path = 'core/templates/water.png' if __name__ != '__main__' else 'templates/water.png'
    water_templ: np.ndarray = cv2.imread(water_path)
    water_templ = cv2.cvtColor(water_templ, cv2.COLOR_BGR2GRAY)

    # 2. 템플릿매칭
    water_result: np.ndarray = cv2.matchTemplate(screen, water_templ, cv2.TM_CCOEFF_NORMED)

    # 3. threshold 적용
    threshold = 0.98
    water_location = set(zip(*np.where(water_result >= threshold)[::-1]))

    # 4. 좌표를 중심으로 변경
    water_location = [(int(x + (water_templ.shape[1] / 2)), int(y + (water_templ.shape[0] / 2))) for x, y in water_location]

    return water_location


def get_fertPos(screenImage: Image):
    # 1. 이미지 로드
    screen = np.array(screenImage)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    fert_path = 'core/templates/fertilizer.png' if __name__ != '__main__' else 'templates/fertilizer.png'
    fert_templ: np.ndarray = cv2.imread(fert_path)
    fert_templ = cv2.cvtColor(fert_templ, cv2.COLOR_BGR2GRAY)

    # 2. 템플릿매칭
    fert_result: np.ndarray = cv2.matchTemplate(screen, fert_templ, cv2.TM_CCOEFF_NORMED)

    # 3. threshold 적용
    threshold = 0.98
    fert_location = set(zip(*np.where(fert_result >= threshold)[::-1]))

    # 4. 좌표를 중심으로 변경
    fert_location = [(int(x + (fert_templ.shape[1] / 2)), int(y + (fert_templ.shape[0] / 2))) for x, y in fert_location]

    return fert_location


def get_seedPos(screenImage: Image):
    # 1. 이미지 로드
    screen = np.array(screenImage)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    seed_path = 'core/templates/seed.png' if __name__ != '__main__' else 'templates/seed.png'
    seed_templ: np.ndarray = cv2.imread(seed_path)
    seed_templ = cv2.cvtColor(seed_templ, cv2.COLOR_BGR2GRAY)

    # 2. 템플릿매칭
    seed_result: np.ndarray = cv2.matchTemplate(screen, seed_templ, cv2.TM_CCOEFF_NORMED)

    # 3. threshold 적용
    threshold = 0.98
    seed_location = set(zip(*np.where(seed_result >= threshold)[::-1]))

    # 4. 좌표를 중심으로 변경
    seed_location = [(int(x + (seed_templ.shape[1] / 2)), int(y + (seed_templ.shape[0] / 2))) for x, y in seed_location]

    return seed_location
