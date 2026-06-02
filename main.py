from commands.open_apps import open_app
from commands.system_info import cpu_usage, ram_usage
from commands.system_info import *


print("================================")
print(" CLOVER AI v0.1 ")
print("================================")

while True:

    command = input("\nClover> ").lower()

    if command == "exit":
        print("Goodbye.")
        break

    elif command.startswith("open "):

        app = command.replace("open ", "")
        open_app(app)

    elif command == "check cpu":

        print(f"CPU Usage: {cpu_usage()}%")

    elif command == "check ram":

        print(f"RAM Usage: {ram_usage()}%")

    elif command == "check disk":
        print(f"Disk Usage: {check_disk()}%")

    elif command == "show ip":
        print(f"IP Address: {show_ip()}")

    elif command == "system info":
        print(system_info())

    elif command == "list processes":
        print(list_processes())

    else:

        print("Command not recognized.")

