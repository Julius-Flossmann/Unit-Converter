# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 13:34:05 2023

@author: Moritz
"""

import tkinter as tk
from tkinter import ttk,StringVar, END, NONE

def open_page(page_num):
    # Aktualisieren des aktiven Reiters auf die ausgewählte Seite
    notebook.select(page_num)

root = tk.Tk()

# Hinzufügen des Menü-Widgets zum Hauptfenster

root.title('Einheitsumwandler')
root.geometry('900x600')
# Erstellen des ttk.Notebook-Widgets
notebook = ttk.Notebook(root)
# Erste Seite zu Geschwindigkeit
# Erstellen von drei Seiten im ttk.Notebook
page1 = ttk.Frame(notebook)
Überschrift1 = tk.Label(page1, text='Hier kannst du Geschwindigkeiten in andere Einheiten umwandeln')
Überschrift1.pack()
#Entry ist das EIngabefeld, je nach Tab muss es dann zu page 2 usw angepasst werden
entry1 = tk.Entry(page1)
entry1.pack()
#Das ist eine Liste, für das dropdaown Auswahlfeld
#Es ist ein speed angehängt, damit klar ist auf dieser Seite geht es um Geschwindigkeit
# Bitte anpassen für 
Einheitenspeed=['Meter pro Sekunde'
,'Kilometer pro Stunde'
,'Knoten'
,'Meilen pro Stunde']
#Hier wird die Liste gedoppelt und als StringVar umgewandelt, damit es zwei unabhängige dropdown Auswahlfelder gibt
variable = StringVar(root)
variable.set(Einheitenspeed[0])
variabl1 = StringVar(root)
variabl1.set(Einheitenspeed[0])
#Hier wir das Dropdown Auswahlfeld erstellt
Starteinheitspeed = tk.OptionMenu(page1, variable, *Einheitenspeed)
Endeinheitspeed = tk.OptionMenu(page1,variabl1, *Einheitenspeed)
#Das ist ein Dictionary, damit wird die Eigabe mit den Werten zum umrechnen verknüpft
# Nenne das 
Einheitenspeeddic={'Meter pro Sekunde': 1,'Kilometer pro Stunde':(1/3.6)
,'Knoten': 0.5144,'Meilen pro Stunde': 0.447}
# Die Rechnung zum Einheitenumwandeln, beachte, dass im Einheitenspeeddic die Zahl so verändert wurde, dass
# jetzt bei der berechnung zum Basiswert(1.Schritt) bzw SI Einheit immer multipliziert werden kann
# je nachdem für welche Einheiten gruppe muss das angepasst werden und die Zahl im Einheitenspeeddic auch 
def Berechnung(wert):
    zwischenwert =  wert * Einheitenspeeddic[variable.get()]
    return zwischenwert/Einheitenspeeddic[variabl1.get()]

eingabe = 0
def wennbestaetigt():
    try:
        eingabe = float(entry1.get())
        #den Ausgabentext können wir später noch anpassen
        ausgabentext = tk.Label(page1, text=str(round(Berechnung(eingabe),2)))
        ausgabentext.pack()
    except ValueError:
        print("Eingabe muss Zahl sein")

button = tk.Button(page1, text="Eingabe bestaetigen", command=wennbestaetigt)
button.pack()
Starteinheitspeed.pack(side= 'left',expand=True)
Endeinheitspeed.pack(side= 'right',expand=True)
#   .pack bedeutet, das vorher erstellt soll an einer stelle im Programm eingefügt werden
notebook.add(page1, text="Geschwindigkeit")

#################################################################################################
page2 = ttk.Frame(notebook)
entry2 = tk.Entry(page2)
entry2.pack()
notebook.add(page2, text="Seite 2")
######################################################################################################
page3 = ttk.Frame(notebook)
entry3 = tk.Entry(page3)
entry3.pack()
notebook.add(page3, text="Seite 3")

notebook.pack(expand=True, fill="both")
# root.mainloop muss ganz am Ende des Programms stehen
root.mainloop()