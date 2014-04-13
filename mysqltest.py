import MySQLdb
import sys
connection = MySQLdb.connect (host = "192.168.2.200", user = "radistart", passwd = "radistart", db = "Telefonbuch")
cursor = connection.cursor ()
cursor.execute ("SELECT * FROM Telefonliste")
result = cursor.fetchall ()
if result:
            for z in result:
                        print 'Nummer: '+z[0]+ '; Name: ' +z[1]+ '; Information: '+z[2]


cursor.close ()
connection.close ()
sys.exit()
