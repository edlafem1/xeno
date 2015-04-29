import database_connection as db_conn
import datetime
import user_class


def get_cars(page, howmany, get_new=False, get_featured=False):
    #print "getting cars!"
    offset = 0
    query = "SELECT cars.id AS id, cars.year AS year, cars.hp AS hp, cars.torque AS torque, cars.miles_driven AS odo, " \
        "cars.acceleration AS acceleration, cars.max_speed AS max_speed, make.description AS make, " \
        "model.description AS model, cars.date_added AS date_added, cars.is_featured AS is_featured, " \
        "make.id AS make_id " \
        "FROM cars " \
        "JOIN make ON cars.make=make.id " \
        "JOIN model ON cars.model=model.id "
    if get_new is False and get_featured is False:
        query += "ORDER BY make.id DESC, date_added DESC "
    elif get_new is True and get_featured is False:
        query += "ORDER BY date_added DESC "
        howmany = 8
        offset = 0
        page = 1
    elif get_featured is True:
        # query += "WHERE cars.is_featured=1 "
        # to force there to be some car that is featured(even if none is marked), do not use WHERE, use ORDER BY
        query += "ORDER BY is_featured DESC, date_added DESC "
        howmany = 4
        offset = 0
        page = 1

#    query = "SELECT * FROM `xeno`.`cars` ORDER BY `make` ASC"
    if howmany > 0:
        offset = (page - 1) * howmany
        query += "LIMIT " + str(offset) + ", " + str(howmany)  # LIMIT offset,row_count
    elif howmany == -1:
        offset = 0
    car_data = db_conn.query_db(query)
#    print car_data
    return car_data


def add_new_car(cdata, current_user):
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