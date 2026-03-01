def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    name, phone = args

    if name in contacts:
        contacts[name] = phone
        return "Contact updated"
    else:
        return "Contact name not found"


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    name = args[0]

    if name in contacts:
        return contacts[name]
    else:
        return "Contact name not found"


def show_all(args: list[str], contacts: dict[str, str]) -> dict[str, str]:
    if contacts:
        return contacts
    else:
        return "No contacts saved"
    


def main() -> None:
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()