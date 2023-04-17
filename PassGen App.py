import string
import secrets
from typing import List, Dict


class PasswordGenerator:
    @staticmethod
    def gen_sequence(conditions: List[bool]) -> str:
        """Generate a sequence of characters based on given conditions.

        Args:
            conditions: A list of boolean values indicating whether to include each character type.

        Returns:
            A string containing the characters to be used for password generation.
        """
        possible_characters = [
            string.ascii_lowercase,
            string.ascii_uppercase,
            string.digits,
            string.punctuation,
        ]
        sequence = ""
        for i, condition in enumerate(conditions):
            if condition:
                sequence += possible_characters[i]
        return sequence

    @staticmethod
    def gen_password(sequence: str, passlength: int = 8) -> str:
        """Generate a password from a given sequence of characters.

        Args:
            sequence: A string containing the characters to be used for password generation.
            passlength: The length of the password to be generated. Default is 8.

        Returns:
            A string containing the generated password.
        """
        password = "".join((secrets.choice(sequence) for _ in range(passlength)))
        return password


class Interface:
    CHARACTER_TYPES: Dict[str, bool] = {
        "lowercase": True,
        "uppercase": True,
        "digits": True,
        "punctuation": True,
    }

    @classmethod
    def change_character_type(cls, change: str) -> None:
        """Toggle the value of a given character type in the dictionary.

        Args:
            change: A string indicating which character type to toggle.

        Raises:
            KeyError: If the specified key does not exist in the dictionary.
        """
        if change not in cls.CHARACTER_TYPES:
            raise KeyError(f"Invalid character type: {change}")
        cls.CHARACTER_TYPES[change] = not cls.CHARACTER_TYPES[change]
        print(f"{change} is now set to {cls.CHARACTER_TYPES[change]}")

    @classmethod
    def show_character_types(cls) -> None:
        """Print the current values of the character types dictionary."""
        print(cls.CHARACTER_TYPES)

    def generate_password(self, length: int) -> None:
        """Generate a password based on the current character type settings and print it to the console.

        Args:
            length: The length of the password to be generated.
        """
        sequence = PasswordGenerator.gen_sequence(list(self.CHARACTER_TYPES.values()))
        password = PasswordGenerator.gen_password(sequence, length)
        print(f"Generated password: {password}")

    @classmethod
    def print_menu(cls) -> None:
        """Print the program menu to the console."""
        print(
            "Welcome to the PassGen App!\n"
            "Commands:\n"
            "  generate password -> <length of the password>\n"
            "  commands to change the characters to be used to generate passwords:\n"
            f"{cls._format_character_types()}")

    @classmethod
    def _format_character_types(cls) -> str:
        """Return a formatted string containing the character types dictionary."""
        return "\n".join(f"  {k}: {v}" for k, v in cls.CHARACTER_TYPES.items())


def decide_operation() -> None:
    """Get user input and execute the appropriate command."""
    user_input = input(": ")
    try:
        length = int(user_input)
        Interface().generate_password(length)
    except ValueError:
        try:
            Interface.change_character_type(user_input)
        except KeyError as err:
            print(f"Invalid character type: {err}")
        else:
            Interface.show_character_types()
    finally:
        print("\n")



def run() -> None:
    """Run the PassGen program."""
    Interface.print_menu()
    while True:
        decide_operation()


if __name__ == "__main__":
    run()

