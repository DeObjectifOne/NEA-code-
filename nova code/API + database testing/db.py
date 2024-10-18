import sqlite3

conn = sqlite3.connect('temp.db')
c = conn.cursor()
'''
c.execute("""CREATE TABLE temporary (
              column1 text,
              column2 text
              )""")
'''
t = 'value5'
i = 'value5'

c.execute("INSERT INTO temporary (column1, column2) VALUES (?, ?)", (t, i))
c.execute("SELECT column1 FROM temporary")
ff = c.fetchall()
print(ff)

conn.commit()
conn.close()
