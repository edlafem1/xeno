from flask_login import UserMixin
import database_connection as db_conn
import datetime

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

    def get_reviews(self):
        query = "SELECT `reviews`.`date_created`, `reviews`.`num_stars`, `reviews`.`text`, `reviews`.`car` FROM `reviews` " \
                "WHERE `reviews`.`reviewer`=%s"
        result = db_conn.query_db(query, [self.db_id])
        print result
        return result

    def get_favorite_car(self):
        subquery = "SELECT `reservations`.`for_car` AS car_id, COUNT(*) AS num_rentals FROM `reservations` " \
                "WHERE `reservations`.`made_by`='%s' GROUP BY `reservations`.`for_car` " \
                "ORDER BY `reservations`.`for_date`"
        max_query = "SELECT car_id, MAX(num_rentals) FROM (" + subquery + ") AS sub"
        car_query = "SELECT `cars`.`id` FROM (" + max_query + ") AS max JOIN `cars` WHERE `cars`.`id=cars_id"

        query = "SELECT cars.id AS id, cars.year AS year, cars.hp AS hp, cars.torque AS torque, cars.miles_driven AS odo, " \
                "cars.acceleration AS acceleration, cars.max_speed AS max_speed, make.description AS make, " \
                "model.description AS model, cars.date_added AS date_added, cars.is_featured AS is_featured, " \
                "make.id " \
                " FROM (" + max_query + ") AS final " \
                "JOIN `cars` ON `cars`.`id`=car_id " \
                "JOIN make ON cars.make=make.id " \
                "JOIN model ON cars.model=model.id "

        result = db_conn.query_db(query, [self.db_id])
        print "Favorite Car Data: "
        print result
        return result


    '''
        Creates a User object and initializes all properties and attributes.
        Should provide functions for updating the database as profile information changes.
        TODO: Create functions to get data from database
        last_modified_by: edlafem1
        @param user_id: a string value for the users's id.
    '''
    def __init__(self, user_id, udata=None):
        #print "Creating new user: " + user_id + str(udata)
        #import inspect
        #curframe = inspect.currentframe()
        # = inspect.getouterframes(curframe, 2)
        #print 'caller name: ', calframe[1][3]

        self = User.init_user(self, user_id)
            
    @staticmethod
    def init_user(u, user_id):    
        udata = db_conn.query_db('SELECT * FROM `xeno`.`users` WHERE `userid`=%s', [user_id], one=True)
        if udata is not None:
            u.db_id = udata["id"]
            u.fname = udata["first_name"]
            u.lname = udata["last_name"]
            u.date_joined = udata["date_joined"]
            u.credits = udata["credits"]
            u.acct_type = udata["acct_type"]

            # http://stackoverflow.com/questions/14291636/what-is-the-proper-way-to-convert-between-mysql-datetime-and-python-timestamp
            # time_format = '%Y-%m-%d %H:%M:%S'
            u.suspended_til = udata["suspended_until"]  # .strftime(time_format)
            now = datetime.datetime.now()
            if udata["suspended_until"] is not None and now < udata["suspended_until"]:
                u.suspended = True
            else:
                u.suspended = False

            u.id = user_id
            u.active = True
            u.authenticated = True
            u.anonymous = True
            u.exists = True
        else:
            u.active = False
            u.authenticated = False
            u.anonymous = False
            u.exists = False
            u.id = None
        return u

    @staticmethod
    def create_new_user(user_data, acct_type=3):
        '''user_data should have full_name, password, email'''
        first_name_space = user_data["full_name"].find(" ")
        fname = user_data["full_name"][0:first_name_space]
        lname = user_data["full_name"][first_name_space + 1:]
        hpass = encode_password(user_data["password"])
        user_id = user_data["email"]

        query = "INSERT INTO `xeno`.`users` " \
                "(`first_name`, `last_name`, `credits`, `acct_type`, `userid`, `hpass`)" \
                "VALUES (%s, %s, 100, %s, %s, %s)"
        args = [fname, lname, acct_type, user_id, hpass]
        #print query, args
        result = db_conn.query_db(query, args, select=False)
        #print "Attempted create user: ", result
        return result




    '''
        Validates user credentials. This is a class method, not instance method.
        last_modified_by: edlafem1
        @param uname: the given username
        @param passwd: the given password
    '''
    @staticmethod
    def validate_credentials(username, password):
        user = db_conn.query_db('SELECT * FROM `xeno`.`users` WHERE `userid`=%s', [username], True)

        #print "Validating: ", username, ":", password
        if user is None:  # not a valid username
            return None

        stored_salted_password = user["hpass"]
        end_salt_pos = stored_salted_password.find('==') + 2
        salt = stored_salted_password[0:end_salt_pos]
        # stored_password = stored_salted_password[end_salt_pos:] # this isnt needed I dont think...

        if stored_salted_password == encode_password(password, salt):
            userid = user["userid"]
            return User(userid, user)
        ''' This is a simple test.
        if username == "Xeno" and password == "cars":
            userid = "testing"
            return User(userid)
        '''
        return None

'''
    # valid username
    user = user.first()
    stored_salted_password = user.password
    end_salt_pos = stored_salted_password.find('==') + 2
    salt = stored_salted_password[0:end_salt_pos]
    password = stored_salted_password[end_salt_pos:]

    if user.password == encode_password(data["password"], salt):
        we good
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
