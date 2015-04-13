import database_connection as db_conn
import datetime

def get_cars(page, howmany):
    print "getting cars!"
    offset = 0
    query = "SELECT * FROM `xeno`.`cars` ORDER BY `make' ASC"
    if howmany > 0:
        offset = (page - 1) * howmany
        query += " LIMIT " + str(offset) + ", " + str(howmany)  # LIMIT offset,row_count
    elif howmany == -1:
        offset = 0
    car_data = db_conn.query_db(query)
    print car_data
    return car_data