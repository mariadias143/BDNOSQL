//Quantos filmes fez cada ator (lista ordenada por ordem descrescente)
MATCH(a:actor)-[r:acted_in]->(f:film)
RETURN (a.first_name + " " + a.last_name) AS Actor, COUNT(r) AS numFilms
ORDER BY numFilms DESC;

//Lista dos atores com os filmes em que participaram
MATCH(a:actor)-[r:acted_in]->(f:film)
WITH a, collect(f.title) AS filmList
RETURN (a.first_name + " " + a.last_name) AS Actor, filmList
ORDER BY Actor ASC;

//Dado um ator saber quais os filmes em que participou(e.g CARMEN HUNT)
MATCH(a:actor{first_name:'CARMEN',last_name:'HUNT'})-[r:acted_in]->(f:film)
RETURN f.title AS Title, f.description AS Description, f.category AS Category;

//Lista dos atores com as categoras dos filmes em que participaram -- uhm meh bue parecido ao outro
MATCH(a:actor)-[r:acted_in]->(f:film)
WITH a, collect(distinct(f.category)) AS catsActor
RETURN catsActor AS Categories, (a.first_name + " " + a.last_name) AS Actor;


//Top sales per film
MATCH(p:payment)-[:related_to]->(r:rental)
WITH r, collect(p.amount) AS sales
UNWIND sales AS s
RETURN r.item AS Film, sum(s) AS Sales
ORDER BY Sales DESC;

//Top sales per customer
MATCH(p:payment)-[:related_to]->(r:rental)-[:rented_by]->(cm:customer)
WITH cm, collect(p.amount) AS sales
UNWIND sales AS s
RETURN cm.first_name + " " + cm.last_name AS Customer, sum(s) as AMOUNT_SPENT
ORDER BY AMOUNT_SPENT DESC;

//Filmes alugados por cada utilizador --meh
MATCH(r:rental)-[:rented_by]->(cm:customer)
WITH cm, collect(distinct(r.item)) AS filmsList
RETURN cm.first_name + " " + cm.last_name AS Customer, filmsList as Watched_Films;