class User:
    """
    Class that generates new instances of users
    """
    user_list = []

    def __init__(self, user_name, email, password):

        """
        __init__ method helps us define our object
        Args:
            user_name: New user name.
            email: New user email.
            password: New user password.
        """
        self.user_name = user_name
        self.email = email
        self.password = password

    def save_user(self):
        """
        save_user method saves the users object into our user_list
        """
        User.user_list.append(self)

    @classmethod
        """
        method to display a user
        """
        def display_user(cls, user_name):
            for user in cls.user_list:
                if user_name = user_name:
                    return user
