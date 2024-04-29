import sqlite3 as sql
conn=sql.connect('aquarium.db')
conn.execute('update FISH set species="Shark" where name="Omkar"')
conn.commit()
print("Changes - ",conn.total_changes)
out=conn.execute('Select tank,name,species,age from fish')
print(*out,sep='\n')