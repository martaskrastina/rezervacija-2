from tkinter import *
from tkinter import ttk
from datetime import timedelta, date


#izveido sākuma ekrānu
window=Tk()
window.title("Viesnīcas rezervācija")
window.geometry("550x450")


def gatavs_vertiba():
  print("Viesnīca ir rezervēta!")

#izveido etiķetes
vards=Label(window, text="Vārds")
vards.grid(row=1, column=2)
uzvards=Label(window, text="Uzvārds")
uzvards.grid(row=2,column=2)
tel=Label(window,text="Telefona numurs")
tel.grid(row=3,column=2)
epasts=Label(window,text="E-pasts")
epasts.grid(row=4,column=2)

#saraksta kādas vērtības var būt katram mainīgajam
vards_vertiba=StringVar
uzvards_vertiba=StringVar
tel_vertiba=StringVar
epasts_vertiba=StringVar
check_vertiba=IntVar

#izveido kastes, kurās lietotājs varēs ievadīt personīgo iznformāciju
vards_kaste=Entry(window,textvariable=vards_vertiba)
vards_kaste.grid(row=1, column=3)
uzvards_kaste=Entry(window,textvariable=uzvards_vertiba)
uzvards_kaste.grid(row=2, column=3)
tel_kaste=Entry(window,textvariable=tel_vertiba)
tel_kaste.grid(row=3, column=3)
epasts_kaste=Entry(window,textvariable=epasts_vertiba)
epasts_kaste.grid(row=4,column=3)


check_kaste=Checkbutton(text="Atcerēties mani",variable=check_vertiba)
check_kaste.grid(row=5,column=3)

Button(text="Rezervēt",command=gatavs_vertiba).grid(row=6,column=3)


#uz ekrāna izveido pirmo lapu
window.mainloop()