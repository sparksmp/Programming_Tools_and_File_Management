import pandas
import sqlite3

def add_data_to_db():
    data = pandas.read_csv("data.csv", names=['Name', 'Age', 'Height', 'Weight'], skiprows = [0])
    conn = sqlite3.connect("people.db")
    cur = conn.cursor()

    cur.execute("CREATE TABLE if not exists data (Name text, Age int, Height int, Weight float)")

    for i in range(len(data)):
        a = data['Name'][i]
        b = data['Age'][i]
        c = data['Height'][i]
        d = data['Weight'][i]
        cur.execute("INSERT INTO data VALUES (\"%s\", %i, %i, %f)" % (a,b,c,d))

    conn.commit()
    conn.close()

def display_all_db_data():
    conn = sqlite3.connect('people.db')
    cur = conn.cursor()
    sql = "select * from DATA" 
    columns = cur.execute(sql)
    all_entries = columns.fetchall()
    for entry in all_entries:
        print(entry)  

def main():
    add_data_to_db()
    display_all_db_data()

main()
