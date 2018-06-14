class Credential:
    '''
    Will generate new instances of account credentials
    '''
    credential_list = []

    def __init__(self, user_name, login_password):
        '''
        Passed in three arguments of the isntances of our variables
        '''
        self.user_name = user_name
        self.login_password = login_password

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
    def find_by_user_name(cls, user_name):
        """
        this method will take a user_name and
        return an account that matches that user_name
        """

        for credential in cls.credential_list:
            if credential.user_name == user_name:
                return credential
    
    @classmethod
    def password_gen(cls, password_length):
        string = "abcdefghigjkmnopqrstuvwxyz1234567890-_=+{}\|"';>./,`!@#$^&*()`'
        password = "".join(random.sample(string, int(password_length)))
        credential_passsword = password
        return credential_passsword
