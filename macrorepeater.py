import time

import pyautogui

def run(repeat, number, timebetween):
    time.sleep(5)  # time to move to text field
    for i in range(0, int(number)):
        pyautogui.typewrite(repeat)
        time.sleep(int(timebetween))


if __name__ == "__main__":
    repeat = input("What macro do you want to repeat: ")
    number = input("How many times: ")
    timebetween = input("Time between repeats: ")
    run(repeat, number, timebetween)
