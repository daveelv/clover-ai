import json

PROFILE_FILE = "memory/profile.json"


def load_profile():

    try:
        with open(PROFILE_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}


def save_profile(profile):

    with open(PROFILE_FILE, "w") as file:
        json.dump(profile, file, indent=4)


def remember(memory):

    profile = load_profile()

    key = f"memory_{len(profile)}"

    profile[key] = memory

    save_profile(profile)

    return f"Remembered: {memory}"


def show_profile():

    profile = load_profile()

    output = ""

    for key, value in profile.items():
        output += f"{key}: {value}\n"

    return output

def what_do_you_know():

    profile = load_profile()

    if not profile:
        return "I do not know anything yet."

    output = []

    output.append("Here is what I know about you:\n")

    for key, value in profile.items():

        output.append(
            f"- {value}"
        )

    return "\n".join(output)

def show_memories():

    profile = load_profile()

    memories = []

    for key, value in profile.items():

        if key.startswith("memory_"):

            memories.append(value)

    if not memories:

        return "No memories stored."

    return "\n".join(memories)

def add_goal(goal):

    with open(
        "memory/goals.md",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(f"- {goal}\n")

    return "Goal saved."

def show_goals():

    try:

        with open(
            "memory/goals.md",
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read()

        return content if content else "No goals saved."

    except FileNotFoundError:

        return "No goals saved."

def add_idea(idea):

    with open(
        "memory/ideas.md",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(f"- {idea}\n")

    return "Idea saved."

def show_ideas():

    try:

        with open(
            "memory/ideas.md",
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read()

        return content if content else "No ideas saved."

    except FileNotFoundError:

        return "No ideas saved."