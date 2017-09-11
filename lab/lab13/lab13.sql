.read sp17data.sql
.read su17data.sql

CREATE TABLE obedience AS
  select seven, image from students;

CREATE TABLE smallest_int AS
  select time, smallest from students where smallest > 5 order by smallest limit 20;

CREATE TABLE greatstudents AS
  select a.date, a.color, a.pet, b.number, a.number FROM sp17students AS a, students AS b 
  		WHERE a.date = b.date and a.color = b.color and a.pet = b.pet;

CREATE TABLE sevens AS
  select seven FROM students AS a, checkboxes AS b 
  		WHERE a.time = b.time and a.number = 7 and b.'7' = 'True';

CREATE TABLE matchmaker AS
  select a.pet, a.beets, a.color, b.color FROM students AS a, students AS b
  		WHERE a.pet = b.pet and a.beets = b.beets and a.time < b.time;
