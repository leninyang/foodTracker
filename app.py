from flask import Flask, render_template, g, request
import sqlite3

app = Flask(__name__)

# CONNECTING OUT DATABASE

def connect_db():
    sql = sqlite3.connect('food_log.db')
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
    db = get_db()
# =====================================
    # INSERTING DATES INTO DB
# =====================================
    if request.method == 'POST':
        date = request.form['date'] #assuming the date is in YYYY-MM-DD format

        # Now that we have the date we're going to:
        # Create it into a datetime object | We parse the string(pass in the date, format)
        dt = datetime.strptime(date, '%Y-%m-%d')
        # Creating the database string w/ new format
        database_date = datetime.strftime(dt, '%Y%m%d')

        db.execute('insert into log_date (entry_date) values (?)', [database_date])
        db.commit()

    # Query to retrieve dates
    cur = db.execute('insert into log_date (entry_date) values (?)' [database])
    db.commit()

    return render_template('home.html')

@app.route('/view')
def view():
	return render_template('day.html')


@app.route('/food', methods=['GET', 'POST'])
def food():
    db = get_db()
# =====================================
	# INSERTING FOOD INTO OUR DB
# =====================================
    # Creating the variables for each input value
    if request.method == 'POST':
        name = request.form['food-name']
        protein = int(request.form['protein'])
        carbohydrates = int(request.form['carbohydrates'])
        fat = int(request.form['fat'])
        
        # Calculates calories from the input values
        calories = protein * 4 + carbohydrates * 4 + fat * 9

        # Add values | Insert into food table | List of values
        db.execute('insert into food (name, protein, carbohydrates, fat, calories) values (?, ?, ?, ?, ?)', \
            [name, protein, carbohydrates, fat, calories])
        db.commit()

    cur = db.execute('select name, protein, carbohydrates, fat, calories from food')
    results = cur.fetchall()

    return render_template('add_food.html', results=results)



if __name__ == '__main__':
	app.run(debug=True)