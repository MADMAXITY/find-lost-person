import sqlite3


def create(conn):
    conn.execute(
        """CREATE TABLE COMPANY  NAME TEXT NOT NULL,EMAIl      INT     NOT NULL,PASSWORD TEXT;"""
    )


def insertion(conn, NAME, EMAIL, PASSWORD):
    conn.execute(f"INSERT INTO COMPANY VALUES({NAME}, {EMAIL}, {PASSWORD}")


def show(conn):
    data = conn.execute("SELECT * FROM COMPANY")
    for row in data:
        print(row)


conn = sqlite3.connect("test.db")
create(conn)
n, e, p = "Shankar", "shankar@gmail.com", "passit"
insertion(conn, n, e, p)

n, e, p = "Shankari", "shankar@hotmail.com", "passitmate"
insertion(conn, n, e, p)

show(conn)