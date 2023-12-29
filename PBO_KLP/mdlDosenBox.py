import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pbl"
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
    
class Instansi:

    def __init__(self):
        self

    def select_data():
        sql = "SELECT nama FROM instansi"
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
    
class Level:

    def __init__(self):
        self

    def select_data():
        sql = "SELECT level FROM level"
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