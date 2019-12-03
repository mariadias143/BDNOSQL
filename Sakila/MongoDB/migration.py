from DataBases.SqlConnector import SqlDataBase
from Models.film import insertFilms
from Models.store import insertStores
from pymongo import MongoClient



def main():
    client = MongoClient("mongodb://localhost:27017/")
    dbMongo = client.Sakila
    dbSQL = SqlDataBase('root','password')
    
    insertFilms(dbSQL,dbMongo)
    insertStores(dbSQL,dbMongo)

 


if __name__ == "__main__":
    main()
