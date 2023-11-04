import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password ="",
    database = "my_oop_database"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM user")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)