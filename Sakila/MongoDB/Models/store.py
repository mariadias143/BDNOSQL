queryStore = "select * from store"
queryAdress = "select a.address,a.district,a.postal_code,a.phone ,ci.city,co.country from store s, address a , city ci, country co where s.address_id = a.address_id and ci.city_id=a.city_id and ci.country_id=co.country_id and s.store_id =%s"
queryFilm = "select distinct f.film_id , f.title,f.description,f.release_year,f.rental_duration,f.rental_rate,f.length,f.replacement_cost,f.rating,f.special_features from inventory i , film f where i.film_id = f.film_id AND store_id = %s "
queryStaff = "select s.first_name, s.last_name, s.email, s.active, s.username ,s.password, a.address,a.district,a.phone,ci.city,co.country from staff s, address a, city ci , country co  where s.address_id = a.address_id  and a.city_id = ci.city_id and ci.country_id=co.country_id and s.store_id = %s"
queryInventario = "select count(*) from inventory where film_id= %s and store_id =%s"
class Store:
    def __init__(self,address,films,staff):
        self.address= address
        self.films = films
        self.staff= staff


    def getStore_id(self):
        return self.store_id
    def getAdress(self):
        return self.adress
    def getFilms(self):
        return self.films
    def getStaff(self):
        return self.staff
    
    

    def staffList(self):
        staff = []
        for sta in self.staff:
            dic = dict()
            dic["first_name"]=sta[0]
            dic["last_name"]=sta[1]
            dic["email"]=sta[2]
            dic["active"]=sta[3]
            dic["username"]=sta[4]
            dic["password"]=sta[5]
            dic["address"]=sta[6]
            dic["district"]=sta[7]
            dic["phone"]=sta[8]
            dic["city"]=sta[9]
            dic["country"]=sta[10]
            staff.append(dic)
        return staff

    def filmsList(self,id_store,dbSQL):
        films = []
        for film in self.films:
            dic = dict()
            dic["title"]=film[1]
            dic["description"]=film[2]
            dic["release_year"]=str(film[3])
            dic["rental_duration"]=str(film[4])
            dic["rental_rate"]=str(film[5])
            dic["length"]=str(film[6])
            dic["replacement_cost"]=str(film[7])
            dic["rating"]=str(film[8])
            dic["special_features"]=list(film[9])
            inventario =dbSQL.queryWithArgs(queryInventario,(film[0],id_store))  
            dic["inventario"] = inventario[0][0]
            films.append(dic)
        return films

    def dictonary(self,id_store,bdSQL):
       dic = dict()
       dic["address"]=self.address[0][0]
       dic["district"]=self.address[0][1]
       dic["postal_code"]=str(self.address[0][2])
       dic["phone"]=str(self.address[0][3])
       dic["city"]=self.address[0][4]
       dic["country"]=self.address[0][5]
       dic["staff"] = self.staffList()
       dic["films"] = self.filmsList(id_store,bdSQL)
       return dic




def insertStores(dbSQL,dbMongo):
    table = dbSQL.tablequery(queryStore)
    for row in table:
        id_store=str(row[0])
        address = dbSQL.queryWithArgs(queryAdress,(id_store,))
        films = dbSQL.queryWithArgs(queryFilm,(id_store,))     
        staff = dbSQL.queryWithArgs(queryStaff,(id_store,))
        store = Store(address,films,staff)
        mydict = store.dictonary(id_store,dbSQL)
        dbMongo.store.insert_one(mydict)
    
    



