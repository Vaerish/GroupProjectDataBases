from flask import Flask, render_template, json, request, redirect, url_for
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

USERNAME = ''
MOST_COMPATIBLE = ['','','', '']
CURR_PERSONALITY = 'Complete the test'
PERSONALITY_DESC = None
COMPAT = ''
PREVIOUS_SCORES = [' ',' ',' ']
PERCENTAGE = 0

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


@app.route('/signIn',methods=['POST','GET'])
def Authenticate():
		global USERNAME
		global CURR_PERSONALITY
		global MOST_COMPATIBLE
		username = request.form['inputName']
		password = request.form['inputPassword']
		USERNAME = username
		try:
				if username and password:
						cursor = mysql.connect().cursor()
						cursor.execute('''SELECT * FROM Account WHERE username=%s''',(username))
						result = cursor.fetchall()
						if not len(result) == 0:
								if result[0][1] == password:
										try:
												user = USERNAME
												cursor.execute('''SELECT previous_scores FROM Account2 WHERE username = %s ORDER BY Attempt DESC LIMIT 1;''',(user))
												result = cursor.fetchall()
												print (result[0][0], 'stuff', user, '0')
												CURR_PERSONALITY = result[0][0]
												cursor.execute('''SELECT username FROM Account2 WHERE previous_scores = %s and username != %s ORDER BY Attempt DESC LIMIT 1;''',(CURR_PERSONALITY, user))
												result = cursor.fetchall()
												MOST_COMPATIBLE[0] = result[0][0]
												cursor.execute('''SELECT name,occupation FROM Famous_Figure WHERE personality_type = %s;''',(CURR_PERSONALITY))
												result = cursor.fetchall()
												MOST_COMPATIBLE[1] = result[0][0]
												MOST_COMPATIBLE[2] = result[0][1]
										except Exception as e:
												MOST_COMPATIBLE = None
												CURR_PERSONALITY = "Complete The Test!"
										print(MOST_COMPATIBLE)
										return ("SUCCCESSSFUL")
								else:
										raise LookupError
						else:
								raise
				else:
						raise
		except Exception as e:
				return e

##Login()	   
##	  username = prompt user for username
##	  password = prompt user for password
##if (query user table for match and if found) 
##logged_in = true
##	  else 
##			  display login error message
##
@app.route('/errorTest')
def errorTest():
				return render_template('errorTest.html')

@app.route('/testFinished')
def testFinished():
		return render_template('testFinished.html')
@app.route('/test')
def test():

		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute('''SELECT Question.question_number, question_text, answer_number, answer_text, E_I_weight, N_O_weight, T_F_weight, J_P_weight
FROM Question, Answer
WHERE Question.question_number = Answer.question_number;''')
		result = cursor.fetchall()
		var = "R"
		holder = []
		lst = []
		for r in result:
						if (var != r[1]):
										var = r[1]
										holder.append(r[1])
										holder.append(r[3])
										holder.append([r[4],r[5],r[6],r[7]])
						else:
										holder.append(r[3])
										holder.append([r[4],r[5],r[6],r[7]])
										lst.append(holder)
										holder = []

				
		return render_template('test.html',test = lst)

@app.route('/testResult',methods=['POST','GET'])
def testResult():
		_questionOne = request.form['1']
		_questionTwo = request.form['2']
		_questionThree = request.form['3']
		_questionFour = request.form['4']

		if _questionOne and _questionTwo and _questionThree and _questionFour and (request.method == 'POST'):
				try:
						if (_questionOne == '1'):
								inputs = 'E'
						else:
								inputs = 'I'
						if (_questionTwo == '1'):
								inputs += 'N'
						else:
								inputs += 'O'
						if (_questionThree == '1'):
								inputs += 'T'
						else:
								inputs += 'F'
						if (_questionFour == '1'):
								inputs += 'J'
						else:
								inputs += 'P'
						conn = mysql.connect()
						cursor = conn.cursor()
						cursor.execute('''INSERT INTO Account2 (username, previous_scores)
VALUES (%s, %s)''',(USERNAME, inputs))
						conn.commit()
						return "Success"
				except Exception as e:
						return e
		else:
				return "error"
		return "Success"
				
