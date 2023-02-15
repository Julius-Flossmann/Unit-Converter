#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Julius Versuch Moritz Gottvorschlag zu verstehen und auf Gewicht zu überragen. 

# Importiere Tkinter für GUI
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 13:34:05 2023

# -*- coding: utf-8 -*-
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
#Entry ist das Eingabefeld, je nach Tab muss es dann zu page 2 usw angepasst werden
entry1 = tk.Entry(page1)
entry1.pack()
#Das ist eine Liste, für das dropdown Auswahlfeld
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
notebook.add(page2, text="Seite 2")

Überschrift2 = tk.Label(page2, text='Hier kannst du Gewicht in andere Einheiten umwandeln')
Überschrift2.pack()
#Entry ist das Eingabefeld, je nach Tab muss es dann zu page 2 usw angepasst werden
entry2 = tk.Entry(page2)
entry2.pack()
#Das ist eine Liste, für das dropdown Auswahlfeld
#Es ist ein weight angehängt, damit klar ist auf dieser Seite geht es um Gewicht
# Bitte anpassen für 
unitweight=['Tonne'
,'Gramm'
,'Kilogramm']
#Hier wird die Liste gedoppelt und als StringVar umgewandelt, damit es zwei unabhängige dropdown Auswahlfelder gibt
variable2 = StringVar(root)
variable2.set(unitweight[0])
variabl2 = StringVar(root)
variabl2.set(unitweight[0])
#Hier wir das Dropdown Auswahlfeld erstellt
Startunitweight = tk.OptionMenu(page2, variable2, *unitweight)
Endunitweight = tk.OptionMenu(page2,variabl2, *unitweight)
#Das ist ein Dictionary, damit wird die Eigabe mit den Werten zum umrechnen verknüpft
# Nenne das 
unitweightzzz={'Gramm': 1
,'Kilogramm': 1000, 'Tonne': 1000000 }
# Die Rechnung zum Einheitenumwandeln, beachte, dass im unitweight die Zahl so verändert wurde, dass
# jetzt bei der berechnung zum Basiswert(1.Schritt) bzw SI Einheit immer multipliziert werden kann
# je nachdem für welche Einheiten gruppe muss das angepasst werden und die Zahl im unitweight auch 
def Berechnung2(wert2):
    zwischenwert2 =  wert2 * unitweightzzz[variable2.get()]
    return zwischenwert2/unitweightzzz[variabl2.get()]

eingabe2 = 0
def wennbestaetigt2():
    try:
        eingabe2 = float(entry2.get())
        #den Ausgabentext können wir später noch anpassen
        ausgabentext2 = tk.Label(page2, text=str(round(Berechnung2(eingabe2),2)))
        ausgabentext2.pack()
    except ValueError:
        print("Eingabe muss Zahl sein")
button2 = tk.Button(page2, text="Eingabe bestaetigen", command=wennbestaetigt2)
button2.pack()
Startunitweight.pack(side= 'left',expand=True)
Endunitweight.pack(side= 'right',expand=True)
#   .pack bedeutet, das vorher erstellt soll an einer stelle im Programm eingefügt werden
notebook.add(page2, text="Gewicht")

######################################################################################################
page3 = ttk.Frame(notebook)
entry3 = tk.Entry(page3)
entry3.pack()
notebook.add(page3, text="Seite 3")

notebook.pack(expand=True, fill="both")
# root.mainloop muss ganz am Ende des Programms stehen
root.mainloop()
