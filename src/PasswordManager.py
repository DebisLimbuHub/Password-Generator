import hashlib
import getpass

password_manager = {}

def create_account():
    username = input("Please Enter a new username: ")
    password = getpass.getpass("Please Enter a new password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("The Account created successfully.")


def login():
    username = input("Please Enter your username: ")
    password = getpass.getpass("Please Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("The Login is successful!")
    else:
        print("Login failed. Invalid username or password.")

def main():
    while True:
        choice = input(" Enter 1 to Create Account, Enter 2 to Login, Enter 3 to Exit: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()







