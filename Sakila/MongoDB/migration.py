from DataBases.SqlConnector import SqlDataBase

def main():
    db = SqlDataBase('root','carroz98')

    table = db.tablequery('SELECT * from customer, address, city, country where customer.address_id = address.address_id  AND address.city_id = city.city_id AND city.country_id = country.country_id')

    print(len(table))

    return

if __name__ == "__main__":
    main()