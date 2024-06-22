import datetime as dt
import subprocess


def submit(hour, minute):
    time = hour * 3600 + minute * 60
    cmd =f"shutdown /s /t {time}"
    if time == 0:
        return -1
    else:
        subprocess.run(["powershell", "-Command", cmd], capture_output=True)
        return 1
    
def cancel():
    cmd = "shutdown /a"
    subprocess.run(["powershell", "-Command", cmd], capture_output=True)


def set_brightness(brightness):
    cmd = f"(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{brightness})"
    subprocess.run(["powershell", "-Command", cmd], capture_output=True)

