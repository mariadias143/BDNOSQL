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
RETURN f.title AS Title, f.description AS Description;

//Lista dos atores com as categorias dos filmes em que participaram
MATCH(a:actor)-[:acted_in]->(f:film)-[:categorized_in]->(cat:category)
WITH a, collect(cat.name) AS catsActor
RETURN (a.first_name + " " + a.last_name) AS Actor catsActor AS Categories;

//Lista de lojas e número de filmes (inventário) que tem
MATCH(f:film)-[r:available_at]->(s:store)
RETURN s.store_id AS Store, sum(r.quantity) AS Inventory;

//Lista de filmes por categoria
MATCH(f:film)-[:categorized_in]->(cat:category)
WITH cat,collect(f.title) AS filmsList
RETURN distinct(cat.name) AS Category, filmsList AS Movies

//Lista do staff das lojas
MATCH(s:staff)-[:works_at]->(st:store)-[:located_in]->(ad:address)
WITH st, ad, collect(s.first_name + " " + s.last_name) AS listStaff
RETURN st.store_id AS ID, ad.address AS Location, listStaff AS Staff

//Filmes alugados por cada utilizador
MATCH(r:rental)-[:rented_by]->(cm:customer)
WITH cm, collect(distinct(r.item)) AS filmsList
RETURN (cm.first_name + " " + cm.last_name) AS Customer, filmsList as Watched_Films;


//Montante gasto por cada utilizador
MATCH(p:payment)-[:related_to]->(r:rental)-[:rented_by]->(cm:customer)
WITH cm, collect(p.amount) AS sales
UNWIND sales AS s
RETURN (cm.first_name + " " + cm.last_name) AS Customer, sum(s) as AMOUNT_SPENT
ORDER BY AMOUNT_SPENT DESC;

//Filmes mais alugados
MATCH(r:rental)
WITH r, collect(distinct(r.item)) AS rents
RETURN r.item AS Film, count(rents) AS nrRentals
ORDER BY nrRentals DESC
LIMIT 10;

//Filmes mais rentáveis
MATCH(p:payment)-[:related_to]->(r:rental)
WITH r, collect(p.amount) AS sales
UNWIND sales AS s
RETURN r.item AS Film, sum(s) AS Sales
ORDER BY Sales DESC;

//Categorias mais vista por um utilizador, e.g. SARAH LEWIS
MATCH(r:rental)-[:rented_by]->(cm:customer{first_name:'SARAH',last_name:'LEWIS'})
MATCH(f:film)-[:categorized_in]->(cat:category)
WHERE f.title = r.item
WITH cat, collect(cat.name) AS ctgs
RETURN head(ctgs) AS Most_Watched_Category, size(ctgs) AS NrRentals
ORDER BY NrRentals DESC
LIMIT 5;