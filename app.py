from flask import Flask, jsonify
from flask import request
from flask import render_template
import pymysql.cursors
import utils
app = Flask(__name__)


def getConnector():
    connection = pymysql.connect(host='dbikes.ccike2q3zkya.eu-west-1.rds.amazonaws.com',
                                 user='admin',
                                 password='admin2022',
                                 db='dbikes',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


@app.route('/')
def indexPage():
    return render_template("indexTest.html")

@app.route('/Register')
def Register():
    return render_template("Register.html")

@app.route('/index')
def toHome():
    return render_template("indexTest.html")

@app.route('/time')
def getTime():
    return utils.get_time()



@app.route('/stationTest')
def getStation():
    conn = getConnector();
    cursor = conn.cursor()
    sql = "SELECT s1.number,s1.name,s1.bike_stands,s1.available_bike_stands,s1.available_bikes,s2.lat,s2.lng FROM show_front_end s1 inner join static_station s2 on s1.number=s2.number;"
    cursor.execute(sql)
    rows= cursor.fetchall()
    return jsonify(stations=[dict(row.items()) for row in rows])
    # return jsonify(stations=[dict(rows[1].items())])

@app.route('/allInfo')
def getInfo():
    conn = getConnector();
    cursor = conn.cursor()
    sql = "select * from show_front_end"
    cursor.execute(sql)
    rows= cursor.fetchall()
    return jsonify(stations=[dict(row.items()) for row in rows])


@app.route('/predicted')
def whether():
    conn = getConnector();
    cursor = conn.cursor()
    sql = "select * from dynamic_station"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return jsonify(predicted=[dict(row.items()) for row in rows])

# 改
@app.route('/test')
def test():
    conn = getConnector();
    cursor = conn.cursor()
    sql = "select * from future_weather f ORDER BY f.dt DESC limit 110"
    cursor.execute(sql)
    rows= cursor.fetchall()
    return jsonify(stations=[dict(row.items()) for row in rows])

@app.route('/pri2')
def pridict2():
    conn = getConnector();
    cursor = conn.cursor()
    sql = "select * from future_weather f ORDER BY f.dt DESC limit 110,110"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return jsonify(stations=[dict(row.items()) for row in rows])


@app.route('/pri3')
def pridict3():
    conn = getConnector();
    cursor = conn.cursor()
    sql = "select * from future_weather f ORDER BY f.dt DESC limit 220,110"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return jsonify(stations=[dict(row.items()) for row in rows])

@app.route('/pri4')
def pridict4():
    conn = getConnector();
    cursor = conn.cursor()
    sql = "select * from future_weather f ORDER BY f.dt DESC limit 330,110"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return jsonify(stations=[dict(row.items()) for row in rows])

@app.route('/pri5')
def pridict5():
    conn = getConnector();
    cursor = conn.cursor()
    sql = "select * from future_weather f ORDER BY f.dt DESC limit 0,550"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return jsonify(stations=[dict(row.items()) for row in rows])
# 改

if __name__ == '__main__':
    app.run()


