import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password ="",
    database = "my_oop_database"
)

mycursor = mydb.cursor()

sql="SELECT * FROM user WHERE id = %s"
val= ("1",)

mycursor.execute(sql, val)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)