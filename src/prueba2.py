import ArangoDB as DB
import customtkinter as ctk
from PyQt5.QtWidgets import QComboBox, QApplication, QMainWindow, QScrollArea, QWidget, QVBoxLayout, QLabel, QFrame, QSpinBox, QPushButton, QListWidget, QListWidgetItem, QDoubleSpinBox

c_negro = '#010101'
c_gris = '#bbbbbb'

def initialize(db): 

    # Crear la aplicación y la ventana principal
    app = QApplication([])
    ventana = QMainWindow()
    ventana.setWindowTitle("IMDB")
    ventana.setGeometry(100, 100, 1000, 600)

    # Crear un objeto QScrollArea y un widget contenedor
    scroll = QScrollArea()
    widget = QWidget()

    # Cambiar el widget principal de la aplicación al QScrollArea
    ventana.setCentralWidget(scroll)

    # Agregar el widget contenedor al QScrollArea
    scroll.setWidget(widget)
    scroll.setWidgetResizable(True)

    # Crear un layout vertical dentro del widget contenedor
    layout = QVBoxLayout(widget)

    # Agregar la etiqueta y el frame de filtros al layout
    etiqueta = QLabel(widget, text="Introduce el filtrado que desees para buscar películas o series:")
    layout.addWidget(etiqueta)
    filterFrame = QFrame()
    layout.addWidget(filterFrame)

    # Agregar los diferentes inputs al frame de filtros
    etiqueta = QLabel(filterFrame, text="Title:")
    layout.addWidget(etiqueta)

    etiqueta = QLabel(filterFrame, text="Date:")
    layout.addWidget(etiqueta)
    spinbox = QSpinBox(filterFrame, width=120, minimum=DB.minDate(db), maximum=DB.maxDate(db),  singleStep=1)
    layout.addWidget(spinbox)

    etiqueta = QLabel(filterFrame, text="Min Rate:")
    layout.addWidget(etiqueta)
    spinbox = QSpinBox(filterFrame, width=120, minimum=0.0, maximum=10.0,  singleStep=0.1) # AJUSTAR
    layout.addWidget(spinbox)

    etiqueta = QLabel(filterFrame, text="Min Votes:")
    layout.addWidget(etiqueta)
    spinbox = QSpinBox(filterFrame, width=120, minimum=DB.minVotes(db), maximum=1000000000, singleStep=1000)
    layout.addWidget(spinbox)

    # Crear el frame de géneros y agregar la barra de desplazamiento
    genreFrame = QFrame(filterFrame)
    genreFrame.setStyleSheet("background-color: #010101;")
    etiqueta = QLabel(genreFrame, text="Genre:")
    layout.addWidget(spinbox)
    genreList = genreList = DB.genreList(db)
    lista = QListWidget(genreFrame)
    for genre in genreList:
        item = QListWidgetItem(genre)
        lista.addItem(item)
    scrollbar = QScrollArea(genreFrame) 
    layout.addWidget(lista)

    # # INPUT DURATION

    etiqueta = QLabel(filterFrame, text="Min Duration:")
    layout.addWidget(etiqueta)
    spinbox = QDoubleSpinBox(filterFrame, width=120, minimum=DB.minDuration(db), maximum=DB.maxDuration(db))
    layout.addWidget(spinbox)

    # INPUT TYPE

    # Crear el frame (tipos)
    typeFrame = QFrame(filterFrame)
    typeFrame.setStyleSheet("background-color: #010101;")

    etiqueta = QLabel(typeFrame, text="Type:")
    layout.addWidget(etiqueta)

    # Crear el botón de selección
    typeList = DB.typeList(db)
    lista2 = QListWidget(typeFrame)
    for type in typeList:
        lista2.addItem(type)

    # Crear la barra de desplazamiento
    scrollbar = QScrollArea(typeFrame)

    # Mostrar la lista de opciones en la ventana
    layout.addWidget(lista2)

    # Crear el frame (certificate)
    certificateFrame = QFrame(filterFrame)
    certificateFrame.setStyleSheet("background-color: #010101;")

    etiqueta = QLabel(certificateFrame, text="Certificate:")
    layout.addWidget(etiqueta)

    certificateList = DB.certificateList(db)

    # Crear un Combobox y agregar las opciones
    combo = QComboBox(certificateFrame, values=certificateList)
    layout.addWidget(combo)

    # Crear un botón de búsqueda
    boton_buscar = QPushButton(ventana, text="Buscar", bg_color = c_gris, command=lambda: search(db, caja_texto.get(), spinbox.get(), spinbox_2.get(), lista.get(0, tk.END), spinbox_3.get(), lista2.get(0, tk.END), combo.get()))
    layout.addWidget(boton_buscar)

    # Cerrar la conexión a la base de datos
    db.close()

    ventana.mainloop()

if __name__ == "__main__":
    main()
