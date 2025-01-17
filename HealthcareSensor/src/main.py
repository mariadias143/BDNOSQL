#!/usr/bin/env python3
import sys
from Models.Biometrics import Biometrics
from Models.Patient import Patient
from Models.Sensor import Sensor
from DataBase import DataBase
import requests as req
import json
import time

from getopt import getopt
opts, resto = getopt(sys.argv[1:],"s:t:")
dop = dict(opts)

sec_between = int(dop.get('-s',5))
total_time = int(dop.get('-t',999))


def fetch_json(id):
    url = "http://nosql.hpeixoto.me/api/sensor/300"
    url += str(id)
    dic = req.get(url).json()
    return dic

def fetchAll(*args):
    dic_list = []
    if len(args) > 0 :
        url = []
        for elem in args :
            fetch_json(elem)
    else:
        for elem in range(1,6):
            dic = fetch_json(elem)
            dic_list.append(dic)
    return dic_list

def parse_json(dic):
    sid = dic['sensorid']
    snum = dic['sensornum']
    tos = dic['type_of_sensor']
    sensor = Sensor(sid, snum, tos)

    pid = dic['patient']['patientid']
    pname = dic['patient']['patientname']
    pbirthdate = dic['patient']['patientbirthdate']
    page = dic['patient']['patientage']
    patient = Patient(pid, pname, pbirthdate, page, sid)

    btemp = dic['bodytemp']
    syst = dic['bloodpress']['systolic']
    diast = dic['bloodpress']['diastolic']
    bpm = dic['bpm']
    tstamp = dic['timestamp']
    biometrics = Biometrics(btemp, syst, diast, bpm, tstamp, sid)

    return sensor, patient, biometrics


def main():
    db = DataBase('root','carroz98')

    dados = []
    dados = fetchAll()

    global sec_between
    global total_time

    if (sec_between > total_time):
        total_time = sec_between
    
    sec_spent = 0

    while sec_spent < total_time:
        dados = fetchAll()
        for dic in dados:
            sensor, patient, biometrics = parse_json(dic)  
            if (db.verify(sensor)):
                db.insert(sensor)
            if (db.verify(patient)):
                db.insert(patient)
            db.insert(biometrics)
        time.sleep(sec_between)
        sec_spent += sec_between 


if __name__ == "__main__":
    main()