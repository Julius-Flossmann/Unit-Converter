# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:14:19 2023

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
root.geometry('600x250')
# Erstellen des ttk.Notebook-Widgets
notebook = ttk.Notebook(root)
# Erste Seite zu Geschwindigkeit
# Erstellen von drei Seiten im ttk.Notebook
page1 = ttk.Frame(notebook)
Überschrift1 = tk.Label(page1, text='Hier kannst du Geschwindigkeiten in andere Einheiten umwandeln')
Überschrift1.pack(side='top')
#Entry ist das Eingabefeld, je nach Tab muss es dann zu page 2 usw angepasst werden
entry1 = tk.Entry(page1)
entry1.pack(side='left')
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
        ausgabentext.pack(side='right')
    except ValueError:
        print("Eingabe muss Zahl sein")

button = tk.Button(page1, text="Eingabe bestaetigen", command=wennbestaetigt)
button.pack()
Start = tk.Label(page1, text= 'Starteinheit')
Start.pack(side='left')
Starteinheitspeed.pack(side= 'left',expand=True)
End = tk.Label(page1, text='Zieleinheit')
End.pack(side='right')
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


def wennbestaetigt2():
    try:
        eingabe2 = float(entry2.get())
        #den Ausgabentext können wir später noch anpassen
        ausgabentext2 = tk.Label(page2, text='Deine letzte Berechnung ergibt '+str(round(Berechnung2(eingabe2),4)))
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

notebook.add(page3, text="Seite 3")

Überschrift3 = tk.Label(page3, text='Hier kannst du Volumen in andere Einheiten umwandeln')
Überschrift3.pack()
#Entry ist das Eingabefeld, je nach Tab muss es dann zu page 2 usw angepasst werden
entry3 = tk.Entry(page3)
entry3.pack()
#Das ist eine Liste, für das dropdown Auswahlfeld
#Es ist ein weight angehängt, damit klar ist auf dieser Seite geht es um Gewicht
# Bitte anpassen für 
unitvol=['Liter', 'Milliliter'
,'Pint'
,'cm³', 'm³', 'gallon']
#Hier wird die Liste gedoppelt und als StringVar umgewandelt, damit es zwei unabhängige dropdown Auswahlfelder gibt
variable3 = StringVar(root)
variable3.set(unitvol[0])
variabl3 = StringVar(root)
variabl3.set(unitvol[0])
#Hier wir das Dropdown Auswahlfeld erstellt
Startunitvol = tk.OptionMenu(page3, variable3, *unitvol)
Endunitvol = tk.OptionMenu(page3,variabl3, *unitvol)
#Das ist ein Dictionary, damit wird die Eigabe mit den Werten zum umrechnen verknüpft
# Nenne das 
unitvold={'Liter': 1
,'Milliliter': (1/1000), 'Pint': (1/2.113), 'cm³':(1/1000), 'm³':1000, 'gallon':3.785  }
# Die Rechnung zum Einheitenumwandeln, beachte, dass im unitweight die Zahl so verändert wurde, dass
# jetzt bei der berechnung zum Basiswert(1.Schritt) bzw SI Einheit immer multipliziert werden kann
# je nachdem für welche Einheiten gruppe muss das angepasst werden und die Zahl im unitweight auch 
def Berechnung3(wert3):
    zwischenwert3 =  wert3 * unitvold[variable3.get()]
    return zwischenwert3/unitvold[variabl3.get()]


def wennbestaetigt3():
    try:
        eingabe3 = float(entry3.get())
        #den Ausgabentext können wir später noch anpassen
        ausgabentext3 = tk.Label(page3, text='Deine letzte Berechnung ergibt '+str(round(Berechnung3(eingabe3),4)))
        ausgabentext3.pack()
    except ValueError:
        print("Eingabe muss Zahl sein")
button3 = tk.Button(page3, text="Eingabe bestaetigen", command=wennbestaetigt3)
button3.pack()
Startunitvol.pack(side= 'left',expand=True)
Endunitvol.pack(side= 'right',expand=True)
#   .pack bedeutet, das vorher erstellt soll an einer stelle im Programm eingefügt werden
notebook.add(page3, text="Volumen")
notebook.pack(expand=True, fill="both")
# root.mainloop muss ganz am Ende des Programms stehen
##################################################################################################
page4 = ttk.Frame(notebook)

notebook.add(page4, text="Zeit")

