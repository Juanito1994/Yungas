#ARRANCA LA WEB! 

from flask import Flask, render_template, request, redirect, url_for, flash
from flask import jsonify
from flaskext.mysql import MySQL

app = Flask (__name__)
mysql = MySQL()

#MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'flaskcontacts'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/add_contact', methods=['POST'])
def add_contact():
    try:
        if request.method == 'POST':
            fullname = request.form['fullname']
            phone = request.form['phone']
            email = request.form['email']
            message = request.form['message']
            conn = mysql.connect()
            cur = conn.cursor()#pymysql.cursors.DictCursor
            query = "INSERT INTO `contacts` (`fullname`, `phone`, `email`, `message`) VALUES (%s, %s, %s, %s)"
            values = (fullname, phone, email, message)
            cur.execute(query, values)
            conn.commit()
            rows = cur.fetchall()
            resp = jsonify(rows)
            resp.status_code=200
            return redirect (url_for('index'))

    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/atracciones')
def atracciones():
    return render_template('atracciones.html')

@app.route('/fotos')
def fotos():
    return render_template('fotos.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/layout')
def layout():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run(port=3000, debug = True)
