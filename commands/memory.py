import json


PROFILE_PATH = "memory/profile.json"
NOTES_PATH = "memory/notes.json"


def show_profile():

    with open(PROFILE_PATH, "r") as file:

        profile = json.load(file)

    return json.dumps(profile, indent=4)


def who_am_i():

    with open(PROFILE_PATH, "r") as file:

        profile = json.load(file)

    return (
        f"Name: {profile['name']}\n"
        f"Course: {profile['current_course']}\n"
        f"Career Goal: {profile['career_goal']}"
    )


def add_note(note):

    with open(NOTES_PATH, "r") as file:

        notes = json.load(file)

    notes.append(note)

    with open(NOTES_PATH, "w") as file:

        json.dump(notes, file, indent=4)

    return "Note saved."


def show_notes():

    with open(NOTES_PATH, "r") as file:

        notes = json.load(file)

    if not notes:
        return "No notes saved."

    return "\n".join(notes)