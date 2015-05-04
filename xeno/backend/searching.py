"""
This file provides utility functions for generating parts of queries related to searching for cars.
"""

import database_connection as db_conn


def create_search_query(form_data):
    """
    This is the function that should be called to generate conditions for a WHERE clause to search on multiple fields.
    :param form_data: A dictionary of values. The dictionary can either have only one element with key "general"
            that represents a simple search; or it can have 3 values with keys "make", "model", "year" and at least 1 of
            which's value is not None and not -1.
    :return: If WHERE clause conditions can be generated, it will have the form AND (...) OR (...) etc, followed by a single
    space. The value returned will be a tuple with this clause and a list of values to be used as arguments in
    the SQL query.
    If no WHERE clause conditions can be generated, it will return the tuple ("", []) which can be used in other places.
    For example:
        clause, arguments = create_search_query(some_data)
        query += clause
        query_args += arguments
    It will not change anything if this function returns the tuple ("", []) as query and query_args will be
    un-changed.
    """
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
                # print "Searching for make: " + term + "=" + str(make)

            if model == -1 or model is None:
                model = find_model(term)
                # print "Searching for model: " + term + "=" + str(model)
    else:
        try:
            myear = int(form_data["year"])
        except ValueError:
            pass
        make = find_make(form_data["make"])
        model = find_model(form_data["model"])
        # print "Searching for make: " + str(make)
        # print "Searching for model: " + str(model)

    return search_for_cars(myear, make, model)


def find_make(term):
    """
    Attempts to determine if this term is a make in the database.
    :param term: A word that may or may not be the make of the car
    :return: The id of the row in the database representing this make,
    None if no make with description==term can be found.
    """
    query = "SELECT id FROM make WHERE description " \
            "RLIKE '([A-Za-z0-9]{0,3} )*[A-Za-z0-9]{0,3}%s[A-Za-z0-9]{0,3}( [A-Za-z0-9]{0,3})*'" % (term,)
    #print query
    return db_conn.query_db(query, one=True)


def find_model(term):
    """
    Attempts to determine if this term is a model in the database.
    :param term: A word that may or may not be the model of the car
    :return: The id of the row in the database representing this model,
    None if no model with description==term can be found.
    """
    query = "SELECT id FROM model WHERE description " \
            "RLIKE '([A-Za-z0-9]{0,3} )*[A-Za-z0-9]{0,3}%s[A-Za-z0-9]{0,3}( [A-Za-z0-9]{0,3})*'" % (term,)
    return db_conn.query_db(query, one=True)


def search_for_cars(year, make_id, model_id):
    """
    Generates a powerset of conditions to match a car upon.
    :param year: A year or None that this car could be
    :param make_id: The id of this car's make, or None if no entry was found
    :param model_id: The id of this car's model, or None if no entry was found
    :return: A string of the form described in the create_search_query documentation.
    """
    where_clause = "AND "
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

    where_clause = where_clause.replace("()", " ")
    where_clause = where_clause.replace(")(", ") OR (")
    where_clause = where_clause.replace(") (", ") OR (")

    while where_clause[len(where_clause)-1] == " ":
        where_clause = where_clause[:-1]
    where_clause += " "

    if where_clause == "AND ":
        return "", []
    return where_clause, args


def combo_maker(year, make_id, model_id):
    """
    Creates a single conditional depending on the values supplied
    :param year: A year or None that this car could be
    :param make_id: The id of this car's make, or None if no entry was found
    :param model_id: The id of this car's model, or None if no entry was found
    :return: A string representing a SQL conditional. It will NOT be wrapped in parenthesis and will have no additional
    space on the end.
    """
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
