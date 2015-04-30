"""
This file manages the queue and assignment of free cars. Once a car is avaiable and not booked in the next day, a user will be notified of its status.
"""

#import database_connection as db_conn
#import configuration
import sched, time, datetime
import mysql.connector as mariadb
import smtplib

s = sched.scheduler(time.time, time.sleep)

database = {
    "user": "root",
    "password": "password",
    "host": "localhost",
    "database": "xeno"
}

con = mariadb.connect(**database)
cur = con.cursor()

con = mariadb.connect(**database)
cur = con.cursor()

FROM = "xenocars@gmail.com"
TO= ["xenocars@gmail.com"]

username = "xenocars@gmail.com"
password = "team1rocksX3N0"

def check_avail_cars(sc):

    print "Checking for available cars"

    #Get list of cars where status is available for checkout (this is just for safety)
    query_check_available_cars = ("SELECT id FROM cars WHERE status = 1")
    cur.execute(query_check_available_cars)
    list_of_available_cars = cur.fetchall()

    TEXT = ""

    for car in list_of_available_cars:
<<<<<<< HEAD
<<<<<<< HEAD
        query_check_car_reservation = ("SELECT id FROM reservations WHERE for_car = '%s' AND for_date = '%s'") % (str(car[0]), str(datetime.date.today()))
        cur.execute(query_check_car_reservation)
        reserved_car_list = cur.fetchall()

        query_get_car_name = ("SELECT make, model FROM cars WHERE id = '%s'") % (str(car[0]))
        cur.execute(query_get_car_name)
        car_make_and_model = cur.fetchall()
        car_make_id = car_make_and_model[0][0]
        query_get_car_make = ("SELECT description FROM make WHERE id = '%s'") % (str(car_make_id))
        cur.execute(query_get_car_make)
        car_make = cur.fetchone()[0]
        car_model_id = car_make_and_model[0][1]
        query_get_car_model = ("SELECT description FROM model WHERE id = '%s'") % (str(car_model_id))
        cur.execute(query_get_car_model)
        car_model = cur.fetchone()[0]

        if(reserved_car_list):
            print "Car " + str(car_make) + " " + str(car_model) + " is reserved today."
        else:
            TEXT =  TEXT + "Car: " + str(car_make) + " " + str(car_model) + " is available, reserve now!\n"
=======
=======
>>>>>>> vb-edits
	#Get the human readable info for cars (make, model)
	query_get_car_name = ("SELECT make, model FROM cars WHERE id = '%s'") % (str(car[0]))
	cur.execute(query_get_car_name)
	car_make_and_model = cur.fetchall()
	car_make_id = car_make_and_model[0][0]
	query_get_car_make = ("SELECT description FROM make WHERE id = '%s'") % (str(car_make_id))
	cur.execute(query_get_car_make)
	car_make = cur.fetchone()[0]
	car_model_id = car_make_and_model[0][1]
	query_get_car_model = ("SELECT description FROM model WHERE id = '%s'") % (str(car_model_id))
	cur.execute(query_get_car_model)
	car_model = cur.fetchone()[0]

	#Get list of cars that aren't checked out/reserved today
	query_check_car_reservation = ("SELECT id FROM reservations WHERE for_car = '%s' AND for_date = '%s'") % (str(car[0]), str(datetime.date.today()))
	cur.execute(query_check_car_reservation)
	reserved_car_list = cur.fetchall()

	if(reserved_car_list):
	    print str(car_make) + " " + str(car_model) + " is reserved today."
	else:
	    TEXT =  TEXT + str(car_make) + " " + str(car_model) + " is available, reserve now!\n"
<<<<<<< HEAD
>>>>>>> vb-edits
=======
>>>>>>> vb-edits

    TEXT = TEXT + "http://xenocars.me"
    print TEXT
    SUBJECT = TEXT
    message = "Subject: %s\n\n%s" % (SUBJECT, TEXT)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(username,password)
<<<<<<< HEAD
<<<<<<< HEAD
    server.sendmail(FROM, TO, message)
    server.quit()
=======
=======
>>>>>>> vb-edits

    #Get top # of user_id's in waiting_queue (where # = # of cars available)
    query_get_user_email = ("SELECT user FROM waiting_queue LIMIT %s") % (str(len(reserved_car_list)))
    cur.execute(query_get_user_email)
    top_users_in_queue = cur.fetchall()

    #send each user an email
    for user in top_users_in_queue:
	query_get_user_email = ("SELECT userid FROM users WHERE id = '%s'") % (str(user[0]))
	cur.execute(query_get_user_email)
	user_email = cur.fetchone()[0]
	server.sendmail(FROM, [user_email], message)
	server.quit()

	#remove user from queue
	query_remove_user_from_queue = ("DELETE FROM waiting_queue WHERE user = '%s'") % (str(user[0]))
	cur.execute(query_remove_user_from_queue)
<<<<<<< HEAD
>>>>>>> vb-edits
=======
>>>>>>> vb-edits

    #run this function every 3600 seconds (60 minutes)
    sc.enter(3600, 1, check_avail_cars, (sc,))

s.enter(1, 1, check_avail_cars, (s,))
s.run()