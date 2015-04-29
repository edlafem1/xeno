import database_connection as db_conn

def create_search_query(form_data):

    myear = -1
    make = -1
    model = -1
    if len(form_data) == 1:
        terms = form_data["general"].split()
        for term in terms:
            try:
                if myear == -1:
                    myear = int(term)
            except ValueError:
                pass
            #  Check if term is a make or model
            if make == -1 or make is None:
                make = find_make(term)
                print "Searching for make: " + term + "=" + str(make)

            if model == -1 or model is None:
                model = find_model(term)
                print "Searching for model: " + term + "=" + str(model)
    else:
        try:
            myear = int(form_data["year"])
        except ValueError:
            pass
        make = find_make(form_data["make"])
        model = find_model(form_data["model"])
        print "aSearching for make: " + str(make)
        print "aSearching for model: " + str(model)

    return search_for_cars(myear, make, model)

def find_make(term):
    query = "SELECT id FROM make WHERE description " \
            "RLIKE '([A-Za-z0-9]{0,3} )*[A-Za-z0-9]{0,3}%s[A-Za-z0-9]{0,3}( [A-Za-z0-9]{0,3})*'" % (term,)
    #print query
    return db_conn.query_db(query, one=True)

def find_model(term):
    query = "SELECT id FROM model WHERE description " \
            "RLIKE '([A-Za-z0-9]{0,3} )*[A-Za-z0-9]{0,3}%s[A-Za-z0-9]{0,3}( [A-Za-z0-9]{0,3})*'" % (term,)
    return db_conn.query_db(query, one=True)

def search_for_cars(year, make_id, model_id):
    where_clause = "WHERE "
    args = []

    where_clause += "("
    where_1, arg1 = combo_maker(year, make_id, model_id)
    where_clause += where_1
    args += arg1

    where_clause += ")("

    where_1, arg1 = combo_maker(-1, make_id, model_id)
    where_clause += where_1
    args += arg1

    where_clause += ")("

    where_1, arg1 = combo_maker(year, make_id, None)
    where_clause += where_1
    args += arg1

    where_clause += ")("

    where_1, arg1 = combo_maker(year, None, model_id)
    where_clause += where_1
    args += arg1

    where_clause += ")("

    where_1, arg1 = combo_maker(-1, make_id, None)
    where_clause += where_1
    args += arg1

    where_clause += ")("

    where_1, arg1 = combo_maker(-1, None, model_id)
    where_clause += where_1
    args += arg1

    where_clause += ")"

    #where_clause = where_clause.rsplit(' ', 2)[0] + " "

    where_clause = where_clause.replace("()", " ")
    where_clause = where_clause.replace(")(", ") OR (")
    where_clause = where_clause.replace(") (", ") OR (")

    while where_clause[len(where_clause)-1] == " ":
        where_clause = where_clause[:-1]
    where_clause += " "

    if where_clause == "WHERE ":
        return "", []
    #print(where_clause)
    return where_clause, args

def combo_maker(year, make_id, model_id):
    where_clause = ""
    args = []

    if year != -1 and year >= 1800:
        where_clause += "ABS(cars.year - %s) < 3 AND " % (year,)
    if make_id != -1 and make_id is not None:
        where_clause += "cars.make=%s AND "
        args.append(make_id["id"])
    if model_id != -1 and model_id is not None:
        where_clause += "cars.model=%s AND "
        args.append(model_id["id"])

    where_clause = where_clause.rsplit(' ', 2)[0]
    return where_clause, args
