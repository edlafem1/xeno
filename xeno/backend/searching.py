# import database_connection as db_conn

def create_search_query(form_data):
    where_q = " WHERE "

    if len(form_data == 1):
        form_data["general"] = form_data["general"].trim()
        terms = form_data["general"].split()
        myear = 0
        for term in terms:
            try:
                if myear == 0:
                    myear = int(term)
            except ValueError:
                pass
