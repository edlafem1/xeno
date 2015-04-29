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

FROM = "xenocars@gmail.com"
TO= ["veshbhatt@gmail.com"]

username = "xenocars@gmail.com"
password = "team1rocksX3N0"

def check_avail_cars(sc):

    print "Checking for available cars"

    query_check_available_cars = ("SELECT id FROM cars WHERE status = 1")
    cur.execute(query_check_available_cars)
    list_of_available_cars = cur.fetchall()

    for car in list_of_available_cars:
        query_check_car_reservation = ("SELECT id FROM reservations WHERE for_car = '%s' AND for_date = '%s'") % (str(car[0]), str(datetime.date.today()))
        cur.execute(query_check_car_reservation)
        reserved_car_list = cur.fetchall()

        if(reserved_car_list):
            print "Car: " + str(car[0]) + " is reserved today"
        else:
            TEXT =  "Car: " + str(car[0]) + " is available, reserve now!"
            print TEXT
            SUBJECT = TEXT
            message = "Subject: %s\n\n%s" % (SUBJECT, TEXT)
            server = smtplib.SMTP("smtp.gmail.com:587")
            server.starttls()
            server.login(username,password)
            server.sendmail(FROM, TO, message)
            server.quit()

    #run this function every 3600 seconds (60 minutes)
    sc.enter(3600, 1, check_avail_cars, (sc,))

s.enter(1, 1, check_avail_cars, (s,))
s.run()
