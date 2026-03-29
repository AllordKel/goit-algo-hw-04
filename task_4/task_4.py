from pathlib import Path
from normalize_phone_3 import normalize_phone


def parse_input(user_input):
    """Normalize input into command and positional arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def load_file(path="contacts.txt"):
    """Load contacts from a plain text file as a dictionary.

    The file format is one contact per line:
        name:phone
    """
    p = Path(path)
    if not p.exists():
        return {} # File may not exist on first run; return an empty phonebook

    contacts = {}
    with open(p, "r", encoding="utf-8") as fh:
        lines = [el.strip() for el in fh.readlines()]

    for line in lines:
        if not line or ":" not in line:
            continue # Skip empty or malformed lines
        name, phone = line.split(":")
        contacts[name.strip()] = phone.strip()
    return contacts


def save_file(contacts, path="contacts.txt"):
    """Save contacts dictionary to a plain text file."""
    with open(Path(path), "w", encoding="utf-8") as phone_directory:
        for name, phone in contacts.items():
            phone_directory.write(f"{name}:{phone}\n")


def update_contact(args, update=False):
    """Create or update a contact."""
    if len(args) != 2:
        return "Invalid input"

    contacts = load_file()
    name, phone = args
    if (name.lower() in contacts and not update) or (name.lower() not in contacts and update):
        return "comand_missmatch"
    contacts[name.lower()] = normalize_phone(phone)
    save_file(contacts)
    return "Contact updated." if update else "Contact added."


def show_all():
    """Display all contacts or a specific message when phonebook is empty."""
    contacts = load_file()
    if not contacts:
        return "Phonebook is empty, save some contacts first"

    output = []
    for name, phone in contacts.items(): # Returning all contacts
        output.append(f"{name}: {phone}")
    return "\n".join(output)


def show_phone(args):
    """Retrieve the phone number for a specific contact."""
    if len(args) != 1:
        return "Invalid input"
    contacts = load_file()
    if args[0] not in contacts:
        return "Contact not found."
    return contacts[args[0]]


def main():
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("Hello, how can I help you?")

        elif command == "add":
            update_answer = update_contact(args)
            if update_answer == "comand_missmatch":
                user_input = input("Such contact already exists, do you want to update? ")
                if user_input.lower() == "yes":
                    print(update_contact(args, True))
                else:
                    continue
            else:
                print(update_answer)

        elif command == "change":
            update_answer = update_contact(args, True)
            if update_answer == "comand_missmatch":
                user_input = input("Such contact does not exist, do you want to create? ")
                if user_input.lower() == "yes":
                    print(update_contact(args))
                else:
                    continue
            else:
                print(update_answer)

        elif command == "phone":
            print(show_phone(args))

        elif command == "all":
            print(show_all())

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
