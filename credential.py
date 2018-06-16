import random

class Credential:
    '''
    Will generate new instances of account credentials
    '''
    credential_list = []

    def __init__(self, account_name, password):
        '''
        Passed in three arguments of the isntances of our variables
        '''
        self.account_name = account_name
        self.password = password

    def save_credential(self):
        '''
        saving credential object into object list
        '''
        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        Will delete any credentials saved in the account_list
        '''
        Credential.credential_list.remove(self)

    
    @classmethod
    def display_credential(cls, user_name):
        """
        this method will take a user_name and
        return credentials that matches that user_name
        """

        for credential in cls.credential_list:
            if credential.user_name == user_name:
                return credential
