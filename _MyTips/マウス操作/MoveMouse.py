#!python3
import pyautogui
import random

# constants
MOVE_DISTSANCE = 60

# method
pyautogui.PAUSE = 2
pyautogui.FAILSAFE = True

def randomMove(screen_pos):
    pyautogui.moveTo(random.randint(0,screen_pos.width), random.randint(0,screen_pos.height), duration=random.random())


def main():
    """main process
    """
    # 画面中央に移動
    screen_pos = pyautogui.size()
    center_x = screen_pos.width / 2
    center_y = screen_pos.height / 2
    pyautogui.moveTo(center_x,center_y)

    try:
        x,y = pyautogui.position()

        while True:
            # pyautogui.moveTo(x, y + MOVE_DISTSANCE, duration=0.2)
            # pyautogui.moveTo(x - MOVE_DISTSANCE, y + MOVE_DISTSANCE, duration=0.2)
            # pyautogui.moveTo(x - MOVE_DISTSANCE, y, duration=0.2)
            for _ in range(random.randint(0,5)):
                randomMove(screen_pos)

            pyautogui.moveTo(x, y, duration=0.2)
            pyautogui.press('ctrl')

    except KeyboardInterrupt:
        print('end')


if __name__ == "__main__":
    print('start')
    print('停止するにはマウスを画面の四隅に移動するか')
    print('コマンドプロンプト上でCtrl+Cを入力してください（2回入力したほうがいいかも）')
    main()