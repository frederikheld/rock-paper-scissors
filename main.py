import tkinter as tk
from tkinter import Canvas, PhotoImage

import random

window = tk.Tk()

window.geometry('800x600')

canvas = Canvas(window, bg="white", width=800, height=600)

canvas.pack()

imagePaper = PhotoImage(file='assets/img/paper.png')

for elem in range(10):
    canvas.create_image(random.randint(0, 800), random.randint(0, 600), image=imagePaper)
#canvas.create_image(350, 230, image=imagePaper)

## Koordinatensystem --> Canvas initialisieren

## Gegenstände  --> Grafik-Objekte auf dem Canvas initialisieren

## Schleife

    ## Gegenstände bewegen sich --> Algorithmus
        ## erst mal random
        ## später: gezielt auf das Opfer zu bewegen (Sichtfeld & gezielte Bewegung)

    ## Kollisionserkennung

    ## bei Kollision:
        ## RPS Regeln anwenden
        ## Verlierer wird umgewandelt in typ des Gewinner-Objekts

    ## Wenn nur ein Typ übrig ist: schleife beenden
    
## Gewinner bekannt geben

window.mainloop()