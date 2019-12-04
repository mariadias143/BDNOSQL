queryFilm = "SELECT * from film"
queryCategory ="select c.name from film_category fc, category c where c.category_id= fc.category_id AND film_id= %s "
queryLanguage = "select l.name from language l, film f where l.language_id = f.language_id AND film_id= %s "
queryActor = "select a.first_name,a.last_name from film_actor fl, actor a where fl.actor_id=a.actor_id AND fl.film_id= %s"



class Film:
    def __init__(self,film_id,title,description,release_year,rental_duration,rental_rate,length,
    replacement_cost,rating,special_features,last_update,category,language,actors):
        self.film_id = film_id
        self.title = title
        self.description = description
        self.release_year = release_year
        self.rental_duration=rental_duration
        self.rental_rate = rental_rate
        self.length = length
        self.replacement_cost = replacement_cost
        self.rating = rating 
        self.special_features = special_features
        self.last_update = last_update
        self.category = category
        self.language = language
        self.actors = actors


    def getFilm_id(self):
        return self.film_id

    def getActors(self):
        return self.actors    

    def categoryList(self):
        category = []
        for cat in self.category:
                category.append(cat[0])
        return category

    def actorsList(self):
        actors = []
        for actor in self.actors:
                actors.append(actor[0] + ' ' + actor[1])
        return actors
    
    
    def dictonary(self):
       dic = dict()
       dic["film_id"]=self.film_id
       dic["title"]=self.title
       dic["description"]=self.description
       dic["release_year"]=str(self.release_year)
       dic["rental_duration"]=str(self.rental_duration)
       dic["rental_rate"]=str(self.rental_rate)
       dic["length"]=str(self.length)
       dic["replacement_cost"]=str(self.replacement_cost)
       dic["rating"]=str(self.rating)
       dic["language"]= self.language[0][0]
       dic["special_features"]=list(self.special_features)
       dic["category"]=self.categoryList()
       dic["actors"]= self.actorsList()
       return dic


def insertFilms(dbSQL,dbMongo):
    table = dbSQL.tablequery(queryFilm)
    for row in table:
        id_film=str(row[0])
        category = dbSQL.queryWithArgs(queryCategory,(id_film,))
        language = dbSQL.queryWithArgs(queryLanguage,(id_film,))
        actors = dbSQL.queryWithArgs(queryActor,(id_film,))
        film = Film(row[0],row[1],row[2],row[3],row[6],row[7],row[8],row[9],row[10],row[11],row[12],category,language,actors)
        mydict = film.dictonary()
        dbMongo.film.insert_one(mydict)




          
    