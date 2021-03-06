import database_connection as db_conn
import datetime, time
import user_class
import searching


def get_cars(page, howmany, get_new=False, get_featured=False, search_params=None, isAdmin=False):
    """
    This function controls getting details for multiple cars at a time. It should be noted that setting get_new=True
    and get_featured=True is the same as get_featured=True, so setting get_new=True is redundant.
    Setting get_featured=True and get_new=False is the same as get_featured=True so setting get_new=False is redundant
    :param page: An integer representing which section of data wanted
    :param howmany: An integer representing how many cars should be retrieved. Used in calculating page data
    :param get_new: Boolean that is True if cars should be ordered only by date_added. Default is False
    :param get_featured: Boolean that is True if cars should be sorted by featured or not(featured first) and then
            by date. Default is False.
    :param search_params: A dictionary to be used the search functionality. Either contains 1 key named "general"
            or 3 keys named "year", "make", and "model". Additional keys may be added later.
    :return: A dictionary of cars, None if no cars found. Keys in the dictionary are: id, year, hp, torque, odo,
    acceleration, max_speed, make, model, date_added, is_featured, make_id. Their values are representative of
    their data type in the database.
    """
    #print "getting cars!"
    args = []
    offset = 0
    query = "SELECT cars.id AS id, cars.year AS year, cars.hp AS hp, cars.torque AS torque, cars.miles_driven AS odo, " \
        "cars.acceleration AS acceleration, cars.max_speed AS max_speed, make.description AS make, " \
        "model.description AS model, cars.date_added AS date_added, cars.is_featured AS is_featured, " \
        "make.id AS make_id " \
        "FROM cars " \
        "JOIN make ON cars.make=make.id " \
        "JOIN model ON cars.model=model.id "
    if not isAdmin:
        query += "WHERE cars.status<=3 "
    else:
        query += "WHERE 1=1 "
    if search_params is not None:
        where_clause, args = searching.create_search_query(search_params)
        query += where_clause
        # print("get_cars: " + where_clause)
    if get_new is False and get_featured is False:
        query += "ORDER BY make.id DESC, cars.date_added DESC "
    elif get_new is True and get_featured is False:
        query += "ORDER BY cars.date_added DESC "
        howmany = 8
        offset = 0
        page = 1
    elif get_featured is True:
        # query += "WHERE cars.is_featured=1 "
        # to force there to be some car that is featured(even if none is marked), do not use WHERE, use ORDER BY
        query += "ORDER BY cars.is_featured DESC, cars.date_added DESC "
        howmany = 4
        offset = 0
        page = 1

#    query = "SELECT * FROM `xeno`.`cars` ORDER BY `make` ASC"
    if howmany > 0:
        offset = (page - 1) * howmany
        query += "LIMIT " + str(offset) + ", " + str(howmany)  # LIMIT offset,row_count
    elif howmany == -1:
        offset = 0
    car_data = db_conn.query_db(query, args)
    return car_data


def get_single_car(id, isAdmin):
    query = "SELECT cars.id AS id, cars.year AS year, cars.hp AS hp, cars.torque AS torque, cars.miles_driven AS odo, " \
            "cars.acceleration AS acceleration, cars.max_speed AS max_speed, make.description AS make, " \
            "model.description AS model, cars.date_added AS date_added, cars.is_featured AS is_featured, " \
            "make.id AS make_id, car_type.description AS ctype, country.description AS country, " \
            "cars.status AS status " \
            "FROM cars " \
            "JOIN make ON cars.make=make.id " \
            "JOIN model ON cars.model=model.id " \
            "JOIN car_type ON cars.type=car_type.id " \
            "JOIN country ON cars.country=country.id "
    query += "WHERE cars.id=%s "
    if not isAdmin:
        query += "AND cars.status<=3 "
    query += "LIMIT 1"

    car_data = db_conn.query_db(query, [id], one=True)
    return car_data


