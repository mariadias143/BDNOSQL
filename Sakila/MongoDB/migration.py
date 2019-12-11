from DataBases.SqlConnector import SqlDataBase
from Models.film import insertFilms
from Models.store import insertStores
from Models.rental import buildRentals
from Models.payment import insertPayments
from pymongo import MongoClient



def main():
    client = MongoClient("mongodb://localhost:27017/")
    dbMongo = client.Sakila
    dbSQL = SqlDataBase('root','carroz98')
    
    #insertFilms(dbSQL,dbMongo)
    #insertStores(dbSQL,dbMongo)

    #buildRentals(dbSQL)
    insertPayments(dbSQL,dbMongo)

 


if __name__ == "__main__":
    main()
    
