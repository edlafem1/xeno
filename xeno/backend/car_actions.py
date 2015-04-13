import database_connection as db_conn
import datetime

def get_cars(page, howmany):
    offset = 0
    if howmany > 0:
        offset = (page - 1) * howmany
    elif howmany == -1:
        offset = 0
     #car_data = db_conn.query_db('SELECT * FROM `xeno`.`cars` OFFSET %s LIMIT %s', [offset])