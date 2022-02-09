import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
root.title("Primer programa!")

label = tk.Label(root, text="Holis", font=("Arial", 20), fg="red", bg='#0f0')
label.pack(padx=10, pady=10)

textbox = tk.Text(root, font=("Comic Sans MS", 20), height=3)
textbox.pack(padx=10, pady=10)

entries = tk.Entry(root, font=("Arial", 20))
entries.pack(padx=20, pady=20)

boton = tk.Button(root, text="Apretame", font=("Arial", 25))
boton.pack()

# TEMA GRID

botones = tk.Frame(root)
botones.columnconfigure(0, weight=1)
botones.columnconfigure(1, weight=1)
botones.columnconfigure(2, weight=1)

btn1 = tk.Button(botones, text="1", font=("Arial", 30))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(botones, text="2", font=("Arial", 30))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(botones, text="3", font=("Arial", 30))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(botones, text="4", font=("Arial", 30))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(botones, text="5", font=("Arial", 30))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(botones, text="6", font=("Arial", 30))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

botones.pack(fill='x')

# FIN GRID

otro_boton = tk.Button(root, text="Otro más", font=("Arial", 15))
otro_boton.place(x=50, y=210, height=50, width=100)

root.mainloop()
