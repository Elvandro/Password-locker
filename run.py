from user import User
from credential import Credential
import random

def create_user(user_name, password):
    '''
    creates a new user
    '''
    new_user = User(user_name, password)
    return new_user

def save_user(user):
    '''
    will save new_users
    '''
    User.save_user()

def user_exists(user_name):
    '''
    will search for user using user_name
    '''
    return User.user_exists(user_name)

def create_profile(user_name, password):
    """
    Function to create new_profile
    """
    new_profile = Passwords(user_name, password)
    return new_profile


def save_profile(credential):
    """
    Function to save profile
    """
    credential.save_profile()


def password_gen(password_length):
    return password_length.password_gen(password_length)

def main():
    print("Hello! Welcome to Password Locker. What is your name?")
    name = input()
    print("")

    print(f"Hi {name}, would you like to create a new account or log in to your already existing account?")
    print(""" Use these short codes:
            new - to create a new account
            sign - to log in to your already existing account
            """)
    while True:
        short_code = input().lower()
        print('_'*100)
        if short_code == "new":
            print("New Password Locker Account")
            print("__" * 20)

            print("Enter a preferred user name")
            user_name = input()

            print("We can generate a password for you or you can set it by yourself")
            print("""Use these short codes:
                    gen-To generate a password
                    make-To make a password on your own""")
            code = input().lower()
            print("__" * 20)
            if code == "gen":
                password_length = int(input("How many characters do you wish your password should have"))

                password = password_gen(password_length)
                print(f"Your password is {password}")
            else:
                print("write a password of your own")
                password = input()

        save_user(create_profile(user_name,password))

    print("You successfully created your new account")
    print("You can now create your password profiles")

if __name__ == '__main__':
    main()
