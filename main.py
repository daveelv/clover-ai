from commands.open_apps import open_app, open_downloads
from commands.system_info import *

print("================================")
print(" CLOVER AI v0.2 ")
print("================================")

while True:

    command = input("\nClover> ").lower()

    if command == "exit":
        print("Goodbye.")
        break

    elif command.startswith("open "):

        app = command.replace("open ", "")
        open_app(app)

    elif command == "open downloads":
        open_downloads()

    elif command == "check cpu":
        print(f"CPU Usage: {cpu_usage()}%")

    elif command == "check ram":
        print(f"RAM Usage: {ram_usage()}%")

    elif command == "check disk":
        print(f"Disk Usage: {check_disk()}%")

    elif command == "show ip":
        print(f"IP Address: {show_ip()}")

    elif command == "show hostname":
        print(hostname())

    elif command == "system info":
        print(system_info())

    elif command == "list processes":
        print(list_processes())

    elif command == "battery status":
        print(battery_status())

    elif command == "take screenshot":
        print(take_screenshot())

    elif command == "what time is it":
        print(current_time())

    elif command == "wifi info":
        print(wifi_info())

    elif command == "check internet":
        print(internet_status())

    elif command == "internet status":
        print(internet_status())

    elif command == "system uptime":
        print(system_uptime())

    elif command == "lock pc":
        lock_pc()

    else:
        print("Command not recognized.")