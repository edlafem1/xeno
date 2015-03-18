from flask_login import UserMixin
#from backbone import login_manager


class User(UserMixin):
    '''
        Next few methods are overridden from UserMixin class to provide other than default values
        last_modified_by: edlafem1
    '''


    @property
    def is_active(self):
        return self.active


    @property
    def is_authenticated(self):
        return self.authenticated


    @property
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
        self.authenticated = False
        self.anonymous = True
        self.exists = True

    '''
        Validates user credentials. This is a class method, not instance method.
        last_modified_by: edlafem1
        @param uname: the given username
        @param passwd: the given password
    '''
    def auth_user(cls, uname, passwd):
        #check against db for correct combo, if correct, get userid
        userid = 'lala'
        return load_user(userid)

#@login_manager.user_loader
def load_user(userid):
    user = User(userid)
    if user.exists == False:
        return None
    return User(userid)
#login_manager.user_loader(load_user)