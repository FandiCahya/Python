import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password ="",
    database = "my_oop_database"
)

mycursor = mydb.cursor()

sql="UPDATE user SET nama = %s WHERE id = %s"
val=("Cahya",1)
mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "Data berhasil diupdate..")
