import database_connection as db_conn
import datetime
import user_class
import searching


def get_cars(page, howmany, get_new=False, get_featured=False, search_params=None):
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
    if search_params is not None:
        where_clause, args = searching.create_search_query(search_params)
        query += where_clause
        print("get_cars: " + where_clause)
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