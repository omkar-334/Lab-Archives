import sqlite3 as sql
conn=sql.connect('aquarium.db')
out1=conn.execute('select tank,name,species,age from fish').fetchall()
print(*out1,sep="\n")


out2=conn.execute('select name from fish where tank=1').fetchall()
print(*out2,sep='\n')


out3=conn.execute('select species from fish where tank=2').fetchall()
print(*out3,sep='\n')
conn.close()