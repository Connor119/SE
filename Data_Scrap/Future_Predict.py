#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import time
import traceback
import pymysql
import pandas as pd
from datetime import datetime
import pickle


# In[2]:


predict_dbikes = pymysql.Connect(
    host = "dbikes.ccike2q3zkya.eu-west-1.rds.amazonaws.com",
    user = "admin",
    passwd = "admin2022",
    database = "dbikes")


# In[3]:


predict_cur = predict_dbikes.cursor()
predict_cur.execute("CREATE TABLE IF NOT EXISTS future_weather(number integer, bike_stands integer, dt integer, weekday integer, hour integer, lat float, lng float, weather varchar(45), temp float, pressure float, wind_speed float, humidity float, pd_abs float)")


# In[4]:


APIKEY = "a4ae2329e4585bbd13dcf83332d04b69a88fb904" 
NAME = "Dublin" 
STATIONS_URI = "https://api.jcdecaux.com/vls/v1/stations"

WEATHER_APIKEY = "eeec159d31a816c2152dbf05ba6e0076"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}"


# In[5]:


def InsertData2Tables(station):
    for i in range(0,len(station)):
        station_row = station[i]
        weather_response = requests.get(WEATHER_URL.format(station_row.get("position").get("lat"), station_row.get("position").get("lng"), WEATHER_APIKEY))
        weather = json.loads(weather_response.text)
#         import the pickle to make prediction
        RF = pickle.load(open('station_'+str(station_row.get("number"))+'.sav', 'rb'))
        for j in range(len(weather['hourly'])):
            future_insert_query = "INSERT INTO future_weather(number, bike_stands, dt, weekday, hour, lat, lng, weather, temp, pressure, wind_speed, humidity, pd_abs) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            pd_abs_x = pd.DataFrame({'bike_stands':[int(station_row.get("bike_stands"))],
                                     'weekday':[int(time.localtime(weather['hourly'][j]["dt"]).tm_wday)],
                                     'hour':[int(time.localtime(weather['hourly'][j]["dt"]).tm_hour)],
                                     'temp':[float(weather['hourly'][j]["temp"])],
                                     'pressure':[float(weather['hourly'][j]["pressure"])],
                                     'wind_speed':[float(weather['hourly'][j]["wind_speed"])],
                                     'humidity':[float(weather['hourly'][j]["humidity"])]})
            insert_data = ( int(station_row.get("number")),
                            int(station_row.get("bike_stands")),
                            int(weather['hourly'][j]["dt"]),
                            int(time.localtime(weather['hourly'][j]["dt"]).tm_wday),
                            int(time.localtime(weather['hourly'][j]["dt"]).tm_hour),
                            float(station_row.get("position").get("lat")),
                            float(station_row.get("position").get("lng")),
                            str(weather['hourly'][j]["weather"][0]["main"]),
                            float(weather['hourly'][j]["temp"]),
                            float(weather['hourly'][j]["pressure"]),
                            float(weather['hourly'][j]["wind_speed"]),
                            float(weather['hourly'][j]["humidity"]), 
                            float(RF.predict(pd_abs_x)))
            predict_cur.execute(future_insert_query, insert_data)
    predict_dbikes.commit()


# In[6]:


def drop_before_data():
    delete_query = "DELETE FROM future_weather"
    predict_cur.execute(delete_query)
    predict_dbikes.commit()


# In[7]:


def ContinuousUpDateData():
    while True:
        try:
            drop_before_data()
            api_response = requests.get(STATIONS_URI, params={"apiKey": APIKEY, "contract": NAME})
            data = json.loads(api_response.text)
            InsertData2Tables(data)
#             sleep every hour
            time.sleep(60*60)
    
        except:
#             hit for problems
            print(traceback.format_exc())


# In[ ]:


ContinuousUpDateData()

