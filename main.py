from passlib.handlers.sha2_crypt import sha512_crypt as hasher
from getpass import getpass


def account_creation():
    username = input("Please enter a username: ")
    password = getpass("Please enter a password: ")
    hashed_password = hasher.hash(password, rounds=200_000)
    database_create(username, hashed_password)


def database_create(username, password):
    file = open(f"{username}.txt", "w")
    file.write(password)
    file.close()
    print("Account created.")


if __name__ == "__main__":
    account_creation()
