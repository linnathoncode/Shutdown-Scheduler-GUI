import datetime as dt
import os


def submit(hour, minute):
    time = hour * 3600 + minute * 60
    if time == 0:
        return -1
    else:
        os.system(f"shutdown /s /t {time}")
        return 1
    
def cancel():
    os.system("shutdown /a")


