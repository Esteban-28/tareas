import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x300")

txt1 = tkinter.Entry(ventana)
txt2 = tkinter.Entry(ventana)
etiqueta = tkinter.Label(ventana)

def sum():
    t1 = txt1.get()
    t2 = txt2.get()
    etiqueta["text"] = int(t1) + int(t2)

boton = tkinter.Button(ventana, text="suma", command=sum)

boton.pack()
txt1.pack()
txt2.pack()
etiqueta.pack()

ventana.mainloop()