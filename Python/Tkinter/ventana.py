from cProfile import label
from cgitb import text
from tkinter import *
import os.path
#crear la ventana raiz

root = Tk()
root.title("Agenda de Contactos")

#comprobar si existe un archivo
rutaIco = os.path.abspath('./image/agenda.ico')

if not os.path.isfile(rutaIco):
    rutaIco = os.path.abspath('./Python/Tkinter/image/agenda.ico')

root.iconbitmap(rutaIco)

texto = Label(root,text = rutaIco)
texto.pack()

root.mainloop()