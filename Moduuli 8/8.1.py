import mysql.connector

def Hae_lentokenttä():
    sql = "SELECT ident FROM airport"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for lentokentta in tulos:
            print(lentokentta[0])
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

Hae_lentokenttä()
