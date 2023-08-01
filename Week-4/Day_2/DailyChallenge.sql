/*
CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)
INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')

-- assumption : the id column will be empty
SELECT * FROM FirstTab

CREATE TABLE SecondTab (
    id integer 
)

-- assumption : the id column will be 5 and null as the new rows
--INSERT INTO SecondTab VALUES
--(5),
--(NULL)
SELECT * FROM SecondTab */

-- What will be the OUTPUT of the following statement?
-- myanswer = an error will occur.
--SELECT COUNT(*) 
--FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

--What will be the OUTPUT of the following statement?
-- myanswer = count will be equal to 1
    --SELECT COUNT(*) 
    --FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
--What will be the OUTPUT of the following statement?
-- myanswer = count will be equal to 2
--SELECT COUNT(*) 
--FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

--What will be the OUTPUT of the following statement?
-- myanswer = count will be equal to 3
 SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )