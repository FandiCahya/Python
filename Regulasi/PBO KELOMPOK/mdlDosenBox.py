import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_pbl"
)

mycursor = mydb.cursor()

class Dosen:

    def __init__(self):
        self

    def select_data():
        sql = "SELECT nama FROM dosen"
        mycursor.execute(sql)
        myresult= mycursor.fetchall()
        data=[]
        for x in myresult:
            data.append(str(x).replace("(","")
                        .replace("'","")
                        .replace(",","")
                        .replace(")","")) #hapus karakter object
            print(x)
        return data