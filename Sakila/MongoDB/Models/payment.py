from datetime import datetime
from Models.rental import buildRentals

class User:
    def __init__(self,id,first_name,last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
    
    def toDic(self):
        dic = {}
        dic['customer_id'] = self.id
        dic['first_name'] = self.first_name
        dic['last_name'] = self.last_name

        return dic


class Payment:
    def __init__(self,id,date,value,user,rental):
        self.id = id
        self.date = date.strftime("%Y-%m-%d %H:%M:%S")
        self.value = value
        self.user = user

        if rental is None:
            self.rental = None
        else:
            self.rental = rental

    def toDic(self):
        dic = {}
        dic['id'] = self.id
        dic['payment_date'] = self.date
        dic['amount'] = self.value
        dic['user'] = self.user.toDic()
        if self.rental is None:
            dic['rental'] = None
        else:
            dic['rental'] =  self.rental.toDic()

        return dic

def insertPayments(dbSQL,dbMongo):

    dicRentals = buildRentals(dbSQL)
    payments_rows = dbSQL.tablequery('select payment.payment_id, payment.payment_date, payment.amount, payment.rental_id, customer.customer_id, customer.first_name, customer.last_name from payment, customer where payment.customer_id = customer.customer_id')

    payments = []

    for row in payments_rows:
        user = User(row[4],row[5],row[6])
        rentalkey = None if row[3] is None else int(row[3])
        pay = Payment(row[0],row[1],float(row[2]),user,dicRentals.get(rentalkey,None))

        payments.append(pay)
    
    f_payments = list(map(lambda x: x.toDic(),payments))
    collection = dbMongo['payments']
    collection.insert_many(f_payments)
    

