import time
import pyautogui


def spamText(text, loops, sleep):
    time.sleep(sleep)
    for x in range(loops):
        try : text = text.split()
        except : text = text
        for words in text:
            pyautogui.typewrite(words)
            pyautogui.press('enter')


text = 'input your text here (or list if you wish)'
loops = 'number of times you want to print'
sleep = 'time you need to set up the screen after initiating the program'
spamText(text, loops, sleep)
