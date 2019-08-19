""" Jayde Amos """

MIN_LENGTH = 5


def main():
    password = input("Enter password of at least 5 characters: ")
    while len(password) < MIN_LENGTH:
        password = input("Enter password of at least 5 characters: ")
    print("You password is", '*' * len(password))


main()
