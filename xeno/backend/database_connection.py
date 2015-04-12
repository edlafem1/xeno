from flask import g
import mysql.connector as mariadb
import configuration
from backbone import app


def connect_db():
    '''Connects to the specific database.'''
    con = mariadb.connect(**configuration.database)
    return con


def get_db():
    '''Opens a new database connection if there is none yet for the
    current application context.
    '''
    if not hasattr(g, 'mariadb'):
        g.mariadb = connect_db()
    return g.mariadb


@app.teardown_appcontext
def close_db(error):
    '''Closes the database again at the end of the request.'''
    if hasattr(g, 'mariadb'):
        g.mariadb.close()


def query_db(query, args=(), one=False):
    '''Use this for all database querying. See example below for how to use.
    To pass variable parts to the SQL statement, use C string formatting(like %s %d) in the statement and pass in the arguments as a
    list. Never directly add them to the SQL statement with string formatting.

    user = query_db('select * from users where username = %s',
                [the_username], one=True)
    if user is None:
        print 'No such user'
    else:
        print the_username, 'has the id', user['user_id']

    This example shows how to call the function with parameters in the query itself and only get one result.
    The example below shows a more general example:

    result = query_db('select * from users')
    for user in result:
        print user['username'], 'has the id', user['user_id']
    '''
    cursor = get_db().cursor(dictionary=True)
    cursor.execute(query, args)
    rv = cursor.fetchall()
    cursor.close()
    return (rv[0] if rv else None) if one else rv