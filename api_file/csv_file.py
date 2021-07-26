import csv
import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()


with open('deals.csv', newline='') as person_table:

    dr = csv.DictReader(person_table)

    to_db = [(i['customer'], i['item'], i['total'], i['quantity'], i['date']) for i in dr]

cur.executemany("INSERT INTO t (customer, item, total, quantity, date) VALUES (?, ?, ?, ?, ?);", to_db)
con.commit()
