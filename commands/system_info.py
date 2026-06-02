
import psutil
import socket
import platform
import os

def cpu_usage():
    return psutil.cpu_percent(interval=1)

def ram_usage():
    return psutil.virtual_memory().percent

def check_disk():
    return psutil.disk_usage('/').percent

def show_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

def system_info():
    return platform.platform()

def ping(target):
    os.system(f"ping {target}")

def list_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        print(proc.info)