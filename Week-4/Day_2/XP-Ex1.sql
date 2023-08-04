/*
CREATE TABLE items(
id SERIAL PRIMARY KEY,
item VARCHAR(20),
price INT
);

CREATE TABLE customers(
id SERIAL PRIMARY KEY,
first_name VARCHAR(20),
last_name VARCHAR(40)
); */
/*
INSERT INTO items(item,price)
VALUES ('Small Desk',100),
	   ('Large desk',300),
	   ('Fan',80);
Ex 1	   
INSERT INTO customers(first_name,last_name)
VALUES('Greg','Jones'),
	  ('Sandra','Jones'),
	  ('Scott','Scott'),
	  ('Trevor','Green'),
	  ('Melanie','Johnson'); 

-- All items, ordered by price (lowest to highest)
SELECT * FROM items
ORDER BY price

-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
SELECT * FROM items
WHERE price >= 80
ORDER BY price DESC

-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
SELECT first_name,last_name FROM customers
ORDER BY first_name
LIMIT 3

-- All last names (no other columns!), in reverse alphabetical order (Z-A)
SELECT last_name FROM customers
ORDER BY last_name DESC*/




