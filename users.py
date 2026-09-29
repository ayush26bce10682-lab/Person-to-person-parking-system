"""Input helpers shared by the parking and booking modules."""


def get_user_name(prompt):
    """Ask for a non-empty user name."""
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("Please enter a name.")


def read_positive_number(prompt):
    """Ask until the user enters a number greater than zero."""
    while True:
        try:
            number = float(input(prompt))
            if number > 0:
                return number
            print("Enter a number greater than zero.")
        except ValueError:
            print("Please enter a valid number.")
