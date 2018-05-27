import sqlite3


class DBInterface:
    def __init__(self):
        self.createTable()

    def createTable(self):
        conn = sqlite3.connect('plannerDB.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS
                  events(id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name text, date DATE, desc text, cycl INT)''')
        conn.commit()
        conn.close()

    def dbToList(self):
        conn = sqlite3.connect('plannerDB.db')
        c = conn.cursor()
        list = c.execute('SELECT * FROM events').fetchall()
        conn.commit()
        conn.close()
        return list

    def selectTable(self):
        conn = sqlite3.connect('plannerDB.db')
        c = conn.cursor()
        c.execute("INSERT INTO events (name, date, desc, cycl)"
                  " VALUES ('dziaga', '2018-5-28', 'granie w noge', 1)")
        for row in c.execute('SELECT * FROM events'):
            print(row)
        conn.commit()
        conn.close()

    def deleteRow(self, id):
        conn = sqlite3.connect('plannerDB.db')
        c = conn.cursor()
        c.execute("DELETE FROM events WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def addEvent(self, name, date, desc, cycl):
        conn = sqlite3.connect('plannerDB.db')
        c = conn.cursor()
        c.execute("INSERT INTO events (name, date, desc, cycl)"
                  " VALUES (?, ?, ?, ?)", (name, date, desc, cycl))
        for row in c.execute('SELECT * FROM events'):
            print(row)
        conn.commit()
        conn.close()
