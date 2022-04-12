#!/usr/bin/env python
# coding: utf-8

# In[13]:


import requests
import json
import time
import traceback
import pymysql
import pandas as pd
from datetime import datetime
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle


# In[14]:


# connect to the database
dbikes = pymysql.Connect(
    host = "dbikes.ccike2q3zkya.eu-west-1.rds.amazonaws.com",
    user = "admin",
    passwd = "admin2022",
    database = "dbikes")


# In[15]:


def getinitialdf():
    # read database and assign each table to dataframe structure
    static_station = pd.read_sql_query("SELECT * FROM static_station", dbikes)
    dynamic_station = pd.read_sql_query("SELECT * FROM dynamic_station", dbikes)
    dynamic_weather = pd.read_sql_query("SELECT * FROM dynamic_weather", dbikes)
    # drop the duplicate data
    dynamic_station_each = dynamic_station.drop_duplicates()
    dynamic_station_each = dynamic_station_each.dropna()
    dynamic_weather_each = dynamic_weather.drop_duplicates()
    dynamic_weather_each = dynamic_weather_each.dropna()
    # convert the timestamp to date week and hours
    dynamic_station_each["last_update"] = pd.to_datetime(dynamic_station_each["last_update"], unit = "ms")
    dynamic_weather_each["last_update"] = pd.to_datetime(dynamic_weather_each["dt"], unit = "s")
    # add weekday to table as a column
    dynamic_station_each["weekday"] = dynamic_station_each["last_update"].map(lambda x: x.weekday())
    dynamic_weather_each["weekday"] = dynamic_weather_each["last_update"].map(lambda x: x.weekday())
    # add hour to table as a column
    dynamic_station_each["hour"] = pd.to_datetime(dynamic_station_each["last_update"], format='%Y-%M-%D %H:%M:%S').dt.hour
    dynamic_weather_each["hour"] = pd.to_datetime(dynamic_weather_each["last_update"], format='%Y-%M-%D %H:%M:%S').dt.hour
    # merge two dynamic dataframe according to the nearest date
    dynamic_station_each = dynamic_station_each.sort_values(['last_update'])
    dynamic_weather_each = dynamic_weather_each.sort_values(['last_update'])
    dynamic_weather_each = dynamic_weather_each.drop(columns=["weekday","hour","dt"])
    station_weather_each = pd.merge_asof(dynamic_station_each, dynamic_weather_each,
                                   on = "last_update",by = "number", 
                                    direction="nearest", tolerance = pd.Timedelta("2 hour"))
    static_station_each = static_station.drop(columns=["name","lat","lng"])
    station_weather_each = pd.merge(station_weather_each,static_station_each)
    station_weather_each = station_weather_each.dropna()
    number_array = station_weather_each['number'].unique()
    return station_weather_each, number_array


# In[16]:


def savepickle(station_weather_each,number_array):
    for number in number_array:
        each_station_ds = station_weather_each[station_weather_each['number']==number]
        X = each_station_ds.loc[:,('bike_stands','weekday', 'hour', 'temp', 'pressure', 'wind_speed','humidity')]
        y = each_station_ds.loc[:,('available_bike_stands')]
        # train and test set division
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        RF_model = RandomForestRegressor(n_estimators=100, random_state=1)
        RF_model.fit(X_train, y_train)
        RF = RF_model.fit(X_train, y_train)
        # save the model to a pickle file
        filename = 'station_'+str(number)+'.sav'
        pickle.dump(RF, open(filename, 'wb'))


# In[17]:


def updatepickle():
    while True:
        station_weather_each, number_array = getinitialdf()
        savepickle(station_weather_each,number_array)
#         sleep 1 hour here because we update the future weather data 1 hour
        time.sleep(60*60)


# In[18]:


updatepickle()

