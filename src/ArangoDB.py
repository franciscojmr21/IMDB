from pyArango.connection import *
from pyArango.collection import Collection, Field
import csv


def connect():
    # Establecer conexión con ArangoDB
    conn = Connection(arangoURL='http://localhost:8529', username='root', password='root')
    return conn  

def create(conn):

    # Crear una nueva base de datos en caso de que no este ya creada
    if not conn.hasDatabase('IMDB'):
        db = conn.createDatabase(name='IMDB')
        print(f'Se ha creado la base de datos IMDB.')
    else:
        db = conn['IMDB']
        print(f'La base de datos IMDB ya existe.')


    # Crear una nueva colección en caso de que no este ya creada
    if not db.hasCollection("seriesYPeliculas"):
        db.createCollection(name="seriesYPeliculas")
        print(f'Se ha creado la colección seriesYPeliculas.')
    else:
        print(f'La colección seriesYPeliculas ya existe.')

    return db



def loadData(db):

    collection = db["seriesYPeliculas"]
    
    

    # Abrir el archivo CSV
    print('Cargando datos...')
    with open('../dataset/imdb.csv', encoding='utf-8', newline='') as archivo_csv:
        # Crear un objeto reader de CSV
        lector_csv = csv.reader(archivo_csv, delimiter=',')
        
        # Saltar la primera fila del archivo CSV (encabezados de columna)
        next(lector_csv)
        
        # Iterar sobre las filas del archivo CSV
        for fila in lector_csv:
            
            # Creamos un nuevo documento para cada fila leida
            data = collection.createDocument()

            data['Name'] = fila[0]
            data['Date'] = fila[1]
            data['Rate'] = fila[2]
            data['Votes'] = fila[3]
            data['Genre'] = fila[4]
            data['Duration'] = fila[5]
            data['Type'] = fila[6]
            data['Certificate'] = fila[7]
            data['Episodes'] = fila[8]
            data['Nudity'] = fila[9]
            data['Violence'] = fila[10]
            data['Profanity'] = fila[11]
            data['Alcohol'] = fila[12]
            data['Frightening'] = fila[13]

            # Insertar el nuevo documento en la colección
            data.save()

    print('Datos cargados.')




