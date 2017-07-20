# SUMADORA-PYTHON
#Sumadora escrita en python 3
#!/usr/bin/env python3
"""
@author: ISC juan luis Ordoñez perez
"""
import tkinter as tk #importamos la lo libreria que nos permitira hacer una grafica
def suma():
    suma= int(entrada1.get())+int(entrada2.get())
    return var.set(suma)#fija el resultado de suma y lo manda  la variable
def cerrar():
    ventana.destroy()

ventana=tk.Tk()
ventana.title(" SUMA DE NUMEROS")
#anchoxalto en pixeles
ventana.geometry('380x300')
#color de fondo de la ventana
ventana.configure(background='dark turquoise')
var=tk.StringVar()#se declara la variable para poder imprimir el resultado



e1=tk.Label(ventana,text="Ingresa el numero 1: ", bg='gray',fg='white')
e1.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
entrada1=tk.Entry(ventana)
entrada1.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

e2=tk.Label(ventana,text="Ingresa el numero 2: ", bg='gray',fg='white')
e2.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
entrada2=tk.Entry(ventana)
entrada2.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

#programamos botones
botonsuma=tk.Button(ventana,text="suma",fg="blue",command=suma)
botonsuma.pack(side=tk.TOP)#dejamos en el centro

#programamos boton de salir del programa
botoncierra=tk.Button(ventana,text="cerrar",fg="blue",command=cerrar)
botoncierra.pack(side=tk.TOP)#dejamos en el centro


res=tk.Label(ventana,bg="plum",textvariable=var,padx=5,pady=5,width=50)#textvariable imprime la informacion segun sea la respuesta
res.pack() #se imprime el resultado



ventana.mainloop()

