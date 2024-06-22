import datetime as dt
import subprocess


def submit(hour, minute, brightness):
    time = hour * 3600 + minute * 60
    cmd1 = f"shutdown /s /t {time}"
    cmd2 = f"(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{brightness})"
    cmd = cmd1 + ";" + cmd2
    if time == 0:
        return -1
    else:
        subprocess.run(["powershell", "-Command", cmd], capture_output=True)
        return 1
    
def cancel(brightness):
    cmd2 = f"(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{brightness})"
    cmd = "shutdown /a" + ";" + cmd2

    subprocess.run(["powershell", "-Command", cmd], capture_output=True)


def set_brightness(brightness):
    cmd = f"(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{brightness})"
    subprocess.run(["powershell", "-Command", cmd], capture_output=True)

set_brightness(50)