def get_car_reviews(id):
    query = "SELECT reviews.date_created AS date_created, reviews.num_stars AS num_stars, reviews.text AS text, " \
            "users.first_name AS fname, users.last_name AS lname " \
            "FROM reviews " \
            "JOIN users ON reviews.reviewer=users.id " \
            "WHERE car=%s " \
            "ORDER BY date_created DESC"
    result = db_conn.query_db(query, [id])
    return result

def add_new_car(cdata, current_user):
    """
    Attempts to insert a new car into the database by first querying to see if things such as the make, model, country,
    and type already have entries in their respective tables, creating them if need be, and then using those ids to
    populate the cars table with related fields and details specific to the car.
    :param cdata: A dictionary representing data from the form. Keys should be: make, model, ctype, country, year, hp,
    torque, odo, acceleration, max_speed, and is_featured. Data type should be clear from the form.
    :param current_user: The user currently logged into the site. Should be an instance of type User
    :return: The id of the car just added, or None if error occurred.
    """
    query = "SELECT id FROM make WHERE description=%s"
    make_id = db_conn.query_db(query, [cdata["make"].lower()], one=True)
    if make_id is None:
        query = "INSERT INTO make (`description`) VALUES (%s)"
        make_id = db_conn.query_db(query, [cdata["make"]], select=False)
        #print "Make id" + str(make_id)
    else:
        make_id = int(make_id["id"])
        #print "Make id already there as " + str(make_id)

    query = "SELECT id FROM model WHERE description=%s"
    model_id = db_conn.query_db(query, [cdata["model"].lower()], one=True)
    if model_id is None:
        query = "INSERT INTO model (`description`) VALUES (%s)"
        model_id = db_conn.query_db(query, [cdata["model"]], select=False)
        #print "Model id" + str(model_id)
    else:
        model_id = int(model_id["id"])
        #print "Model id already there as " + str(model_id)

    query = "SELECT id FROM car_type WHERE description=%s"
    car_type = db_conn.query_db(query, [cdata["ctype"].lower()], one=True)
    if car_type is None:
        query = "INSERT INTO car_type (`description`) VALUES (%s)"
        car_type = db_conn.query_db(query, [cdata["ctype"]], select=False)
        #print "Car Type id" + str(car_type)
    else:
        car_type = int(car_type["id"])
        #print "Car Type already there as " + str(car_type)

    query = "SELECT id FROM country WHERE description=%s"
    country_id = db_conn.query_db(query, [cdata["country"].lower()], one=True)
    if country_id is None:
        query = "INSERT INTO country (`description`) VALUES (%s)"
        country_id = db_conn.query_db(query, [cdata["country"]], select=False)
        #print "Country id" + str(country_id)
    else:
        country_id = int(country_id["id"])
        #print "Country id already there as " + str(country_id)

    is_featured = 0
    if cdata["is_featured"] == "on":
        is_featured = 1

    query = "INSERT INTO cars (make, model, year, country, type, hp, torque, miles_driven, acceleration, max_speed, added_by, is_featured)" \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    result = False
    try:
        result = db_conn.query_db(query, [make_id, model_id, int(cdata["year"]), country_id, car_type,
                                        int(cdata["hp"]), int(cdata["torque"]), int(cdata["odo"]),
                                        float(cdata["acceleration"]), int(cdata["max_speed"]), current_user.db_id, is_featured],
                                        select=False)
    except Exception, e:
        result = False
        print repr(e)

    return result

def make_reservation(car_id, text_date, user):
    credits_required = 50  # hard coded

    #  check if user has enough credits
    query = "SELECT credits FROM users WHERE id=%s"
    result = db_conn.query_db(query, [user.db_id], one=True)
    num_credits = 0
    if result is not None:
        num_credits = result["credits"]
    if num_credits < credits_required:
        return "You do not have enough credits."
    # month, day, year
    date_list = text_date.split("/")
    
