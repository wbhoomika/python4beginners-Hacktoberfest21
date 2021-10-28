import time
from os import system

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:03d}:{:03d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    system('cls')
    print("halt")
    print("stop")

countdown(5)
