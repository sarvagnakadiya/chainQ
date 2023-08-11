import sqlite3
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()

read_sql_query('SELECT * FROM transaction_data LIMIT 10;',
               "chainQ.db")