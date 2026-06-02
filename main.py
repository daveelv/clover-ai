print("THIS IS THE NEW MAIN.PY")

from commands.open_apps import open_app, open_downloads
from commands.system_info import *
from commands.memory import *
from commands.voice import listen


def process_command(command):

    command = command.lower().strip()

    print(f"DEBUG: [{command}]")

    if command == "exit":
        print("Goodbye.")
        return False

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

    elif command == "who am i":
        print(who_am_i())

    elif command == "show profile":
        print(show_profile())

    elif command == "what do you know about me":

        print(
            what_do_you_know()
        )

    elif command.startswith("add note "):

        note = command.replace(
            "add note ",
            ""
        )

        print(add_note(note))

    elif command == "show notes":
        print(show_notes())

    elif command == "voice":

        print("Voice mode activated.")

        voice_command = listen()

        if voice_command:
            process_command(voice_command)

    elif command.startswith("remember "):

        memory = command.replace(
            "remember ",
            ""
        )

        print(remember(memory))


    elif command == "show memories":

        print(show_memories())


    elif command.startswith("forget "):

        memory = command.replace(
            "forget ",
            ""
        )

        print(forget(memory))

    elif command.startswith("add goal "):

        goal = command.replace(
            "add goal ",
            ""
        )

        print(add_goal(goal))

    elif command == "show goals":

        print(show_goals())

    elif command.startswith("add idea "):

        idea = command.replace(
            "add idea ",
            ""
        )

        print(add_idea(idea))

    elif command == "show ideas":

        print(show_ideas())

    else:
        print("Command not recognized.")

    return True


print("================================")
print(" CLOVER AI v0.3 ")
print("================================")

running = True

while running:

    command = input("\nClover> ")

    running = process_command(command)