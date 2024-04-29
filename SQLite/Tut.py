import sqlite3

connection = sqlite3.connect("aquarium.db")
print(connection.total_changes)
cursor = connection.cursor()
cursor.execute("CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER)")
cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")
rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
print(rows)

#Reading Data
target_fish_name = "Jamie"
rows = cursor.execute(
    "SELECT name, species, tank_number FROM fish WHERE name = ?",
    (target_fish_name,),
).fetchall()
print(rows)

#Modifying Data
new_tank_number = 2
moved_fish_name = "Sammy"
cursor.execute(
    "UPDATE fish SET tank_number = ? WHERE name = ?",
    (new_tank_number, moved_fish_name)
)

rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
print(rows)

#Delete
released_fish_name = "Sammy"
cursor.execute(
    "DELETE FROM fish WHERE name = ?",
    (released_fish_name,)
)
rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
print(rows)

#inner join
SELECT a1, a2, b1, b2
FROM A
INNER JOIN B on B.f = A.f;

#outer join
SELECT *
FROM dogs 
FULL OUTER JOIN cats
    ON dogs.color = cats.color;
