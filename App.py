from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '-'
app.config['MYSQL_DB'] = 'contacts'

mysql = MySQL(app)


#Routes
@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/add_contact')
def add_contact():
    return 'add contact'

@app.route('/delete')
def delete_contact():
    return 'delete contact'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)