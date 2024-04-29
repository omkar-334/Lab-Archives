import sqlite3 as sql
conn=sql.connect('aquarium.db')
conn.execute('delete from FISH where name="Vinay"')
conn.commit()
out=conn.execute('Select name,species from fish').fetchall()
print(*out,sep='\n')