@app.route('/signUp',methods=['POST','GET'])
def signUp():
		_name = request.form['inputName']
		_password = request.form['inputPassword']

		if _name and _password and (request.method == 'POST'):
				try:
						conn = mysql.connect()
						cursor = conn.cursor()
						cursor.execute('''INSERT INTO Account(username,user_password) VALUES(%s,%s)''',(_name,_password))
						conn.commit()
				except Exception as e:
						return e
		else:
				return "error"
		return "Success"

@app.route('/success')
def success():
		return render_template('success.html')

@app.route('/errorSignUp')
def errorSignUp():
		return render_template('errorSignUp.html')

@app.route('/errorSignIn')
def errorSignIn():
		return render_template('errorSignIn.html')

@app.route('/compare')
def compare():
		return render_template('compare.html')

@app.route('/compareError')
def compareError():
		return render_template('compareError.html')

@app.route('/compareFinished')
def compareFinished():
		print (COMPAT)
		return render_template('compareFinished.html',compat = COMPAT)

@app.route('/testCompare',methods=['POST','GET'])
def testCompare():
		global COMPAT
		_name = request.form['inputName']
		if _name and USERNAME != '' and (request.method == 'POST'):
				try:
						conn = mysql.connect()
						cursor = conn.cursor()
						cursor.execute('''SELECT previous_scores FROM Account2 WHERE username = %s ORDER BY Attempt DESC LIMIT 1;''',(USERNAME))
						resultPerson = cursor.fetchall()
						cursor.execute('''SELECT previous_scores FROM Account2 WHERE username = %s ORDER BY Attempt DESC LIMIT 1;''',(_name))
						resultOtherPerson = cursor.fetchall()
						conn.commit()
						if (resultPerson[0] == resultOtherPerson[0]):
								COMPAT = "You are compatible"
						else:
								COMPAT = "You are not compatible"
				except Exception as e:
						return e
		else:
				return "error"
		print (COMPAT)
		return "Success"



@app.route('/dashboard')
def dashboard():
		global PERSONALITY_DESC
		global PREVIOUS_SCORES
		if MOST_COMPATIBLE and USERNAME != '':
				cursor = mysql.connect().cursor()
				cursor.execute('''SELECT short_description FROM Personality WHERE personality_full_name = %s;''',(CURR_PERSONALITY))
				result = cursor.fetchall()
				PERSONALITY_DESC = result[0][0]

				#Percentage Code
				cursor.execute('''SELECT COUNT(previous_scores) FROM Account2;''')
				result = cursor.fetchall()

				cursor.execute('''SELECT COUNT(username) FROM Account2 WHERE previous_scores = %s;''',(CURR_PERSONALITY))
				result2 = cursor.fetchall()
				PERCENTAGE = round((int(result2[0][0]) * 1.0)/int(result[0][0])*100, 2)
				#-----------------------

				#Previous Scores
				cursor.execute('''SELECT previous_scores FROM Account2 WHERE username = %s;''',(USERNAME))
				result = cursor.fetchall()
				if len(result) > 3:
					result = result[:3]
				for i in range(0,len(result)):
					PREVIOUS_SCORES[i] = result[i][0]
				#------------------------

				return render_template('dashboard.html',user = USERNAME, personality = CURR_PERSONALITY, most_compatible= MOST_COMPATIBLE, personailty_desc = PERSONALITY_DESC, percentage = PERCENTAGE,scores=PREVIOUS_SCORES)
		elif USERNAME != '':
				PERSONALITY_DESC = 'It seems you have not taken the Personality Quiz yet. To begin the quiz hit the button that says "Take Personality Test". After completing the test you will be able to see interesting information concerning you personality type!'
				return render_template('dashboard.html',user = USERNAME, personality = CURR_PERSONALITY, most_compatible= MOST_COMPATIBLE, personailty_desc = PERSONALITY_DESC,percentage = PERCENTAGE,scores=PREVIOUS_SCORES)
		else:
				return render_template('signin.html')



#Unused when running with 'flask run', to turn debug on must use 'set FLASK_DEBUG=1' in terminal every time
#When using 'python app.py' to run script it will set debug to True, using the following lines
#Must be kept underneath all @app.route declerations or it will inpede them running
if __name__ == '__main__':
		app.run(debug=True)
