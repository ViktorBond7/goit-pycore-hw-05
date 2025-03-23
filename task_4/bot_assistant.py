from input_error import input_error

def parse_input(user_input: str) -> tuple[str, list[str]]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return "Contact added."
    else:
        return "contact with such a name exists"

@input_error
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
    else:
        return f'Error: Contact {name} not found'       
    return "Contact updated."

@input_error
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    name = args[0]
    return f"{contacts[name]}"

def show_all(contacts: dict[str, str]) -> str:
    if not contacts:
        return "has no contacts created"
    else:
        result = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
        return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        match command:
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(show_all(contacts))   
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()