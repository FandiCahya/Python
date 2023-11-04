import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password ="",
    database = "my_oop_database"
)

mycursor = mydb.cursor()

sql="DELETE FROM user WHERE id = %s"
value=(2,)

mycursor.execute(sql,value)

mydb.commit()

print(mycursor.rowcount, "Data berhasil dihapus..")