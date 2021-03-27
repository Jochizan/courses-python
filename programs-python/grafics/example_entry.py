from tkinter import *

raiz=Tk()
miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)
cuadroApellido.config(fg="red", justify="center")

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, padx=10, pady=10)

scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
# para colocar el scrollbar usamos:
scrollVert.grid(row=4, column=2, sticky="nsew")
# como scrollVert recien se define en las 3 lineas anteriores la configuración de texto comentario debe ir después.
textoComentario.config(yscrollcommand=scrollVert.set)

nameLabel=Label(miFrame, text="Nombre: ")
nameLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

passLabel=Label(miFrame, text="Password: ")
passLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10) # Aquí esta la muestra de como se usa las filas 
# y columnas en los labels y sticky para la alineación de los mismos.

direccionLabel=Label(miFrame, text="Direccion de casa: ")
direccionLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Direccion de casa: ")
comentariosLabel.grid(row=4, column=0, sticky="w", padx=10, pady=10)

def codigoBoton():
    minombre.set("Juan")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()