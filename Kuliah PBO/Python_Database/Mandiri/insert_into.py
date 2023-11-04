import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password ="",
    database = "my_oop_database"
)

mycursor = mydb.cursor()

sql = "INSERT INTO user (nama, username, password, level) values (%s,%s,%s,%s)"
val = ("Cahya", "Cahyanoid", "12369", "Admin")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "Data berhasil ditambahkan..")
