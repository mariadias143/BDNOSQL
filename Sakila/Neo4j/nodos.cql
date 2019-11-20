//Actor Node
CREATE CONSTRAINT ON (a:actor) ASSERT a.actor_id IS UNIQUE;
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///actor.csv" AS line
CREATE (a:actor {actor_id: toInteger(line.actor_id),
first_name: line.first_name,
last_name: line.last_name,
last_update: line.last_update});


//Country Node
CREATE CONSTRAINT ON (cr:country) ASSERT cr.country_id IS UNIQUE;
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///country.csv" AS line
CREATE (cr:country {country_id: toInteger(line.country_id),
country: line.country,
last_update: line.last_update});

//City Node w/ relationship between city and country
CREATE CONSTRAINT ON (c:city) ASSERT c.city_id IS UNIQUE;
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///city.csv" AS line
MATCH (cr:country{country_id: toInteger(line.country_id)})
CREATE (c:city {city_id: toInteger(line.city_id),
city: line.city,
last_update: line.last_update})
MERGE (c)-[:belongs_to]->(cr);

//Address Node w/ relationship between address and city
CREATE CONSTRAINT ON (ad:address) ASSERT ad.address_id IS UNIQUE;
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///address.csv" AS line
MATCH (c:city{city_id: toInteger(line.city_id)})
CREATE (ad:address {address_id: toInteger(line.address_id),
address: line.address,
address2: line.address2,
district: line.district,
postal_code: line.postal_code,
phone: line.phone,
last_update: line.last_update})
MERGE (ad)-[:contained_in]->(c);

//Category Node
CREATE CONSTRAINT ON (cat:category) ASSERT cat.category_id IS UNIQUE;
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///category.csv" AS line
CREATE (cat:category {category_id: toInteger(line.category_id),
name: line.name,
last_update: line.last_update});

//Language Node
CREATE CONSTRAINT ON (l:language) ASSERT l.language_id IS UNIQUE;
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///language.csv" AS line
CREATE (l:language {language_id: toInteger(line.language_id),
name: line.name,
last_update: line.last_update});

//Film Node 
CREATE CONSTRAINT ON (f:film) ASSERT f.film_id IS UNIQUE;
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///film.csv" AS line
MATCH (l:language {language_id: toInteger(line.language_id)})
CREATE (f:film {film_id: toInteger(line.film_id),
title: line.title,
description: line.description,
release_year: toInteger(line.release_year),
rental_duration: toInteger(line.rental_duration),
rental_rate: toFloat(line.rental_rate),
length: toInteger(line.length),
replacement_cost: toFloat(line.replacement_cost),
rating: line.rating,
special_features: line.special_features,
last_update: line.last_update})
MERGE (f)-[:in_language]->(l); //change relationships names

//Relationship N:M between film and actor
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///film_actor.csv" AS line
MATCH(f:film {film_id: toInteger(line.film_id)})
MATCH(a:actor {actor_id: toInteger(line.actor_id)})
MERGE (a)-[:acted_in]->(f);

//Relationship N:M between film and category
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///film_category.csv" AS line
MATCH(f:film {film_id: toInteger(line.film_id)})
MATCH(cat:category {category_id: toInteger(line.category_id)})
MERGE (f)-[:categorized_in]->(cat);


//Inventory Node
CREATE CONSTRAINT ON (i:inventory) ASSERT i.inventory_id IS UNIQUE;
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///inventory.csv" AS line
CREATE (i:inventory {inventory_id: toInteger(line.inventory_id),
film_id: line.film_id,
store_id: line.store_id});


//Store Node
CREATE CONSTRAINT ON (s:store) ASSERT s.store_id IS UNIQUE;
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///store.csv" AS line
MATCH (ad:address{address_id: toInteger(line.address_id)})
CREATE (s:store {store_id: toInteger(line.address_id),
manager_staff_id: toInteger(line.manager_staff_id),
last_update: line.last_update})
MERGE (s)-[:located_in]->(ad);

//Staff Node
CREATE CONSTRAINT ON (sf:staff) ASSERT sf.staff_id IS UNIQUE;
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///staff.csv" AS line
MATCH (ad:address{address_id: toInteger(line.address_id)}), (s:store{store_id: toInteger(line.store_id)})
CREATE (sf:staff {staff_id: toInteger(line.staff_id),
first_name: line.first_name,
last_name: line.last_name,
email: line.email,
active: toBoolean(line.active),
username: line.username,
password: line.password,
last_update: line.last_update})
MERGE (s)<-[:works_at]-(sf)-[:lives_in]->(ad);

//Create relationship between store and staff
MATCH (s:store),(sf:staff)
WHERE s.manager_staff_id = sf.staff_id
CREATE (sf)-[:manages]->(s);

//Remove manager_staff_id from Store Node
MATCH (st:store)
REMOVE st.manager_staff_id;

//Customer Node
CREATE CONSTRAINT ON (cm:customer) ASSERT cm.customer_id IS UNIQUE;
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///customer.csv" AS line
MATCH (ad:address{address_id: toInteger(line.address_id)}), (s:store{store_id: toInteger(line.store_id)})
CREATE (cm:customer {customer_id: toInteger(line.customer_id),
first_name: line.first_name,
last_name: line.last_name,
email: line.email,
active: toBoolean(line.active),
create_date: line.create_date,
last_update: line.last_update})
MERGE (s)<-[:shops_at]-(cm)-[:lives_in]->(ad);

//Rental Node
CREATE CONSTRAINT ON (r:rental) ASSERT r.rental_id IS UNIQUE;
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///rental.csv" AS line
MATCH (i:inventory{inventory_id: toInteger(line.inventory_id)}), (cm:customer{customer_id: toInteger(line.customer_id)}),
(sf:staff{staff_id: toInteger(line.staff_id)})
CREATE (r:rental {rental_id: toInteger(line.rental_id),
rental_date: line.rental_date,
return_date: line.return_date,
last_update: line.last_update})
MERGE (i)<-[:consists_of]-(r)-[:rented_by]->(cm)
MERGE (r)-[:approved_by]->(sf);

//Payment Node
CREATE CONSTRAINT ON (p:payment) ASSERT p.payment_id IS UNIQUE;
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///payment.csv" AS line
MATCH (r:rental{rental_id: toInteger(line.rental_id)}), (cm:customer{customer_id: toInteger(line.customer_id)}),
(sf:staff{staff_id: toInteger(line.staff_id)})
CREATE (p:payment {payment_id: toInteger(line.payment_id),
amount: toFloat(line.amount),
payment_date: line.payment_date,
last_update: line.last_update})
MERGE (r)<-[:related_to]-(p)-[:made_by]->(cm)
MERGE (p)-[:received_by]->(sf);
