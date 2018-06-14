class User:
    """
    Class that generates new instances of users
    """
    user_list = []

    def __init__(self, user_name, password):

        """
        __init__ method helps us define our object
        Args:
            user_name: New user name.
            password: New user password.
        """
        self.user_name = user_name
        self.password = password

    def save_user(self):
        """
        save_user method saves the users object into our user_list
        """
        User.user_list.append(self)

    @classmethod
    def search_user_exists(cls, user_name):
        """
        method to check is a user exists
        """
        for user in cls.user_list:
            if user_name == user_name:
                return user
