import sqlite3

#create table of records
def createRecordsTable():
    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute(('''CREATE TABLE IF NOT EXISTS records
                    (url TEXT, username TEXT, password TEXT)'''))
    conn.commit()
    conn.close()

#add records to database table
def addDbRecord(url, username, password):
    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO records (url, username, password) VALUES (?, ?, ?)", (url, username, password))
    conn.commit()
    conn.close()

#delete records by row id number
def deleteDbRecord(id):
    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM records WHERE rowid = ?", (id,))
    conn.commit()
    conn.close()

def editDbRecord(id):
    pass

#return list of records in database and id number
def getRecords():
    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, * FROM records")
    records = cursor.fetchall()
    conn.close()
    return records

#return record from table based on id
def selectRecord(id):
    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("SELECT url, username, password FROM records WHERE rowid = ?", (id,))
    record = cursor.fetchone()
    conn.close()
    return record

#print(getRecords())
#print(selectRecord(3))
#deleteDbRecord(3)

createRecordsTable()
