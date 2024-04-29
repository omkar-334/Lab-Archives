import sqlite3 as sql
conn=sql.connect('aquarium.db')
out=conn.execute('select * from fish inner join food on fish.tank=food.tank')
# out=conn.execute('select tank,name,species from fish')
print(*out,sep='\n')
conn.close()