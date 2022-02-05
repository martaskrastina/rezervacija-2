from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

numuri=["divvietīgs","trīsvietīgs","četrvietīgs"]

#izveido sākuma ekrānu
window=Tk()
window.title("Viesnīcas rezervācija")
window.geometry("550x450")

#kad nospiesta poga rezervēt konsolē parādās, ka viesnīca ir rezervēta un teksta failā tiek ievadīta informācija
def gatavs_vertiba():
  print("Viesnīca ir rezervēta!")
  vards1=vards_kaste.get()
  uzvards1=uzvards_kaste.get()
  tel1=tel_kaste.get()
  epasts1=epasts_kaste.get()
  f=open("klients.txt","a")
  f.write("Nummura lielums: " + numurs_vertiba.get() + "\n")
  f.write("Klienta vārds: " + vards1 + "\n")
  f.write("Klienta uzvārds: " + uzvards1 + "\n")
  f.write("Klienta telefona nummurs: " + tel1 + "\n")
  f.write("Klienta e-pasts: " + epasts1 + "\n" + "\n")
  

#izveido etiķetes
vards=Label(window, text="Vārds")
vards.grid(row=1, column=3)
uzvards=Label(window, text="Uzvārds")
uzvards.grid(row=2,column=3)
tel=Label(window,text="Telefona numurs")
tel.grid(row=3,column=3)
epasts=Label(window,text="E-pasts")
epasts.grid(row=4,column=3)

#saraksta kādas vērtības var būt katram mainīgajam
vards_vertiba=StringVar
uzvards_vertiba=StringVar
tel_vertiba=StringVar
epasts_vertiba=StringVar
check_vertiba=IntVar
numurs_vertiba=StringVar(window)
numurs_vertiba.set('divvietīgs')

#izveido kastes, kurās lietotājs varēs ievadīt personīgo iznformāciju
vards_kaste=Entry(window,textvariable=vards_vertiba)
vards_kaste.grid(row=1, column=4)
uzvards_kaste=Entry(window,textvariable=uzvards_vertiba)
uzvards_kaste.grid(row=2, column=4)
tel_kaste=Entry(window,textvariable=tel_vertiba)
tel_kaste.grid(row=3, column=4)
epasts_kaste=Entry(window,textvariable=epasts_vertiba)
epasts_kaste.grid(row=4,column=4)

#atcerēties mani kastīte
check_kaste=Checkbutton(text="Atcerēties mani",variable=check_vertiba)
check_kaste.grid(row=5,column=4)

#pga rezervēt
Button(text="Rezervēt",command=gatavs_vertiba).grid(row=6,column=4)

#numura lieluma izvēlēšanās
Label(window,text="Izvēlies numura lielumu").grid(row=1,column=1)
numurs_kaste=Combobox(window,values=numuri).grid(row=2,column=1)

#uz ekrāna izveido pirmo lapu
window.mainloop()