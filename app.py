from database.connection import connect

conn = connect()
cur = conn.cursor()
cur.execute("SELECT * FROM SAMPLE")

for res in cur:
    print(res)

