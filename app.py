from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

# CONNECTING OUT DATABASE

def connect_db():
    sql = sqlite3.connect('/mnt/c/Users/antho/Documents/data.db')
    sql.row_factory = sqlite3.Row # Results will be returned as Dictionary's instead of Tuples
    return sql

def get_db():
    if not hasattr(g, 'sqlite_db'): # Global object will check if SQLiteDB exists in there
        g.sqlite_db = connect_db() # If it doesnt, it will add it & connect to DB using it and return results of the connection
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'): #Close at the end of request/route
        g.sqlite_db.close()


# ROUTES FOR OUR FOOD TRACKING APP
# Home Route
@app.route('/')
def index():
	return render_template('home.html')

@app.route('/view')
def view():
	return render_template('day.html')


@app.route('/food')
def food():
	return render_template('add_food.html')



if __name__ == '__main__':
	app.run(debug=True)