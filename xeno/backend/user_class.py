from flask_login import UserMixin
from backbone import login_manager#, get_db
from flask import g
import database_connection as db_conn

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

    '''
        Validates user credentials. This is a class method, not instance method.
        last_modified_by: edlafem1
        @param uname: the given username
        @param passwd: the given password
    '''
    @staticmethod
    def validate_credentials(username, password):
        result = db_conn.query_db('SHOW TABLES')
        for row in result:
            print row[0] + ", ",
        print()

        print "Validating: ", username, ":", password
        # do a sql query here and return the User object
        if username == "Xeno" and password == "cars":
            userid = "testing"
            return User(userid)
        return None

'''
    # valid username
    user = user.first()
    stored_salted_password = user.password
    end_salt_pos = stored_salted_password.find('==') + 2
    salt = stored_salted_password[0:end_salt_pos]
    password = stored_salted_password[end_salt_pos:]
'''


def encode_password(password, salt=None):
    import uuid
    import hashlib
    import base64
    if salt == None:
        salt = base64.urlsafe_b64encode(uuid.uuid4().bytes)
    else:
        salt = salt.encode('utf-8')
    t_sha = hashlib.sha512()
    t_sha.update((password + salt.decode('utf-8')).encode('utf-8'))
    hashed_password = base64.urlsafe_b64encode(t_sha.digest())

    # hashed_password)
    return (salt+hashed_password).decode('utf-8')
