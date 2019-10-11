#!/usr/bin/env python3
import sys
sys.path.append('/Users/mariadias/Documents/4º ANO/BDNOSQL/BDNOSQL/HealthcareSensor/Models')
import Biometrics
import Patient 
import Sensor 
import requests as req
import json


def fetch_json(id):
    url = "http://nosql.hpeixoto.me/api/sensor/300"
    url += id
    dic = req.get(url).json()
    return dic

def fetchAll(*args):
    if len(args) > 0 :
        url = []
        for elem in args :
            fetch_json(elem)
    else:
        for elem in range(1,5):
            fetch_json(elem)

def parse_json(dic):
    sensor = Sensor(dic['sensorid'],dic['sensornum'],dic['type_of_sensor'])
    patient = Patient(dic['patient']['patientid'],dic['patient']['patientname'],dic['patient']['patientbirthdate'],dic['patient']['patientage'],dic['sensorid'])
    biometrics = Biometrics(dic['bodytemp'],dic['bloodpress']['systolic'],dic['bloodpress']['diastolic'],dic['bpm'],dic['timestamp'],dic['sensorid'])


def update_biometrics(dic):