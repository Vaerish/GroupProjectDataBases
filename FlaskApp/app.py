from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
#from flask_mysqldb import MySQL
from werkzeug import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'sql9268523'
app.config['MYSQL_DATABASE_PASSWORD'] = 'K73sXeXVF2'
app.config['MYSQL_DATABASE_DB'] = 'sql9268523'
app.config['MYSQL_DATABASE_HOST'] = 'sql9.freemysqlhosting.net'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/showSignIn')
def showSignIn():
    return render_template('signin.html')


#Works but only through typing 'http://127.0.0.1:5000/Authenticate?UserName=Admin&Password=admin'
#Also only works with EmpData database
@app.route("/Authenticate")
def Authenticate():
    username = request.form['inputName']
    password = request.form['inputPassword']
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from Account where username='" + username + "' and user_password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"

##Login()	
##	username = prompt user for username
##	password = prompt user for password
##if (query user table for match and if found) 
##logged_in = true
##	else 
##		display login error message
##

@app.route('/signUp',methods=['POST','GET'])
def signUp():
	_name = request.form['inputName']
	_password = request.form['inputPassword']

	if _name and _password:
		try:
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute('''INSERT INTO Account(username,user_password) VALUES(%s,%s)''',(_name,_password))
			conn.commit()
		except Exception as e:
			return ('INSERTING ERROR:  ' + str(e))
	else:
		return "Invalid Entry State"
	return "Completed"

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



#Unused when running with 'flask run', to turn debug on must use 'set FLASK_DEBUG=1' in terminal every time
#When using 'python app.py' to run script it will set debug to True, using the following lines
#Must be kept underneath all @app.route declerations or it will inpede them running
if __name__ == '__main__':
    app.run(debug=True)

