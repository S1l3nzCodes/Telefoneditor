import MySQLdb
import sys
connection = MySQLdb.connect (host = "192.168.2.200", user = "radistart", passwd = "radistart", db = "Telefonbuch")
cursor = connection.cursor ()
Name=raw_input('Name:')
Nummer=raw_input('Nummer:')
Info=raw_input('Info:')
cursor.execute("""INSERT INTO Telefonliste2 values (%s, %s, %s)""",(Name, Nummer, Info))
connection.commit()



cursor.execute ("SELECT * FROM Telefonliste2")
result = cursor.fetchall ()
if result:
            for z in result:
                        print z[0]+' \t'+ z[1]+' \t'+z[2] #+ '\t'+ z[3]+' \t'+z[4]+' \t'+z[5]


cursor.close ()
connection.close ()
sys.exit()
