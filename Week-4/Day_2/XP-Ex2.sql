-- In the dvdrental database write a query to select all the columns from the “customer” table.
--SELECT * FROM customer;

--display the names (first_name, last_name) using an alias named “full_name”.
-- SELECT (first_name , last_name) AS full_name FROM customer

--select all the create_date from the “customer” table (there should be no duplicates).
--SELECT DISTINCT create_date FROM customer

--get all the customer details from the customer table, it should be displayed in descending order by their first name.
--SELECT * FROM customer
--ORDER BY first_name;

--get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
--SELECT film_id,title,description,release_year,rental_rate FROM film
--ORDER BY rental_rate 

--  get the address, and the phone number of all customers living in the Texas district
--SELECT address,phone FROM address
--WHERE district = 'Texas';

--retrieve all movie details where the movie id is either 15 or 150.
--SELECT * FROM film
--WHERE film_id IN (15,150);

--check if your favorite movie exists in the database.get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.
--SELECT film_id,title,description,length,rental_rate FROM film
--WHERE title = 'Jurassic Park '

--get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.
--SELECT film_id,title,description,length,rental_rate FROM film
--WHERE title LIKE 'Ju%'

-- find the 10 cheapest movies.
--SELECT film_id ,title , description FROM film
--Order by replacement_cost
--LIMIT 10;

--find the next 10 cheapest movies.Bonus: Try to not use LIMIT.
SELECT film_id ,title , description FROM film
--Order by replacement_cost
--OFFSET 9
--FETCH FIRST 10 ROWS ONLY;

-- join the data in the customer table and the payment table. You want to get the first name and last name from the curstomer table, as well as the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).
--SELECT customer.first_name, customer.last_name AS full_name,payment.amount,payment.payment_date
--FROM customer
--INNER JOIN payment
--ON payment.customer_id = customer.customer_id
--ORDER BY customer.customer_id;

--get all the movies which are not in inventory.
--SELECT film.title FROM film 
--INNER JOIN inventory
--ON inventory.film_id != film.film_id;

--find which city is in which country.
--SELECT city.city,country.country
--FROM city
--INNER JOIN country
--ON city.country_id = country.country_id;

--SELECT customer.customer_id ,customer.first_name,customer.last_name,payment.amount,payment.payment_date,payment.staff_id
--FROM customer
--INNER JOIN payment
--ON customer.customer_id = payment.customer_id;

