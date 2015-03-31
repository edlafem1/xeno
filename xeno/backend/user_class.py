from flask_login import UserMixin
from backbone import login_manager


class User(UserMixin):
    '''
        Next few methods are overridden from UserMixin class to provide other than default values
        last_modified_by: edlafem1
    '''

    def is_active(self):
        return self.active

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return self.anonymous


    '''
        Creates a User object and initializes all properties and attributes.
        Should provide functions for updating the database as profile information changes.
        TODO: Create functions to get data from database
        last_modified_by: edlafem1
        @param user_id: a string value for the users's id.
    '''
    def __init__(self, user_id):
        self.id = user_id
        self.active = True
        self.authenticated = True
        self.anonymous = True
        self.exists = True
        print(type(self), self)

    '''
        Validates user credentials. This is a class method, not instance method.
        last_modified_by: edlafem1
        @param uname: the given username
        @param passwd: the given password
    '''
    @staticmethod
    def validate_credentials(username, password):
        print("Validating: ", username, ":", password)
        # do a sql query here and return the User object
        if username == "Xeno" and password == "cars":
            userid = "testing"
            return User(userid)
        return None
'''
#edlafem1-these dont seem to exist in backbone.py
    # @login_manager.user_loader
    @staticmethod
    def load_user(userid):
        # get user info from DB here, validate userid is a valid User in DB.
        user = User(userid)
        print(vars(user))
        if user.exists == False:
            return None
        return user

    @classmethod
    def get_login_callback(cls):
        login_manager.user_callback = cls.load_user
'''