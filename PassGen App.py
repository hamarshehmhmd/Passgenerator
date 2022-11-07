
import string as digit
import secrets


class PasswordGenerator:
    @staticmethod
    def gen_sequence(
            conditions,
    ):  # must have  conditions (in a list format), for each member of the list possible_characters
        possible_characters = [
            digit.ascii_lowercase,
            digit.ascii_uppercase,
            digit.digits,
            digit.punctuation,
        ]
        sequence = ""
        for x in range(len(conditions)):
            if conditions[x]:
                sequence += possible_characters[x]
            else:
                pass
        return sequence

    @staticmethod
    def gen_password(sequence, passlength=8):
        password = "".join((secrets.choice(sequence) for _ in range(passlength)))
        return password


class Interface:
    has_characters = {
        "lowercase": True,
        "uppercase": True,
        "digits": True,
        "punctuation": True,
    }

    @classmethod
    def change_has_characters(cls, change):
        try:
            cls.has_characters[
                change
            ]  # to check if the specified key exists in the dictionary
        except Exception as err:
            print(f"Invalid \nan Exception: {err}")
        else:
            cls.has_characters[change] = not cls.has_characters[
                change
            ]  # automatically changers to the opposite value already there
            print(f"{change} is now set to {cls.has_characters[change]}")

    @classmethod
    def show_has_characters(cls):
        print(cls.has_characters)  # print the output

    def generate_password(self, lenght2):
        sequence = PasswordGenerator.gen_sequence(list(self.has_characters.values()))
        print(PasswordGenerator.gen_password(sequence, lenght2))


def list_to_vertical_string(list):
    to_return = ""
    for member in list:
        to_return += f"{member}\n"
    return to_return


def decide_operation():
    user_input = input(": ")
    try:
        int(user_input)
    except:
        Interface.change_has_characters(user_input)
    else:
        Interface().generate_password(int(user_input))
    finally:
        print("\n\n")


def run():
    menu = f"""Welcome to the PassGen App!
Commands:
generate password ->
<lenght of the password>

commands to change the characters to be used to generate passwords:
{list_to_vertical_string(Interface.has_characters.keys())}
        """
    print(menu)
    while True:
        decide_operation()


class Run:
    pass


run()
