import customtkinter as ctk
import tkinter as tk 
import ArangoDB as DB
from spinbox import FloatSpinbox
from listBox import CTkListbox
from table import CTkTable
import re

c_negro = '#010101'
c_gris = '#bbbbbb'
all_selected_genres = False
all_selected_types = False
resultTable = None

def initialize(db, databaseName): 
    # Crear la ventana principal
    ventana = ctk.CTk()
    ventana.geometry("1300x650")
    ventana.title(databaseName)

    canvas = ctk.CTkCanvas(ventana, borderwidth=0, highlightthickness=0)

    # Crear un Frame para agregar el contenido
    frame = ctk.CTkFrame(canvas)

    resulFrame = ctk.CTkFrame(canvas)

    etiqueta = ctk.CTkLabel(resulFrame, text="Resultado de la busqueda: ", font=("Arial", 15))
    etiqueta.pack()

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
    title = ctk.CTkLabel(titleFrame, text="Title:")
    title.pack()
    caja_texto_title = ctk.CTkEntry(titleFrame)
    caja_texto_title.pack(side="left")

    #SpinBox FRAME
    spinBoxFrame = ctk.CTkFrame(filterFrame)
    spinBoxFrame.pack(side="left")
    
    # INPUT DATE
    dateFrame = ctk.CTkFrame(spinBoxFrame, bg_color= c_negro)
    dateFrame.grid(padx=10, pady=10, row=0, column=0)
    etiqueta = ctk.CTkLabel(dateFrame, text="Date:")
    etiqueta.pack()

    spinbox_date = FloatSpinbox(dateFrame, width=120, min_value=DB.minDate(db), max_value=DB.maxDate(db),  step_size=1)
    spinbox_date.pack()

    # INPUT RATE    
    rateFrame = ctk.CTkFrame(spinBoxFrame, bg_color= c_negro)
    rateFrame.grid(padx=10, pady=10, row=0, column=1)
    etiqueta = ctk.CTkLabel(rateFrame, text="Min Rate:")
    etiqueta.pack()
    spinbox_rate = FloatSpinbox(rateFrame, width=120, min_value=0.0, max_value=10.0,  step_size=0.1, esInt= False)
    spinbox_rate.pack()

    # INPUT VOTES
    votesFrame = ctk.CTkFrame(spinBoxFrame, bg_color= c_negro)
    votesFrame.grid(padx=10, pady=10, row=1, column=0)
    etiqueta = ctk.CTkLabel(votesFrame, text="Min Votes:")
    etiqueta.pack()
    spinbox_votes = FloatSpinbox(votesFrame, width=120, min_value=DB.minVotes(db), max_value=1000000000, step_size=1000)
    spinbox_votes.pack()
    
    # # INPUT DURATION
    durationFrame = ctk.CTkFrame(spinBoxFrame, bg_color= c_negro)
    durationFrame.grid(padx=10, pady=10, row=1, column=1)
    etiqueta = ctk.CTkLabel(durationFrame, text="Min Duration:")
    etiqueta.pack()
    spinbox_duration = FloatSpinbox(durationFrame, width=120, min_value=DB.minDuration(db), max_value=DB.maxDuration(db),  step_size=30)
    spinbox_duration.pack()

    
    # INPUT EPISODES
    episodesFrame = ctk.CTkFrame(spinBoxFrame, bg_color= c_negro)
    etiqueta_ep = ctk.CTkLabel(episodesFrame, text="Min Episodes:")
    spinbox_ep = FloatSpinbox(episodesFrame, width=120, min_value=DB.minEpisodes(db), max_value=DB.maxEpisodes(db),  step_size=5)

    
    # INPUT GENERO

    # Crear el frame (generos)
    genreFrame = ctk.CTkFrame(filterFrame, bg_color= c_negro)

    # Mostrar el frame (div) en la ventana
    genreFrame.pack(padx=10, pady=10, side="left")
    etiqueta = ctk.CTkLabel(genreFrame, text="Genre:")
    etiqueta.pack()

    all_button_genre = ctk.CTkButton(genreFrame, text="Select ALL")
    all_button_genre.pack()

    # Crear el botón de selección
    genreList = DB.genreList(db)
    lista_genre = CTkListbox(genreFrame, selectmode=tk.MULTIPLE, exportselection=False)
    for genre in genreList:
        lista_genre.insert(tk.END, genre)

    # Crear la barra de desplazamiento
    scrollbar = ctk.CTkScrollbar(genreFrame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lista_genre.config(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lista_genre.yview)

    # Mostrar la lista de opciones en la ventana
    lista_genre.pack()

    # INPUT TYPE

    # Crear el frame (tipos)
    typeFrame = ctk.CTkFrame(filterFrame, bg_color= c_negro)
    typeFrame.pack(padx=10, pady=5, side="left")
    etiqueta = ctk.CTkLabel(typeFrame, text="Type:")
    etiqueta.pack()

    all_button_type = ctk.CTkButton(typeFrame, text="Select ALL")
    all_button_type.pack()

    # Crear el botón de selección
    typeList = DB.typeList(db)
    lista_type = CTkListbox(typeFrame, selectmode=tk.MULTIPLE, exportselection=False)
    for type in typeList:
        lista_type.insert(tk.END, type)

    # Crear la barra de desplazamiento
    typeScrollbar = ctk.CTkScrollbar(typeFrame)
    typeScrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lista_type.config(yscrollcommand=typeScrollbar.set)
    typeScrollbar.configure(command=lista_type.yview)

    # Mostrar la lista de opciones en la ventana
    lista_type.pack()

    #COMBO FRAME
    comboFrame = ctk.CTkFrame(filterFrame)
    comboFrame.pack(side="left")

    # INPUT CERTIFICATE

    # Crear el frame (certificate)
    certificateFrame = ctk.CTkFrame(comboFrame, bg_color= c_negro)
    certificateFrame.grid(padx=10, pady=5, row=0, column=0)
    etiqueta = ctk.CTkLabel(certificateFrame, text="Certificate:")
    etiqueta.pack()

    certificateList = DB.certificateList(db)
    
    # Crear un Combobox y agregar las opciones
    combo_certificate = ctk.CTkComboBox(certificateFrame, values=certificateList)
    combo_certificate.pack()

    # INPUT NUDITY

    nudityFrame = ctk.CTkFrame(comboFrame, bg_color=c_negro)
    nudityFrame.grid(padx=10, pady=10, row=0, column=1)
    etiqueta = ctk.CTkLabel(nudityFrame, text="Nudity:")
    etiqueta.pack()

    nudityList = DB.nudityList(db)

    # Crear un Combobox y agregar las opciones
    combo_nudity = ctk.CTkComboBox(nudityFrame, values=nudityList)
    combo_nudity.pack()


    # INPUT VIOLENCE

    violenceFrame = ctk.CTkFrame(comboFrame, bg_color=c_negro)
    violenceFrame.grid(padx=10, pady=10, row=1, column=0)
    etiqueta = ctk.CTkLabel(violenceFrame, text="Violence:")
    etiqueta.pack()

    violenceList = DB.violenceList(db)

    # Crear un Combobox y agregar las opciones
    combo_violence = ctk.CTkComboBox(violenceFrame, values=violenceList)
    combo_violence.pack()


    # INPUT PROFANITY

    profanityFrame = ctk.CTkFrame(comboFrame, bg_color=c_negro)
    profanityFrame.grid(padx=10, pady=10,row=1, column=1)
    etiqueta = ctk.CTkLabel(profanityFrame, text="Profanity:")
    etiqueta.pack()

    profanityList = DB.profanityList(db)

    # Crear un Combobox y agregar las opciones
    combo_profanity = ctk.CTkComboBox(profanityFrame, values=profanityList)
    combo_profanity.pack()


    # INPUT ALCOHOL

    alcoholFrame = ctk.CTkFrame(comboFrame, bg_color=c_negro)
    alcoholFrame.grid(padx=10, pady=10, row=0, column=2)
    etiqueta = ctk.CTkLabel(alcoholFrame, text="Alcohol:")
    etiqueta.pack()

    alcoholList = DB.alcoholList(db)

    # Crear un Combobox y agregar las opciones
    combo_alcohol = ctk.CTkComboBox(alcoholFrame, values=alcoholList)
    combo_alcohol.pack()


    # INPUT FRIGHTENING

    frighteningFrame = ctk.CTkFrame(comboFrame, bg_color=c_negro)
    frighteningFrame.grid(padx=10, pady=10, row=1, column=2)
    etiqueta = ctk.CTkLabel(frighteningFrame, text="Frightening:")
    etiqueta.pack()

    frighteningList = DB.frighteningList(db)

    # Crear un Combobox y agregar las opciones
    combo_frightening = ctk.CTkComboBox(frighteningFrame, values=frighteningList)
    combo_frightening.pack()

# FUNCIONES AUXILIARES

    def getAllValues(db, databaseName):
        Title = caja_texto_title.get()
        
        Date = spinbox_date.getInt()
        if(Date>DB.maxDate(db)):
            Date = DB.maxDate(db)
            spinbox_date.setInt(DB.maxDate(db))
        elif(Date<DB.minDate(db)):
            Date = DB.minDate(db)
            spinbox_date.setInt(DB.minDate(db))

        Rate = spinbox_rate.getFloat()
        if(Rate>10.0):
            Rate = 10.0
            spinbox_rate.setFloat(10.0)
        elif(Rate<0.0):
            Rate = 0.0
            spinbox_rate.setFloat(0.0)

        Votes = spinbox_votes.getInt()
        if(Votes<DB.minVotes(db)):
            Votes = DB.minVotes(db)
            spinbox_votes.setInt(DB.minVotes(db))

        Genre = []
        for i in range(lista_genre.size()):
            if(lista_genre.selection_includes(i)):
                Genre.append(lista_genre.get(i))

        Duration = spinbox_duration.getInt()
        if(Duration>DB.maxDuration(db)):
            Duration = DB.maxDuration(db)
            spinbox_duration.setInt(DB.maxDuration(db))
        elif(Duration<DB.minDuration(db)):
            Duration = DB.minDuration(db)
            spinbox_duration.setInt(DB.minDuration(db))

        Type = []
        for i in range(lista_type.size()):
            if(lista_type.selection_includes(i)):
                Type.append(lista_type.get(i))
            lista_type.curselection()
        Certificate = combo_certificate.get()

        Episodes = spinbox_ep.getInt()
        if(Episodes>DB.maxEpisodes(db)):
            Episodes = DB.maxEpisodes(db)
            spinbox_ep.setInt(DB.maxEpisodes(db))
        elif(Episodes<DB.minEpisodes(db)):
            Episodes = DB.minEpisodes(db)
            spinbox_ep.setInt(DB.minEpisodes(db))

        Nudity = combo_nudity.get()
        Violence = combo_violence.get()
        Profanity = combo_profanity.get()
        Alcohol = combo_alcohol.get()
        Frightening = combo_frightening.get()
        etiquetaResult = ctk.CTkLabel(resulFrame, text="No se ha encontrado ningún resultado en la búsqueda", font=("Arial", 15))
        results = DB.consulta(db, Title, Date, Rate, Votes, Duration, Episodes, Genre, Type, Certificate, Nudity, Alcohol, Violence, Profanity, Frightening, databaseName)
        headers = ["Title", "Date", "Rate", "Votes", "Categories", "Duration", "Type", "Certificate", "Episodes", "Nudity", "Violence", "Profanaty", "Alcohol", "Frightering"]
        resulFrame.grid(row=1, column=0)
        
        if (len(results) < 1):
            print("puta madre")
            #resulFrame.grid(row=1, column=0)
            etiquetaResult.pack()
        
        else:
            etiquetaResult.pack_forget()
            # Crear la tabla
            global resultTable
            if(resultTable != None):
                resultTable.remove_table()
            #resulFrame.grid(row=1, column=0)
            resultTable = CTkTable(resulFrame, headers, results)
        

    def combobox_callback(choice):
        print("combobox dropdown clicked:", choice)

    def select_all_type(valor):
        global all_selected_types
        if(not all_selected_types):
            all_selected_types = True
            for i in range(lista_type.size()):
                lista_type.select_set(i)
        elif(all_selected_types):
            all_selected_types = False
            for i in range(lista_type.size()):
                lista_type.select_clear(i)

    def select_all_genre(valor):
        global all_selected_genres
        if(not all_selected_genres):
            all_selected_genres = True
            for i in range(lista_genre.size()):
                lista_genre.select_set(i)
        elif(all_selected_genres):
            all_selected_genres = False
            for i in range(lista_genre.size()):
                lista_genre.select_clear(i)

    # Función para mostrar u ocultar un elemento
    def mostrar_ocultar(valor):
        val_serie = 0
        serie_selcted = False

        for i in range(lista_type.size()):
            if(lista_type.get(i) == "Series"):
                val_serie = i

        if(len(lista_type.curselection())>=1):
            if val_serie in lista_type.curselection():
                serie_selcted = True
        
        if(serie_selcted and len(lista_type.curselection())==1):
            episodesFrame.grid(padx=10, pady=10, row=0, column=2)
            etiqueta_ep.pack()
            spinbox_ep.pack()
        else:
            episodesFrame.grid_forget()
            etiqueta_ep.pack_forget()
            spinbox_ep.pack_forget()
        
    lista_type.bind("<<ListboxSelect>>", mostrar_ocultar)
    all_button_type.bind("<Button-1>", select_all_type)
    all_button_genre.bind("<Button-1>", select_all_genre)

    #select/option ultimos 5 campos PRUEBA


    # Añadir un botón a la ventana
    boton = ctk.CTkButton(frame, text="Buscar", command=lambda: getAllValues(db, databaseName))

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

    
    frame.grid(row=0, column=0)

    ventana.mainloop()  