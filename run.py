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

# def copy_password(account_name):
#    '''
#    Function that allows us to copy a password from their account_name
#    '''
#    return Passwords.copy_password()

def password_gen(password_length):
    return Passwords.password_gen(password_length)

def main():
    print("Hello! Welcome to Password Locker. What is your name?")
    user_name = input()
    print("")

    print(f "Hi {user_name}, would you like to create a new account or log in to your already existing account?")
    print(""" Use these short codes:
            cn - to create a new account
            li - to log in to your already existing account
            """)
    while True:
        short_code = input().lower
        print('_'*100)
        if short_code == "cn":
            print("New Password Locker Account")
            print("_" * 20)

            print("Enter a preferred user name")
            name = input()        