#    current_time = datetime.datetime.now() - datetime.timedelta(hours=5)
#    if current_time > datetime.datetime(int(date_list[2]), int(date_list[0]), int(date_list[1])):
 
    current_time = time.strftime("%Y-%m-%d")
    requested_time = date_list[2] + "-" + date_list[0] + "-" + date_list[1]
    
    # 2015-05-03 < 2015-05-04   
    if requested_time < current_time:
        return "Invalid date. Reservation must be today, or in the future."

    # check if car is already reserved or if user already has a car reserved that day
    query = "SELECT COUNT(id) AS count FROM reservations WHERE (for_car=%s OR made_by=%s) AND for_date=%s AND car_returned <> 2"
    sql_date = date_list[2] + "-" + date_list[0] + "-" + date_list[1]
    result = db_conn.query_db(query, [car_id, user.db_id, sql_date], one=True)
    
    if result is None or result["count"] == 0:
        # can make reservation
        query = "INSERT INTO reservations (made_by, for_car, for_date) VALUES (%s, %s, %s)"
        args = [user.db_id, int(car_id), sql_date]
        result = db_conn.query_db(query, args, select=False)
        user.update_user(["credits"], [user.credits-50])
        
    else:
        return "You may not reserve this car today."

    return True


def claim_car(user_id, car_id):
    
    # Does not include the redundant check to see if this user
    # has this car checked out because we already get all of
    # the reservations for this user on this day in /dashboard
    
    # Indicates that the car has been checked out
    query = "UPDATE cars SET status=2 WHERE id=%s"
    result = db_conn.query_db(query, [car_id])
    
    print "Claim result: ", result
    
    return result


# Returns the car
def return_car(user_id, reservation_id, car_id):
    # Updates the cars checked in/out status and sets the return date
    query = "UPDATE reservations SET car_returned=2, return_time=%s WHERE (id=%s)"
    # Gets the date returned
    date_returned = datetime.datetime.now().date()
    result = db_conn.query_db(query, [str(date_returned), reservation_id])
    
    # Indicates that the car has been checked in
    query = "UPDATE cars SET status=1 WHERE id=%s"
    result = db_conn.query_db(query, [car_id])
    
    # If we were able to return the car
    if not result:
        num_credits = 50 # Hard coded, 50 credits per rental
        
        # Gets the date rented
        query = "SELECT for_date FROM reservations WHERE id=%s"
        date_rented = db_conn.query_db(query, [reservation_id])[0]['for_date']
        
        # Calculate how many days it has been since they rented the car
        num_days_difference = (date_returned - date_rented).days
        
        # If they returned the car more than 1 day late, penalize them
        # Else, give the user their 50 credits back
        if num_days_difference > 1:
            num_credits = -25 * (num_days_difference - 1)
        
        # Updates the user's credits
        query = "UPDATE users SET credits=credits+%s WHERE (id=%s)"
        result = db_conn.query_db(query, [num_credits, user_id])
    
    return result
    
    # Gets the car that the user reserved today
def get_reserved_car(user_id):
    query = "SELECT * FROM reservations WHERE (made_by=%s) AND (for_date<=%s) AND (car_returned=0)"
    current_date = time.strftime("%Y-%m-%d")
    result = db_conn.query_db(query, [user_id, current_date])
    
    return result

def create_review(review_data, u_id):
    query = "SELECT COUNT(id) AS count FROM reservations WHERE for_car=%s AND made_by=%s"
    result = db_conn.query_db(query, [review_data["car_id"], u_id], one=True)
    if result["count"] == 0:
        return "You cannot review a car you never drove!"
    
    query = "INSERT INTO reviews (date_created,num_stars, text, reviewer, car) VALUES " \
            "(%s, %s, %s, %s, %s)"
    result = db_conn.query_db(query,
                              [datetime.datetime.now(),
                                review_data["carRating"],
                                review_data["carReview"],
                                u_id, review_data["car_id"]],
                              select=False)
    return result

def get_reserved_dates(id):
    # Reserved dates are where the car is not returned (0) or returned
    # but not ready for rental (1)
    query = "SELECT for_date FROM reservations WHERE for_car=%s AND (car_returned <> 2)"
    result = db_conn.query_db(query, [id])
    dates = []
    for date in result:
        # starts as year-month-day
        # needs to be day-month-year
        date = str(date["for_date"]).split("-")
        temp = str(int(date[2]))
        date[2] = str(int(date[0]))
        date[0] = temp
        date[1] = str(int(date[1]))
        dates.append("-".join(date))
    return dates


