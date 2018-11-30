from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'jay'
app.config['MYSQL_DATABASE_PASSWORD'] = 'jay'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/home')
def home():
    return "<h2>This site is a flask pyhon database system to compare ones own Brygs-Myers Personality type to someone elses</h2>"

@app.route('/about')
def about():
    return "<h2>A collaborative project to test your personality against other students and see how compatible you are according to the Brygs-Myers test</h2>"


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:
            
            # All Good, let's call MySQL
            
            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = generate_password_hash(_password)
            cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'User created successfully !'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close() 
        conn.close()


##Login()	
##	username = prompt user for username
##	password = prompt user for password
##if (query user table for match and if found) 
##logged_in = true
##	else 
##		display login error message
##
##Create_User()	
##	username = prompt user for username
##	password = prompt user for password
##	if(username !exist in username section of user table)
##		Insert new username into the user table along with the password
##
##Delete_User()
##	//A way to delete one's own account
##	if(prompt for confirmation is confirmed)
##		Remove user from user table
##		Cascades changes throughout the other tables
##
##Take_Quiz()	
##// Will display the questions in a linear order and start adding answer scores
##	Loop through Questions
##		display question
##		display answers of joining current Qnum in Questions == Qnum in Answers table
##		add weights of user chosen answer to the weights in personality
##	calculate personality_full_name in personality based on weights
##	add personality_full_name to previous_scores
##
##Show_Personality_Score()	
##	p = retrieve personality_full_name from Personality matching to the current username
##	display the list of all celebrities with a matching personality
##	display a list of all the fictional characters with matching personality types
##
##Compare_Score() 
##	name = prompt user for name
##	if(name exists in User)
##		display username next to their personality_full_name from the Personality table


if __name__ == '__main__':
    app.run
