from user import User
from credential import Credential

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

def copy_password(account_name):
    '''
    Function that allows us to copy a password from their account_name
    '''
    return Passwords.copy_password()
