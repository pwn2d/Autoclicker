import pyautogui
import keyboard
import threading

def left_clicker():
    while True:
        while keyboard.is_pressed('r') == True:
            x = pyautogui.position()
            pyautogui.click(x)

def right_clicker():
    while True:
        while keyboard.is_pressed('t') == True:
            x = pyautogui.position()
            pyautogui.click(x, button='right')


for i in range(20):
    thread1 = threading.Thread(target=right_clicker)
    thread = threading.Thread(target=left_clicker)
    thread1.start()
    thread.start()




