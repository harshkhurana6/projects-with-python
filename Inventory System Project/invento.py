import sqlite3
sqlite_file='invent.sqlite'
conn=sqlite3.connect(sqlite_file)
c=conn.cursor()
#c.execute('Create table if not exists tblogin(username Text,password Text)')
#c.execute('alter table tbstock add picpath Text')
#c.execute('Create table if not exists tbstock (icode Text, iname Text,rate Text,qih Text,doi Text,qtyissue Text)')
c.execute('update tbstock set picpath=? where icode=?',('images/bacardi.png',1031))
conn.commit()
conn.close()
