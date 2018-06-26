from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'codeberlin'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        first_name = userDetails['first-name']
        last_name = userDetails['last-name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO userdata(firstname, lastname, email) VALUES(%s, %s, %s)",(first_name, last_name, email))
        mysql.connection.commit()
        cur.close()
        return redirect('/userdata')
    return render_template('main.html')

@app.route('/userdata')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM userdata")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)
