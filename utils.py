import datetime as dt
import os
import subprocess


def submit(hour, minute):
    time = hour * 3600 + minute * 60
    if time == 0:
        return -1
    else:
        os.system(f"shutdown /s /t {time}")
        set_brightness(0)
        return 1
    
def cancel():
    os.system("shutdown /a")
    set_brightness(50)

def set_brightness(brightness):
    cmd = f"(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{brightness})"
    subprocess.run(["powershell", "-Command", cmd], capture_output=True)

