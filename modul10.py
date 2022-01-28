# sqlalchemy
# sqlite

import sqlite3 as sql
import os

# sqlite Serverlos und self-contained
# Nur eine schreibende Verbindung

try:
    conn = sql.connect("database.db", ) # Öffnet eine Verbindung und speichert sie in der Variable conn
except sql.Error as e:
    print(f"Fehler ist aufgetreten: {e}")
c = conn.cursor() # Pointer, der auf die derzeitige Tabelle im Speicher verweist
c.execute("create table if not exists Test (x int, y int)")  # Führt SQL Befehl aus
c.execute("Insert into Test values (?,?)", (12, 15))

conn.commit()  # Müssen comitten damit die Änderungen gespeichert werden
conn.close()  # Schließt die Datenbank verbindung

with sql.connect("database.db") as conn:
    c = conn.cursor()
    c.execute("create table if not exists zahlen (row1 int)") # Führt einen Befehl aus
    number = [(10,), (20,), (30,)]
    c.executemany("Insert into zahlen values (?)", number)  # Muss ein tuple übergeben werden
    # executemany() iteriert über seinen parameter und fügt jedes ELement in die Abfrage ein

    c.execute("Select * from zahlen") # Führt select befehl aus
    print(c.fetchone()) # Gib eine Zeile aus
    print(c.fetchone()) # Gib eine Zeile aus
    # Der cursor merkt sich in welcher Zeile er ist
    c.execute("Select * from test")
    print(c.fetchmany(5)) # Gibt fünf Zeilen als Liste aus
    # print(c.fetchall()) # Gibt alle Zeilen als Liste aus
    liste = c.fetchall() # Wenn das fetchall aus Zeile 34 ausgeführt wird
    # ist die Liste leer, da alle Zeilen aus dem Speicher geholt wurden
    print(liste)

# Da wir mit with arbeiten brauchen wir kein commit() und close(), der with Block
# führt beides automatisch aus





