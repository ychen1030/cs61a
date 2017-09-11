.read lab13.sql

CREATE TABLE sp17favnum AS
  select number, COUNT(*) AS count FROM sp17students 
  		GROUP BY number ORDER BY count DESC LIMIT 1;


CREATE TABLE sp17favpets AS
  select pet, COUNT(*) AS count FROM sp17students
  		GROUP BY pet ORDER BY count DESC LIMIT 10;


CREATE TABLE su17favpets AS
  select pet, COUNT(*) AS count FROM students
  		GROUP BY pet ORDER BY count DESC LIMIT 10;


CREATE TABLE su17dog AS
  select pet, COUNT(*) FROM students WHERE pet = 'dog';


CREATE TABLE su17alldogs AS
  select pet, COUNT(*) FROM students WHERE pet LIKE '%dog%';


CREATE TABLE obedienceimage AS
  select seven, image, COUNT(*) FROM students WHERE seven = '7' GROUP BY image ORDER BY image;

CREATE TABLE smallest_int_count AS
  select smallest, COUNT(*) FROM students GROUP BY smallest ORDER BY smallest;
