#!C://Python/python.exe
# -*- coding: utf-8 -*-
import time
import os
import MySQLdb
import Tkinter as tk
import socket, getpass
import ScrolledText

U=getpass.getuser()
R=socket.gethostname()
serverIP="172.24.105.118"


#Layout
hellblau="#AFBCE4"
dunkelblau="#6D87CF"
orange="#EFC58B"
gruen="#A3C08B"
Font="helvetica 13"
buttonfarbe=orange
schriftgross="helvetica 18"
schriftmittel="arial 14"


def write():
            connection = MySQLdb.connect (host = serverIP, user = "radistart", passwd = "radistart", db = "Telefonbuch")
            cursor=connection.cursor()
            Z=time.asctime()
            Nummer=Entry_nummer.get()
            Name=Entry_name.get()
            Info=Entry_Info.get()
            Fax=Entry_Fax.get()
            cursor.execute("""INSERT INTO Telefonbuch (Name, Info, Nummer, Fax) values (%s, %s, %s, %s)""", (Name,Info,Nummer,Fax))
            connection.commit()
            result=cursor.execute("select * from Telefonbuch")
            #Entry_name.delete(0, 999)
            Entry_nummer.delete(0,999)
            Entry_Info.delete(0, 999)
            Entry_Fax.delete(0,9999)
            cursor.close()
            connection.close()

def read():
            connection = MySQLdb.connect (host =serverIP, user = "radistart", passwd = "radistart", db = "Telefonbuch")
            cursor = connection.cursor ()
            Text.delete("1.0","end")
            gesucht="'%"+str(Entry_name.get())+"%'"
            sql=("SELECT * FROM Telefonbuch WHERE name LIKE "+gesucht)
            print(sql)
            cursor.execute(sql)
            for i in cursor:
                I="Name:",i[0]," Info:", i[1], " Nummer:", i[2], "Fax:",i[3]
                Text.insert("end",I)
                Text.insert("end","\n")
            cursor.close()
            connection.close()

def readinfo():
            connection = MySQLdb.connect (host =serverIP, user = "radistart", passwd = "radistart", db = "Telefonbuch")
            cursor=connection.cursor()
            gesucht="'%"+str(Entry_Info.get())+"%'"
            sql=("SELECT * FROM Telefonbuch WHERE Info LIKE "+gesucht)
            print(sql)
            cursor.execute(sql)
            for i in cursor:
                I="Info:",i[1],"Name: ",i[0]," Nummer:",i[2],"Fax:",i[3]
                Text.insert("end",I)
                Text.insert("end","\n")
            cursor.close()
            connection.close()

def clear():
    Text.delete("1.0", "end")
    Entry_name.delete(0,99)
    Entry_Info.delete(0,99)

                
#GUI           
main=tk.Tk()
main.geometry("800x550+50+0")
main.maxsize(1100,1400)
main.title("Editor für das Online-Telefonbuch der Klinik für Radiologie und Neuroradiologie")
Label_uberschrift=tk.Label(main, text="Neue Telefondaten einfügen:", font="Helvetiva 16", bg=orange)
Label_uberschrift.pack(side="top", fill="x")





Frame_oberframe=tk.Frame(main, bd=3, bg=hellblau)
Frame_oberframe.pack(side="top",fill="both")

Frame_ersteZeile=tk.Frame(Frame_oberframe, relief="sunken", bd=2, bg=dunkelblau)
Frame_ersteZeile.pack(expand=1)
Frame_zweiteZeile=tk.Frame(Frame_oberframe, relief="sunken",bd=2, bg=dunkelblau)
Frame_zweiteZeile.pack(expand=1)
Frame_dritteZeile=tk.Frame(Frame_oberframe, relief="sunken",bd=2, bg=dunkelblau)
Frame_dritteZeile.pack(expand=1)
Frame_nummer=tk.Frame(Frame_ersteZeile, bd=2, bg=dunkelblau)
Frame_nummer.pack(expand=1, fill="x")
Frame_name=tk.Frame(Frame_ersteZeile, bd=2, bg=dunkelblau)
Frame_name.pack(expand=1, fill="x")
Frame_Info=tk.Frame(Frame_ersteZeile, bd=2, bg=dunkelblau)
Frame_Info.pack(expand=1, fill="x")
Frame_Fax=tk.Frame(Frame_ersteZeile, bd=2, bg=dunkelblau)
Frame_Fax.pack(expand=1, fill="x")
Frame_button=tk.Frame(Frame_dritteZeile, bd=2, bg=dunkelblau)
Frame_button.pack(expand=1, fill="x")



Label_nummer=tk.Label(Frame_nummer,text="Nummer:", font=Font, bg=dunkelblau)
Label_nummer.pack(side="left", expand=1, fill="x")
Label_name=tk.Label(Frame_name, text="Name:", font=Font, bg=dunkelblau)
Label_name.pack(side="left", expand=1, fill="x")
Label_Info=tk.Label(Frame_Info,text="Info:", font=Font, bg=dunkelblau)
Label_Info.pack(side="left", expand=1)
Label_Fax=tk.Label(Frame_Fax, text="Fax:", font=Font, bg=dunkelblau)
Label_Fax.pack(side="left", expand=1)

Entry_nummer=tk.Entry(Frame_nummer, width=45, font=Font)
Entry_nummer.pack(side="right")
Entry_name=tk.Entry(Frame_name, width=45, font=Font)
Entry_name.pack(side="right")
Entry_Info=tk.Entry(Frame_Info, width=45, font=Font)
Entry_Info.pack(side="right")
Entry_Fax=tk.Entry(Frame_Fax, width=45, font=Font)
Entry_Fax.pack(side="right")

#Buttons
Schreiben=tk.Button(Frame_button,text="in Datenbank schreiben", command=write, bg=gruen)
Schreiben.pack(side="left")
LesenName=tk.Button(Frame_button,text="Name in Datenbank suchen", command=read, bg=orange)
LesenName.pack(side="right")
LesenInfo=tk.Button(Frame_button,text="Info in Datenbank suchen", command=readinfo, bg=orange)
LesenInfo.pack(side="right")
Bclear=tk.Button(Frame_button,text="Suche löschen", command=clear, bg=orange)
Bclear.pack(side="right")

Text=ScrolledText.ScrolledText(main, width=140, height=15, font=schriftmittel)
Text.pack(expand=1, fill="y")

main.mainloop()

