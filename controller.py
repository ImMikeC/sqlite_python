import sqlite3 as sql

def createDB():
    conn = sql.connect("streamers.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE streamers (
            name text,
            followers integer,
            subs integer
        )"""
    )
    conn.commit()
    conn.close()

def insertRow(nombre, followers, subs):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES ('{nombre}',{followers},{subs})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def readRows():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def insertRows(streamerList):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES (?, ?, ?)"
    cursor.executemany(instruccion, streamerList)
    conn.commit()
    conn.close()   

def readOrdered(field):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers ORDER BY {field}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)


if __name__ == "__main__":
    #createDB()
    #createTable()
    #insertRow("Manolo", 700000, 2500)
    #insertRow("Juyin", 1500000, 80000)
    readRows()
    # gallos = [
    #     ("Nachita", 500000, 3124),
    #     ("Emilia", 300000, 2145),
    #     ("Moira", 800000, 4754)
    # ]
    # insertRows(gallos)
    readOrdered("subs")