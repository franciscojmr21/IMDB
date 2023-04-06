import tkinter as tk


def inicializar():
    
    # Crear la ventana principal
    ventana = tk.Tk()

    #cambiar el logo de la ventana
    ventana.iconbitmap("imagenes/imdb.ico")


    ventana.title("IMDB")
    

    ventana.geometry("800x500")

    # Añadir un botón a la ventana
    boton = tk.Button(ventana, text="Haz clic aquí")

    # Ubicar el botón en la ventana
    boton.pack()

    # Iniciar el loop principal de la ventana
    ventana.mainloop()
