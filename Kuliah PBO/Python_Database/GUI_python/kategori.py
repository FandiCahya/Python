import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="my_oop_database"
)

mycursor = mydb.cursor()

class kategori:
    def __init__(self) :
        self

    def select_data():
        sql = "select kategori FROM kategori"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        data = []
        for x in myresult:
            data.append(str(x).replace("(","")
                        .replace("'","")
                        .replace(",","")
                        .replace(")",""))
            print(x)
        return data