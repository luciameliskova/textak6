import tkinter

okno = tkinter.Tk()

#definujeme funkciu, ktora vie printnut nacitany text
def zobraz_text():
    txt = open("/Users/lucka/Desktop/textak.txt")
    y = txt.read()
    print(y)

#vytvorime tlacitko, ktore ked stlacim spusti funkciu, ktora
#printuje nas text
tlacitko = tkinter.Button(okno,text = "tlacitko", command = zobraz_text)
tlacitko.pack()

okno.mainloop()
