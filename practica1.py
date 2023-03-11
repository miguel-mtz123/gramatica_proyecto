import tkinter as tk
from nltk.parse.generate import generate
from nltk.grammar import CFG
import tkinter.scrolledtext as scrolledtext
from tkinter import filedialog,END 
from tkinter.filedialog import asksaveasfilename
import nltk
import sys
from tkinter import messagebox as mb
from tkinter.messagebox import askyesno, askquestion
from tkinter import ttk

aplicacion1 = tk.Tk()
aplicacion1.geometry("400x300")
aplicacion1.title("Gramáticas")
init_dir='C:\\Users\\Miguel Martinez\\Desktop\\Gramáticas\\' # carpeta de gramaticas

def nueva_gramatica():
    t1.delete('1.0',END)
    global nombre_del_archivo     
    nombre_del_archivo='sin_titulo.txt' # nuevo nombre de archivo
    aplicacion1.title(nombre_del_archivo)

def abrir_gramatica():
    archivo = filedialog.askopenfilename(
        filetypes = [("Documentos de textos", ".txt")],
        defaultextension = ".txt",
        initialdir = init_dir,
        )
    if archivo: # si el usuario no ha cancelado el diálogo para guardar
        global nombre_del_archivo     
        nombre_del_archivo = archivo # establecer el nombre del archivo
        aplicacion1.title(nombre_del_archivo)    # actualizar el título de la interfaz
        fob = open(archivo,'r') # abrir en leer más
        my_str1 = fob.read() # leer datos de un archivo
        producciones = nltk.CFG.fromstring(my_str1)
        aplicacion1.gramatica = producciones
        #print(list(generate(producciones)))
        #mb.showinfo("Gramática", producciones.productions())
        t1.delete('1.0',END) # eliminar el contenido anterior 
        t1.insert(tk.END, my_str1) # añadir nuevos datos de un archivo a un cuadro de texto
        fob.close()
    else: # el usuario ha cancelado la operación
        mb.showinfo("Información", "No se ha seleccionado ningún archivo")

def guardar_gramatica():
    global nombre_del_archivo # recopilar el nombre del archivo
    if(nombre_del_archivo == 'sin_titulo.txt'): # si el nombre de archivo por defecto sigue ahí
        guardar_gramatica_como() # llama a la función
    else:
        fob=open(nombre_del_archivo,'w') # abierto en modo escritura
        my_str1=t1.get("1.0",END) # recopilar los datos del widget de texto
        fob.write(my_str1)  # escribir en el archivo

def guardar_gramatica_como():
    archivo = filedialog.asksaveasfilename(
        filetypes=[("Documentos de textos", ".txt")],
        defaultextension=".txt",initialdir=init_dir)
    if archivo: # si el usuario no ha cancelado el diálogo para guardar
        fob=open(archivo,'w') # abre el archivo en modo de escritura
        my_str1=t1.get("1.0",END) # recopilar datos del widget de texto
        producciones = nltk.CFG.fromstring(my_str1)
        fob.write(my_str1) # escribir en archivo
        global nombre_del_archivo
        nombre_del_archivo = archivo # establecer el nombre del archivo
        aplicacion1.title(nombre_del_archivo)    # actualizar el título de la interfaz
        #aplicacion1.title(archivo)  # Actualizar el título de la Interfaz con el nombre del archivo
        fob.close() # Cerrar el puntero del archivo
    else: # el usuario ha cancelado la operación
        mb.showinfo("Información", "No se ha guardado la gramática.")

def cerrar_gramatica():
    guardar_gramatica()  # guarda el archivo antes de cerrar el archivo
    t1.delete('1.0',END) # eliminar el contenido del widget de texto
    aplicacion1.title('') # eliminar el título de la Interfaz
    
def cerrar_programa(e):
    #cerrar_gramatica()
    pregunta = askyesno(title='Confirmar', message='¿Quiere guardar los cambios antes de salir?')
    if pregunta:
        cerrar_gramatica()
        aplicacion1.destroy()
    else:
        aplicacion1.destroy()

def guardar_g(e):
    guardar_gramatica()

def abrir_g(e):
    abrir_gramatica()

def nueva_g(e):
    nueva_gramatica()

def cerrar_g(e):
    cerrar_gramatica()

def confirmar():
    answer = askyesno(title='Confirmar', message='¿Quiere guardar los cambios antes de salir?')
    if answer:
        
        aplicacion1.destroy()

menubar = tk.Menu(aplicacion1)
my_font1=('Times',12,'bold')
menu_f = tk.Menu(menubar,title='my title',tearoff=0)

menubar.add_cascade(label="Archivo", menu=menu_f)

menu_f.add_command(label="Nuevo", command=lambda:nueva_gramatica())
menu_f.add_command(label="Abrir...", command=lambda:abrir_gramatica())  
menu_f.add_command(label="Guardar", command=lambda:guardar_gramatica())
menu_f.add_command(label="Guardar como...", command=lambda:guardar_gramatica_como())
menu_f.add_command(label="Cerrar gramática", command=lambda:cerrar_gramatica())
menu_f.add_separator()
menu_f.add_command(label="Salir", command=aplicacion1.quit)
aplicacion1.config(menu=menubar) # añadir menú a la ventana

t1 = tk.Text(aplicacion1, height=15, width=45) # se añade el cuadro de texto
t1.grid(row=0,column=0,padx=30,pady=20)

set_up_button = tk.Button(aplicacion1, height=1, width=10, text='Ask Yes/No', command=confirmar)
set_up_button.grid(row=1,column=0)
#nueva_gramatica()

#Bind the Keyboard shortcut Key
aplicacion1.bind('<Control-n>', nueva_g)
aplicacion1.bind('<Control-N>', nueva_g)
aplicacion1.bind('<Control-w>', cerrar_g)
aplicacion1.bind('<Control-W>', cerrar_g)
aplicacion1.bind('<Control-q>', cerrar_programa)
aplicacion1.bind('<Control-Q>', cerrar_programa)
aplicacion1.bind('<Control-s>', guardar_g)
aplicacion1.bind('<Control-o>', abrir_g)
aplicacion1.bind('<Control-O>', abrir_g)
aplicacion1.bind('<Control-Shift-S>', lambda e: guardar_g(e))
aplicacion1.mainloop()