def get_activity(user_id):
    query = "SELECT for_car, for_date FROM reservations WHERE made_by=%s AND car_returned=2 ORDER BY for_date DESC"
    rentals = db_conn.query_db(query, [user_id])
    
    query = "SELECT car, date_created FROM reviews WHERE reviewer=%s ORDER BY id DESC"
    reviews = db_conn.query_db(query, [user_id])
    
    # Manual Inner Join because the car rentals
    # use Dates and the reviews use Datetimes
    activity = []
    rental_i = 0
    reviews_i = 0
    for i in range(len(rentals) + len(reviews)):
                                                        
        # If the rental came first, append it
        if reviews_i == len(reviews) or (rental_i != len(rentals) and rentals[rental_i]['for_date'] < reviews[reviews_i]['date_created'].date()):
            
            activity.append({
                    'date':rentals[rental_i]['for_date'],
                    'car':rentals[rental_i]['for_car'],
                    'type':'Rented'})
            
            # Increment the rental index
            rental_i = rental_i + 1
            
        else:
            # Else, review came first, so add it
            activity.append({
                    'date':str(reviews[reviews_i]['date_created'].date()),
                    'car':reviews[reviews_i]['car'],
                    'type':'Reviewed'})
            
            # Increment the reviews index
            reviews_i = reviews_i + 1
    
    return activity


# Adds the user to the waiting list
def join_waitlist(user_id):
    
    # Check if the user is already on the waiting list
    query = "SELECT id FROM waiting_queue WHERE user=%s"
    result = db_conn.query_db(query, [user_id])
    
    # If the user is not on the waitlist, add them
    if not result:
        query = "INSERT INTO waiting_queue (`user`) VALUES (%s)"
        result = db_conn.query_db(query, [user_id])
        
        return True
    
    # Indicates that the user is already on the waitlist
    return False

# Checks if the user is on the waitlist
def check_waitlist(user_id):
    
    # Check if the user is already on the waiting list
    query = "SELECT id FROM waiting_queue WHERE user=%s"
    result = db_conn.query_db(query, [user_id])
    
    return len(result) > 0


def leave_waitlist(user_id):
    # Removes the user from the waiting list
    query = "DELETE FROM waiting_queue where user=%s"
    result = db_conn.query_db(query, [user_id])
    
    return result
    
def get_last_driver(car_id):
    query = "SELECT made_by FROM reservations WHERE for_car=%s AND for_date<CURRENT_DATE() " \
            "ORDER BY for_date DESC LIMIT 1"
    driver = db_conn.query_db(query, [car_id], one=True)

def log_work(car_id, description, worker):
    last_driver = get_last_driver(car_id)
    query = "UPDATE cars SET status=3 WHERE id=%s"
    result = db_conn.query_db(query, [car_id], select=False)
    if last_driver is None:
        last_driver = 1
    query = "INSERT INTO maintenance_log (car, description, last_driver, maintenance_worker) " \
            "VALUES (%s, %s, %s, %s)"
    result = db_conn.query_db(query, [car_id, description, last_driver, worker], select=False)
    return result

def update_car_status(car_id, car_status):
    query = "UPDATE cars SET status=%s WHERE id=%s"
    result = db_conn.query_db(query, [car_status, car_id], select=False)
    return result


def get_broken_cars():
    query = "SELECT cars.id AS id, cars.year AS year, cars.hp AS hp, cars.torque AS torque, cars.miles_driven AS miles, " \
        "cars.acceleration AS acceleration, cars.max_speed AS max_speed, make.description AS make, maintenance_log.description AS issue, " \
        "model.description AS model, cars.date_added AS date_added, cars.is_featured AS is_featured, " \
        "make.id AS make_id " \
        "FROM cars " \
        "JOIN make ON cars.make=make.id " \
        "JOIN model ON cars.model=model.id " \
        "JOIN maintenance_log ON cars.id=maintenance_log.car " \
        "WHERE cars.status=3"
    result = db_conn.query_db(query)
    return result