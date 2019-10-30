#!/usr/bin/env python3
import sys
import requests as req
from pymongo import MongoClient
import json
import time

from getopt import getopt
opts, resto = getopt(sys.argv[1:],"s:t:")
dop = dict(opts)

sec_between = int(dop.get('-s',5))
total_time = int(dop.get('-t',999))


def fetch_sensor(id):
    url = "http://nosql.hpeixoto.me/api/sensor/300"
    url += str(id)
    dic = req.get(url).json()
    return dic

def fetch_cardiac(id):
    url = "http://nosql.hpeixoto.me/api/sensor/400"
    url += str(id)
    dic = req.get(url).json()
    return dic

def fetchAllSensors():
    dic_list = []
    for elem in range(1,6):
            sensor = fetch_sensor(elem)
            dic_list.append(sensor)
    return dic_list

def fetchAllCardiac():
    dic_list = []
    for elem in range(1,6):
            cardiac = fetch_cardiac(elem)
            dic_list.append(cardiac)
    return dic_list


def main():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["HealthCareSensors"]

    sensorCol = db["Sensor"]
    cardiacCol = db["Cardiac"]

    sensorData = []
    cardiacData = []

    global sec_between
    global total_time

    if (sec_between > total_time):
        total_time = sec_between
    
    sec_spent = 0

    while sec_spent < total_time:
        sensorData = fetchAllSensors()
        cardiacData = fetchAllCardiac()
        for dic in sensorData:
            sensorCol.insert_one(dic)
            print("Sensor data inserted")
        for dic in cardiacData:
            cardiacCol.insert_one(dic)
            print("Cardiac data inserted")
        time.sleep(sec_between)
        sec_spent += sec_between 


if __name__ == "__main__":
    main()