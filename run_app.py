from flask import Flask, render_template, request
from flaskext.mysql import MySQL
#from flask_mysqldb import MySQL
import sys
import os

myapp = Flask(__name__)

myapp.config['MYSQL_HOST'] = 'localhost'
myapp.config['MYSQL_USER'] = 'root'
myapp.config['MYSQL_DB'] = 'myflask'
myapp.config['MYSQL_PASSWORD'] = ''

mysql = MySQL(myapp)

mysql.init_app(myapp)
#cursor = mysql.get_db().cursor()

@myapp.route('/', methods=['GET','POST'])
def georgerrmartin():
	if request.method == 'POST':
	    firstName = request.form['fname']
	    lastName = request.form['lname']
	    cur = mysql.connection.cursor()
	    cur.execute('''INSERT INTO names(firstname, lastname) VALUES (%s, %s)''', (firstName, lastName))
	    
	    #commit data to mysql
	    mysql.connection.commit()

	    #close mysql connection
	    cur.close()
	    return 'success'
	return render_template('form.html')
if __name__ == '__main__':
  myapp.debug = True
  host = os.environ.get('IP','0.0.0.0')
  port = int(os.environ.get('PORT','8081'))
  myapp.run(host=host, port=port)
