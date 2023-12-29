import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pbl"
)
mycursor = mydb.cursor()

class User:
    def __init__(self):
        self
        
    def nilai(self):
        sql = "SELECT * FROM users"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
        
    def cari_data(val1):
        sql = "SELECT * from users where id = %s"
        val = (val1,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchone()
        return myresult
    
    def login(val1, val2):
        sql = "SELECT level FROM users WHERE username = %s AND password = %s"
        val = (val1, val2)
        mycursor.execute(sql,val)
        level = mycursor.fetchone()
        return str(level[0])
    
    def select_data(self):
        sql = "SELECT * FROM users"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    
    def insert_data(val1,val2,val3,val4):
        sql = "INSERT INTO users (id, username, password, level) VALUES (%s, %s, %s, %s)"
        val = (val1,val2,val3,val4)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil ditambahkan...")
        
    def update_data(val1,val2,val3,val4):
        sql = "UPDATE user SET username = %s, password = %s, level = %s WHERE id = %s"
        val = (val1,val2,val3,val4,)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil diupdate...")
        
    def delete_data(val1):
        sql = "DELETE FROM users WHERE id = %s"
        value = (val1, )
        mycursor.execute(sql, value)
        mydb.commit()
        print(mycursor.rowcount, "Data berhasil dihapus")