import random
from csl import agenda, optionmains, options_menu
import pyautogui
from data import eventos as events
import time

time.sleep(5)


def test_random_task(events):
    count = 0
    for event in events:
        count += 1
        if count == 3: 
            return
        pyautogui.typewrite('1')
        pyautogui.press('enter')
        time.sleep(1)
        nome, data, horario = event
        print(data)
        pyautogui.typewrite(nome)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite(data)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite(horario)
        pyautogui.press('enter')
        time.sleep(3)


def test_search(events):
    count = 0
    for event in events:
        count += 1
        if count == 3: 
            return
        nome, data, horario = event
        pyautogui.typewrite('2')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite(nome)
        pyautogui.press('enter')
        time.sleep(3)


#test_random_task(events)
test_search(events)

