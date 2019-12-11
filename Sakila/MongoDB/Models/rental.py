from datetime import datetime

class FilmRental:
    def __init__(self,id,title,categories):
        self.id = id
        self.title = title
        self.categories = categories

    def toDic(self):
        dic = {}
        dic['film_id'] = self.id
        dic['title'] = self.title
        dic['categories'] = self.categories

        return dic

class Rental:
    def __init__(self,rentalDate,returnDate,film):
        self.rental_date = rentalDate.strftime("%Y-%m-%d %H:%M:%S")
        if returnDate is None:
            self.return_date = None
        else:
            self.return_date = returnDate.strftime("%Y-%m-%d %H:%M:%S")
        self.film = film
    
    def toDic(self):
        dic = {}
        dic['rental_date'] = self.rental_date
        dic['return_date'] = self.return_date
        dic['film'] = self.film.toDic()

        return dic
        

def buildRentals(dbSQL):
    dicRental = {}
    rentals_to_transform = dbSQL.tablequery('SELECT * from rental')

    for row in rentals_to_transform:
        film_info = dbSQL.queryWithArgs('select film.film_id,film.title from film, inventory where film.film_id = inventory.film_id AND inventory.inventory_id = %s',(row[2],))[0]
        film_cat = []
        for catrow in dbSQL.queryWithArgs('select category.name from film_category, category where film_category.category_id = category.category_id AND film_category.film_id = %s',(film_info[0],)):
            film_cat.append(catrow[0])
        film = FilmRental(film_info[0],film_info[1],film_cat)

        rental = Rental(row[1],row[4],film)

        dicRental[int(row[0])] = rental

    return dicRental