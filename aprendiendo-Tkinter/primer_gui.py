'''
Este ejemplo lo saqué del youtube de NeuralNine:
https://www.youtube.com/watch?v=ibf5cx221hk&ab_channel=NeuralNine
'''

import tkinter as tk
from tkinter import messagebox


class MyGUI:

    def __init__(self) -> None:

        self.root = tk.Tk()
        self.root.geometry('800x600')

        #! Armando menú de barrita!

        self.menubar = tk.Menu(self.root)

        # tearoff=0 es para que no aparezca una linea medio molesta
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        # En command le ponés qué función querés que ejecute el botón
        self.filemenu.add_command(label="Cerrar", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Cerrar sin preguntar", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(
            label='Mostrar mensajito', command=self.show_message)

        self.menubar.add_cascade(menu=self.filemenu, label='Archivo')
        self.menubar.add_cascade(menu=self.actionmenu, label='Acción')

        self.root.config(menu=self.menubar)

        #! Fin menú

        self.label = tk.Label(self.root, text='Mensaje..', font=('Arial', 20))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 20))
        self.textbox.pack(padx=10, pady=10)

        self.estado = tk.IntVar()

        # el valor 0 o 1 lo guarda en la variable seleccionada, que hay que definir previamente
        self.check = tk.Checkbutton(self.root, text='Mostrar mensajito', font=(
            'Arial', 15), variable=self.estado)
        self.check.pack(padx=10, pady=10)

        self.btn = tk.Button(self.root, height=1, width=10,
                             text='OK', font=('Arial', 15), command=self.show_message)
        self.btn.pack(padx=10, pady=10)

        # Esto es para que ejecute la funcion on_closing cuando aprietes la X de cerrar ventana
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Esta linea va siempre!
        self.root.mainloop()

    def show_message(self):
        if self.estado.get():  # para poder leer el resultado de la variable estado es necesario usar el método .get()
            print('No está chequeado')
            # Para hacer aparecer el messagebox hay que importarlo! y luego usar el método .showinfo
            messagebox.showinfo(
                title='Mensaje', message=self.textbox.get('1.0', tk.END))  # Esta es la forma de agarrar desde el inicio hasta el final de una textbox!
        else:
            print("Está chequeado")
            print(self.textbox.get('1.0', tk.END))

    def on_closing(self):
        if messagebox.askyesno(title='Salir?!', message='Te querés rajar amigo?'):
            self.root.destroy()  # Función que termina el programa


MyGUI()
