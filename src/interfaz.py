import customtkinter as ctk
import tkinter as tk 
import ArangoDB as DB
from spinbox import FloatSpinbox

c_negro = '#010101'
c_gris = '#bbbbbb'
 
def initialize(db): 
    # Crear la ventana principal
    ventana = ctk.CTk()
    ventana.geometry("1000x600")
    ventana.title("IMDB")

    canvas = ctk.CTkCanvas(ventana, borderwidth=0, highlightthickness=0)

    # Crear un Frame para agregar el contenido
    frame = ctk.CTkFrame(canvas)
    frame.pack(fill='both', expand=True)

    #########Se añade el contenido de la ventana

    etiqueta = ctk.CTkLabel(frame, text="Introduce el filtrado que desees para buscar películas o series:", font=("Arial", 15))
    etiqueta.pack()

    filterFrame = ctk.CTkFrame(frame, fg_color = c_gris, height=300, width=800)

    # Mostrar el frame en la ventana
    filterFrame.pack(padx=10, pady=10)

    # Creamos los diferentes inputs

    
    # INPUT TITULO
    titleFrame = ctk.CTkFrame(filterFrame, bg_color= c_negro)
    titleFrame.pack(padx=10, pady=10, side="left")
    etiqueta = ctk.CTkLabel(titleFrame, text="Title:")
    etiqueta.pack()
    caja_texto = ctk.CTkEntry(titleFrame)
    caja_texto.pack(side="left")
    
    # INPUT DATE
    dateFrame = ctk.CTkFrame(filterFrame, bg_color= c_negro)
    dateFrame.pack(padx=10, pady=10, side="left")
    etiqueta = ctk.CTkLabel(dateFrame, text="Date:")
    etiqueta.pack()

    spinbox = FloatSpinbox(dateFrame, width=120, min_value=DB.minDate(db), max_value=DB.maxDate(db),  step_size=1)
    spinbox.pack(side="left")
    # INPUT RATE    
    rateFrame = ctk.CTkFrame(filterFrame, bg_color= c_negro)
    rateFrame.pack(padx=10, pady=10, side="left")
    etiqueta = ctk.CTkLabel(rateFrame, text="Min Rate:")
    etiqueta.pack()
    spinbox = FloatSpinbox(rateFrame, width=120, min_value=0.0, max_value=10.0,  step_size=0.1, esInt= False)
    spinbox.pack(side="left")

    # INPUT VOTES
    votesFrame = ctk.CTkFrame(filterFrame, bg_color= c_negro)
    votesFrame.pack(padx=10, pady=10, side="left")
    etiqueta = ctk.CTkLabel(votesFrame, text="Min Votes:")
    etiqueta.pack()
    spinbox = FloatSpinbox(votesFrame, width=120, min_value=DB.minVotes(db), max_value=1000000000, step_size=1000)
    spinbox.pack(side="left")
    
    # INPUT GENERO

    # Crear el frame (generos)
    genreFrame = ctk.CTkFrame(filterFrame, bg_color= c_negro)

    # Mostrar el frame (div) en la ventana
    genreFrame.pack(padx=10, pady=10, side="left")
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
    lista.pack(side="left")


    # # INPUT DURATION
    durationFrame = ctk.CTkFrame(filterFrame, bg_color= c_negro)
    durationFrame.pack(padx=10, pady=10, side="left")
    etiqueta = ctk.CTkLabel(durationFrame, text="Min Duration:")
    etiqueta.pack()
    spinbox = FloatSpinbox(durationFrame, width=120, min_value=DB.minDuration(db), max_value=DB.maxDuration(db),  step_size=30)
    spinbox.pack(side="left")


    # INPUT TYPE

    # Crear el frame (tipos)
    typeFrame = ctk.CTkFrame(filterFrame, bg_color= c_negro)
    typeFrame.pack(padx=10, pady=5, side="left")
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
    certificateFrame.pack(padx=10, pady=5, side="left")
    etiqueta = ctk.CTkLabel(certificateFrame, text="Certificate:")
    etiqueta.pack()

    certificateList = DB.certificateList(db)
    
    # Crear un Combobox y agregar las opciones
    combo = ctk.CTkComboBox(certificateFrame, values=certificateList)
    combo.pack(side="left")

    # INPUT EPISODES
    episodesFrame = ctk.CTkFrame(filterFrame, bg_color= c_negro)
    etiqueta_ep = ctk.CTkLabel(episodesFrame, text="Min Episodes:")
    spinbox_ep = FloatSpinbox(episodesFrame, width=120, min_value=DB.minEpisodes(db), max_value=DB.maxEpisodes(db),  step_size=5)

    


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
            episodesFrame.pack(padx=10, pady=10, side="left")
            etiqueta_ep.pack()
            spinbox_ep.pack(side="left")
        else:
            episodesFrame.pack_forget()
            etiqueta_ep.pack_forget()
            spinbox_ep.pack_forget()

    lista2.bind("<<ListboxSelect>>", mostrar_ocultar)

    #select/option ultimos 5 campos PRUEBA


    # Añadir un botón a la ventana
    boton = ctk.CTkButton(frame, text="Buscar")

    # Ubicar el botón en la ventana
    boton.pack(side="bottom", padx=10, pady=10)

    ########FIN CONTENIDO VENTANA

    # Crear una scrollbar vertical para el canvas
    scrollbar = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    canvas.create_window((0, 0), window=frame, anchor="nw")
    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

 
    ventana.mainloop()  
 
 