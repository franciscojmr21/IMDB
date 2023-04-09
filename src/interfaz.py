import tkinter as tk
from tkinter import ttk
import ArangoDB as DB




def initialize(db):   
    # Crear la ventana principal
    ventana = tk.Tk()

    #cambiar el logo de la ventana
    #ventana.iconbitmap("rimdb.ico")  NO VA OSTIA PUTA


    ventana.title("IMDB")
    
    # Cambiar el tamaño de la ventana
    ventana.geometry("800x500")

    # Creamos los diferentes inputs

    
    # INPUT TITULO
    etiqueta = tk.Label(ventana, text="Title:")
    etiqueta.pack()

    caja_texto = tk.Entry(ventana)
    caja_texto.pack()

    # INPUT DATE
    etiqueta = tk.Label(ventana, text="Date:")
    etiqueta.pack()
    
    spinbox = tk.Spinbox(ventana, from_=DB.minDate(db), to=DB.maxDate(db))
    spinbox.pack()

    # INPUT RATE
    etiqueta = tk.Label(ventana, text="Min Rate:")
    etiqueta.pack()
    spinbox = tk.Spinbox(ventana, from_=0.0, to=10.0, increment=0.1)
    spinbox.pack()

    # INPUT VOTES
    etiqueta = tk.Label(ventana, text="Min Votes:")
    etiqueta.pack()
    spinbox = tk.Spinbox(ventana, from_=DB.minVotes(db), to=1000000000, increment=1000)
    spinbox.pack()
    
    # INPUT GENERO

    # Crear el frame (generos)
    genreFrame = tk.Frame(ventana, bg="gray", bd=2)

    # Mostrar el frame (div) en la ventana
    genreFrame.pack(padx=10, pady=10)
    etiqueta = tk.Label(genreFrame, text="Genre:")
    etiqueta.pack()

    # Crear el botón de selección
    genreList = DB.genreList(db)
    lista = tk.Listbox(genreFrame, selectmode=tk.MULTIPLE)
    for genre in genreList:
        lista.insert(tk.END, genre)

    # Crear la barra de desplazamiento
    scrollbar = tk.Scrollbar(genreFrame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lista.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lista.yview)

    # Mostrar la lista de opciones en la ventana
    lista.pack()


    # INPUT DURATION

    etiqueta = tk.Label(ventana, text="Min Duration:")
    etiqueta.pack()
    spinbox = tk.Spinbox(ventana, from_=DB.minDuration(db), to=DB.maxDuration(db), increment=30)
    spinbox.pack()


    # INPUT TYPE pelis/series

    # Crear el frame (tipos)
    typeFrame = tk.Frame(ventana, bg="gray", bd=2)

    # Mostrar el frame (div) en la ventana
    typeFrame.pack(padx=10, pady=5)

    etiqueta = tk.Label(typeFrame, text="Type:")
    etiqueta.pack()

    # Crear el botón de selección
    typeList = DB.typeList(db)
    lista2 = tk.Listbox(typeFrame, selectmode=tk.MULTIPLE)
    for type in typeList:
        lista2.insert(tk.END, type)

    # Crear la barra de desplazamiento
    scrollbar = tk.Scrollbar(typeFrame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lista2.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lista.yview)

    # Mostrar la lista de opciones en la ventana
    

    lista2.pack()




    # INPUT CERTIFICATE

    # Crear el frame (certificate)
    certificateFrame = tk.Frame(ventana, bg="gray", bd=2)

    # Mostrar el frame (div) en la ventana
    certificateFrame.pack(padx=10, pady=5)

    etiqueta = tk.Label(certificateFrame, text="Certificate:")
    etiqueta.pack()

    certificateList = DB.certificateList(db)
    
    # Crear un Combobox y agregar las opciones
    combo = ttk.Combobox(certificateFrame, values=certificateList)
    combo.pack()

    # INPUT EPISODES
    etiqueta_ep = tk.Label(ventana, text="Min Episodes:")
    spinbox_ep = tk.Spinbox(ventana, from_=DB.minEpisodes(db), to=DB.maxEpisodes(db), increment=5)
    
    # Función para mostrar u ocultar un elemento
    def mostrar_ocultar(valor):
        val_serie = 0
        serie_selcted = False
    
        for i in range(lista2.size()):
            if(lista2.get(i) == "Series"):
                val_serie = i

        if(len(lista2.curselection())>=1):
            if val_serie in lista2.curselection():
                serie_selcted = True
        print("serie",serie_selcted)
        
        if(serie_selcted and len(lista2.curselection())==1):
            print("entra1")
            etiqueta_ep.pack()
            spinbox_ep.pack()
        else:
            print("entra2")
            etiqueta_ep.pack_forget()
            spinbox_ep.pack_forget()




    lista2.bind("<<ListboxSelect>>", mostrar_ocultar)



#select/option ultimos 5 campos PRUEBA

    
    # Crear un botón para refrescar la ventana
    boton = tk.Button(ventana, text="Refrescar")

    # Definir una función que actualice la ventana
    def refrescar():
        ventana.update()

    # Vincular la función al evento clic del botón
    boton.config(command=refrescar)

    # Empaquetar el botón en la ventana
    boton.pack()

    # Añadir un botón a la ventana
    boton = tk.Button(ventana, text="Buscar")

    # Ubicar el botón en la ventana
    boton.pack()

    # Iniciar el loop principal de la ventana
    ventana.mainloop()













