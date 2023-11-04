import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password ="",
    database = "my_oop_database"
)

mycursor = mydb.cursor()

sql="UPDATE user SET level = 'Admin' WHERE id = 2"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "Data berhasil diupdate..")
