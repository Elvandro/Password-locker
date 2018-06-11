class User:
    """
    Class that generates new instances of users
    """
    user_list = [] #Empty user list

    def __init__(self,user_name, password):

        """
        __init__ method helps us define our object
        Args:
            user_name: New user name.
            password: New user password.
        """
        self.user_name = user_name
        self.password = password
