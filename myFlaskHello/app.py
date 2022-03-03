from flask import Flask, jsonify
from flask import request
from flask import render_template
import pymysql.cursors
app = Flask(__name__)


def getConnector():
    connection = pymysql.connect(host='dbikes.ccike2q3zkya.eu-west-1.rds.amazonaws.com',
                                 user='admin',
                                 password='admin2022',
                                 db='dbikes',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

# cursor = getConnector().cursor()
# sql = "select * from static_station"
# cursor.execute(sql)
# result = cursor.fetchall()
# for data in result:
#     print(data)
# cursor.close()

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
@app.route('/temp')
def hello_world3():
    return render_template("index.html")

@app.route('/login')
def hello_world2():
    name = request.values.get("name")
    return f'name={name}'

@app.route('/hello')
def hello_world1():
    id = request.values.get("id")
    return f"""<form action="/login">
                账号：<input name="name" value="{id}">
                <input type="submit">
                </form>
    """


@app.route('/ajax')
def hello_world4():
    name = request.values.get("name")
    return name

@app.route('/station')
def getStation():
    conn = getConnector();
    cursor = conn.cursor()
    sql = "select * from static_station"
    cursor.execute(sql)
    rows= cursor.fetchall()
    return jsonify(stations=[dict(row.items()) for row in rows])

if __name__ == '__main__':
    app.run()





