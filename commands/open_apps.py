import os

def open_app(command):

    if command == "brave":
        os.system("start brave")

    elif command == "calculator":
        os.system("calc")

    elif command == "github":
        os.system("start https://github.com")

    elif command == "notepad":
        os.system("notepad")

    else:
        print("Application not recognized.")


def open_downloads():
    os.startfile(os.path.expanduser("~/Downloads"))