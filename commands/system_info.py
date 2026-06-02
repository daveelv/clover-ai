import psutil
import socket
import requests
import os
import ctypes

from datetime import datetime
from PIL import ImageGrab


def cpu_usage():
    return psutil.cpu_percent(interval=1)


def ram_usage():
    return psutil.virtual_memory().percent


def check_disk():
    return psutil.disk_usage('/').percent


def show_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)


def system_info():

    return (
        f"CPU: {cpu_usage()}%\n"
        f"RAM: {ram_usage()}%\n"
        f"Disk: {check_disk()}%\n"
        f"IP: {show_ip()}"
    )


def list_processes():

    processes = []

    for proc in psutil.process_iter(['pid', 'name']):

        try:
            processes.append(
                f"{proc.info['pid']} - {proc.info['name']}"
            )

        except Exception:
            pass

    return "\n".join(processes[:30])


def hostname():
    return socket.gethostname()


def battery_status():

    battery = psutil.sensors_battery()

    if battery:
        return f"Battery: {battery.percent}%"

    return "No battery detected."


def take_screenshot():

    image = ImageGrab.grab()

    image.save("screenshot.png")

    return "Screenshot saved."


def current_time():

    return datetime.now().strftime("%I:%M:%S %p")


def internet_status():

    try:

        requests.get(
            "https://www.google.com",
            timeout=3
        )

        return "Internet Connected"

    except Exception as e:

        return f"No Internet: {e}"


def wifi_info():

    output = os.popen(
        "netsh wlan show interfaces"
    ).read()

    return output


def system_uptime():

    boot_time = datetime.fromtimestamp(
        psutil.boot_time()
    )

    return f"System started: {boot_time}"


def lock_pc():

    ctypes.windll.user32.LockWorkStation()


def kill_process(process):

    os.system(
        f"taskkill /f /im {process}"
    )