Überschrift4 = tk.Label(page4, text='Hier kannst du Zeit in andere Einheiten umwandeln')
Überschrift4.pack()
#Entry ist das Eingabefeld, je nach Tab muss es dann zu page 2 usw angepasst werden
entry4 = tk.Entry(page4)
entry4.pack()
#Das ist eine Liste, für das dropdown Auswahlfeld
#Es ist ein weight angehängt, damit klar ist auf dieser Seite geht es um Gewicht
# Bitte anpassen für 
unittime=['Sekunde', 'Minute'
,'Stunde'
,'Tag', 'Woche', 'Jahr']
#Hier wird die Liste gedoppelt und als StringVar umgewandelt, damit es zwei unabhängige dropdown Auswahlfelder gibt
variable4 = StringVar(root)
variable4.set(unittime[0])
variabl4 = StringVar(root)
variabl4.set(unittime[0])
#Hier wir das Dropdown Auswahlfeld erstellt
Startunittime = tk.OptionMenu(page4, variable4, *unittime)
Endunittime = tk.OptionMenu(page4,variabl4, *unittime)
#Das ist ein Dictionary, damit wird die Eigabe mit den Werten zum umrechnen verknüpft
# Nenne das 
unittimed={'Sekunde': 1
,'Minute': 60, 'Stunde': (3600), 'Tag':(3600*24), 'Woche':(3600*168), 'Jahr':(3600*365.25*24)  }
# Die Rechnung zum Einheitenumwandeln, beachte, dass im unitweight die Zahl so verändert wurde, dass
# jetzt bei der berechnung zum Basiswert(1.Schritt) bzw SI Einheit immer multipliziert werden kann
# je nachdem für welche Einheiten gruppe muss das angepasst werden und die Zahl im unitweight auch 
def Berechnung4(wert4):
    zwischenwert4 =  wert4 *unittimed[variable4.get()]
    return zwischenwert4/unittimed[variabl4.get()]


def wennbestaetigt4():
    try:
        eingabe4 = float(entry4.get())
        #den Ausgabentext können wir später noch anpassen
        ausgabentext4 = tk.Label(page4, text='Deine letzte Berechnung ergibt '+str(round(Berechnung4(eingabe4),4)))
        ausgabentext4.pack()
    except ValueError:
        print("Eingabe muss Zahl sein")
button4 = tk.Button(page4, text="Eingabe bestaetigen", command=wennbestaetigt4)
button4.pack()
Startunittime.pack(side= 'left',expand=True)
Endunittime.pack(side= 'right',expand=True)
#   .pack bedeutet, das vorher erstellt soll an einer stelle im Programm eingefügt werden
notebook.add(page4, text="Zeit")
notebook.pack(expand=True, fill="both")
# root.mainloop muss ganz am Ende des Programms stehen
#############################################################################################
page5 = ttk.Frame(notebook)

notebook.add(page5, text="Druck")

Überschrift5 = tk.Label(page5, text='Hier kannst du Druck in andere Einheiten umwandeln')
Überschrift5.pack()
#Entry ist das Eingabefeld, je nach Tab muss es dann zu page 2 usw angepasst werden
entry5 = tk.Entry(page5)
entry5.pack()
#Das ist eine Liste, für das dropdown Auswahlfeld
#Es ist ein weight angehängt, damit klar ist auf dieser Seite geht es um Gewicht
# Bitte anpassen für 
unitpres=['Bar', 'psi'
,'Pascal', 'Hectopascal']
#Hier wird die Liste gedoppelt und als StringVar umgewandelt, damit es zwei unabhängige dropdown Auswahlfelder gibt
variable5 = StringVar(root)
variable5.set(unitpres[0])
variabl5 = StringVar(root)
variabl5.set(unitpres[0])
#Hier wir das Dropdown Auswahlfeld erstellt
Startunitpres = tk.OptionMenu(page5, variable5, *unitpres)
Endunitpres = tk.OptionMenu(page5,variabl5, *unitpres)
#Das ist ein Dictionary, damit wird die Eigabe mit den Werten zum umrechnen verknüpft
# Nenne das 
unitpred={'Bar': 100000
,'psi': 0.000145, 'Pascal': 1, 'Hectopascal':(1/100) }
# Die Rechnung zum Einheitenumwandeln, beachte, dass im unitweight die Zahl so verändert wurde, dass
# jetzt bei der berechnung zum Basiswert(1.Schritt) bzw SI Einheit immer multipliziert werden kann
# je nachdem für welche Einheiten gruppe muss das angepasst werden und die Zahl im unitweight auch 
def Berechnung5(wert5):
    zwischenwert5 =  wert5 / unitpred[variable5.get()]
    return zwischenwert5*unitpred[variabl5.get()]


def wennbestaetigt5():
    try:
        eingabe5 = float(entry5.get())
        #den Ausgabentext können wir später noch anpassen
        ausgabentext5 = tk.Label(page5, text='Deine letzte Berechnung ergibt '+str(round(Berechnung5(eingabe5),4)))
        ausgabentext5.pack()
    except ValueError:
        print("Eingabe muss Zahl sein")
button5 = tk.Button(page5, text="Eingabe bestaetigen", command=wennbestaetigt5())
button5.pack()
Startunitpres.pack(side= 'left',expand=True)
Endunitpres.pack(side= 'right',expand=True)
#   .pack bedeutet, das vorher erstellt soll an einer stelle im Programm eingefügt werden
notebook.add(page5, text="Druck")
notebook.pack(expand=True, fill="both")
# root.mainloop muss ganz am Ende des Programms stehen
root.mainloop()