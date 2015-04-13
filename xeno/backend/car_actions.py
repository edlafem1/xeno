import database_connection as db_conn
import datetime

def get_cars(page, howmany):
    print "getting cars!"
    offset = 0
    query = "SELECT cars.id AS id, cars.year AS year, cars.hp AS hp, cars.torque AS torque, cars.miles_driven AS odo, " \
        "cars.acceleration AS acceleration, cars.max_speed AS max_speed, make.description AS make, " \
        "model.description AS model " \
        "FROM cars " \
        "JOIN make ON cars.make=make.id " \
        "JOIN model ON cars.model=model.id " \
        "ORDER BY make.id ASC"
#    query = "SELECT * FROM `xeno`.`cars` ORDER BY `make` ASC"
    if howmany > 0:
        offset = (page - 1) * howmany
        query += " LIMIT " + str(offset) + ", " + str(howmany)  # LIMIT offset,row_count
    elif howmany == -1:
        offset = 0
    car_data = db_conn.query_db(query)
    #print car_data
    return car_data

def add_new_car(cdata):
    '''
    make, model, year, country, hp(int), torque(int), acceleration(int), max_speed(int)
    '''
    query = "SELECT id FROM make WHERE description=%s"
    make_id = db_conn.query_db(query, [cdata["make"].lower()], one=True)
    if make_id is None:
        query = "INSERT INTO make (`description`) VALUES (%s)"
        make_id = db_conn.query_db(query, [cdata["make"]], select=False)
        print "Make id" + str(make_id)
    else:
        make_id = int(make_id["id"])
        print "Make id already there as " + str(make_id)

    query = "SELECT id FROM model WHERE description=%s"
    model_id = db_conn.query_db(query, [cdata["model"].lower()], one=True)
    if model_id is None:
        query = "INSERT INTO model (`description`) VALUES (%s)"
        model_id = db_conn.query_db(query, [cdata["model"]], select=False)
        print "Model id" + str(model_id)
    else:
        model_id = int(model_id["id"])
        print "Model id already there as " + str(model_id)

    query = "SELECT id FROM country WHERE description=%s"
    country_id = db_conn.query_db(query, [cdata["country"].lower()], one=True)
    if country_id is None:
        query = "INSERT INTO country (`description`) VALUES (%s)"
        country_id = db_conn.query_db(query, [cdata["country"]], select=False)
        print "Country id" + str(country_id)
    else:
        country_id = int(country_id["id"])
        print "Country id already there as " + str(country_id)

    print "ugh"
    query = "INSERT INTO cars (make, model, year, country, hp, torque, miles_driven, added_by, acceleration, max_speed)" \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    result = db_conn.query_db(query, [make_id, model_id, int(cdata["year"]), country_id, int(cdata["hp"]),
                                      int(cdata["torque"]), int(cdata["odo"]), 1, int(cdata["acceleration"]),
                                      int(cdata["max_speed"])], select=False)
    print result
    print "added"

    return True