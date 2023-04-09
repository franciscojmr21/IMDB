import ArangoDB as DB
import tkinter as tk
import customtkinter as ctk
from spinbox import FloatSpinbox

c_negro = '#010101'
c_gris = '#bbbbbb'


def main():
    initialize()






def initialize(db):   
    # Crear la ventana principal
    ventana = ctk.CTk()

    #cambiar el logo de la ventana  NO FUNCIONA
    #ventana.iconbitmap("imdb.ico")  
    #logo = PhotoImage(file = 'imdb.png')
    #ventana.call('wm', 'iconphoto', ventana._w, logo)


    ventana.title("IMDB")
    
    # Cambiar el tamaño de la ventana
    ventana.geometry("1000x600")

    ventana.grid_rowconfigure((0,1), weight=1)
    ventana.grid_columnconfigure(0, weight=1)

    etiqueta = ctk.CTkLabel(ventana, text="Introduce el filtrado que desees para buscar películas o series:", font=("Arial", 15))
    etiqueta.pack()

    filterFrame = ctk.CTkFrame(ventana, fg_color = c_gris, height=300, width=800)

    # Mostrar el frame en la ventana
    filterFrame.pack(padx=10, pady=10)


    # Creamos los diferentes inputs

    
    # INPUT TITULO
    etiqueta = ctk.CTkLabel(filterFrame, text="Title:")
    etiqueta.pack()

    caja_texto = ctk.CTkEntry(filterFrame)
    caja_texto.pack()

    # INPUT DATE
    etiqueta = ctk.CTkLabel(filterFrame, text="Date:")
    etiqueta.pack()
    
    spinbox = FloatSpinbox(filterFrame, width=120, min_value=DB.minDate(db), max_value=DB.maxDate(db),  step_size=1)
    spinbox.pack()
    

    # INPUT RATE    
    etiqueta = ctk.CTkLabel(filterFrame, text="Min Rate:")
    etiqueta.pack()
    spinbox = FloatSpinbox(filterFrame, width=120, min_value=0.0, max_value=10.0,  step_size=0.1, esInt= False) # AJUSTAR
    spinbox.pack()

    # INPUT VOTES
    etiqueta = ctk.CTkLabel(filterFrame, text="Min Votes:")
    etiqueta.pack()
    spinbox = FloatSpinbox(filterFrame, width=120, min_value=DB.minVotes(db), max_value=1000000000, step_size=1000)
    spinbox.pack()
    
    # INPUT GENERO

    # Crear el frame (generos)
    genreFrame = ctk.CTkFrame(filterFrame, bg_color= c_negro)

    # Mostrar el frame (div) en la ventana
    genreFrame.pack(padx=10, pady=10)
    etiqueta = ctk.CTkLabel(genreFrame, text="Genre:")
    etiqueta.pack()

    # Crear el botón de selección
    genreList = genreList = DB.genreList(db)
    lista = tk.Listbox(genreFrame, selectmode=tk.MULTIPLE)
    for genre in genreList:
        lista.insert(tk.END, genre)

    # Crear la barra de desplazamiento
    scrollbar = ctk.CTkScrollbar(genreFrame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lista.config(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lista.yview)

    # Mostrar la lista de opciones en la ventana
    lista.pack()


    # # INPUT DURATION

    etiqueta = ctk.CTkLabel(filterFrame, text="Min Duration:")
    etiqueta.pack()
    spinbox = FloatSpinbox(filterFrame, width=120, min_value=DB.minDuration(db), max_value=DB.maxDuration(db),  step_size=30)
    spinbox.pack()


    # INPUT TYPE

    # Crear el frame (tipos)
    typeFrame = ctk.CTkFrame(filterFrame, bg_color= c_negro)

    # Mostrar el frame (div) en la ventana
    typeFrame.pack(padx=10, pady=5)

    etiqueta = ctk.CTkLabel(typeFrame, text="Type:")
    etiqueta.pack()

    # Crear el botón de selección
    typeList = DB.typeList(db)
    lista2 = tk.Listbox(typeFrame, selectmode=tk.MULTIPLE)
    for type in typeList:
        lista2.insert(tk.END, type)

    # Crear la barra de desplazamiento
    scrollbar = ctk.CTkScrollbar(typeFrame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lista2.config(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lista.yview)

    # Mostrar la lista de opciones en la ventana
    lista2.pack()

    # INPUT CERTIFICATE

    # Crear el frame (certificate)
    certificateFrame = ctk.CTkFrame(filterFrame, bg_color= c_negro)

    # Mostrar el frame (div) en la ventana
    certificateFrame.pack(padx=10, pady=5)

    etiqueta = ctk.CTkLabel(certificateFrame, text="Certificate:")
    etiqueta.pack()

    certificateList = DB.certificateList(db)
    
    # Crear un Combobox y agregar las opciones
    combo = ctk.CTkComboBox(ventana, values=certificateList)
    combo.pack()

    # INPUT EPISODES
    etiqueta_ep = ctk.CTkLabel(filterFrame, text="Min Episodes:")
    spinbox_ep = FloatSpinbox(filterFrame, width=120, min_value=DB.minEpisodes(db), max_value=DB.maxEpisodes(db),  step_size=5)
    


# FUNCIONES AUXILIARES



    def combobox_callback(choice):
        print("combobox dropdown clicked:", choice)



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
        
        if(serie_selcted and len(lista2.curselection())==1):
            etiqueta_ep.pack()
            spinbox_ep.pack()
        else:
            etiqueta_ep.pack_forget()
            spinbox_ep.pack_forget()




    lista2.bind("<<ListboxSelect>>", mostrar_ocultar)



#select/option ultimos 5 campos PRUEBA


    # Añadir un botón a la ventana
    boton = ctk.CTkButton(filterFrame, text="Buscar")

    # Ubicar el botón en la ventana
    boton.pack()

    # Iniciar el loop principal de la ventana
    ventana.mainloop()




if __name__ == "__main__":
    main()








