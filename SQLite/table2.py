import sqlite3 as sql
conn=sql.connect("aquarium.db")
conn.execute('create table food (tank INT, food_mg INT, frequency INT)')
conn.execute('insert into food values(1,250,2)')
conn.execute('insert into food values(2,500,3)')
conn.execute('insert into food values(1,250,3)')
conn.commit()
out=conn.execute('select tank,food_mg,frequency from food')
print(*out,sep='\n')