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

            if fila[3] == 'No Votes':
                data['Votes'] = 0
            else:
                data['Votes'] = int(fila[3].replace(",", ""))

            data['Genre'] = fila[4]

            if fila[5] == 'None':
                data['Duration'] = 0
            else:
                data['Duration'] = int(fila[5])

            data['Type'] = fila[6]
            data['Certificate'] = fila[7]
            
            if fila[8] == '-':
                data['Episodes'] = 0
            else:
                data['Episodes'] = int(fila[8])

            data['Nudity'] = fila[9]
            data['Violence'] = fila[10]
            data['Profanity'] = fila[11]
            data['Alcohol'] = fila[12]
            data['Frightening'] = fila[13]

            # Insertar el nuevo documento en la colección
            data.save()

    print('Datos cargados.')


def minDate(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Date"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    min_value = min(cursor.result)

    return int(min_value)


def maxDate(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Date"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    max_value = max(cursor.result)

    return int(max_value)

def minVotes(db):   

    query = "FOR doc IN seriesYPeliculas RETURN doc.Votes"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    min_value = min(cursor.result)

    return min_value

def genreList(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Genre"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    genre = []
    for i in cursor.result:
        generos= i.split(",")
        for j in generos:
            if j not in genre:
                genre.append(j)

    return sorted(genre)

def typeList(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Type"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    type = []
    for i in cursor.result:
        if i not in type:
            type.append(i)

    return sorted(type)


def certificateList(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Certificate"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    certificate = []
    for i in cursor.result:
        if i not in certificate:
            certificate.append(i)

    return sorted(certificate)

def minDuration(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Duration"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    min_value = min(cursor.result)

    return min_value

def maxDuration(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Duration"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    max_value = max(cursor.result)

    return max_value
    
def minEpisodes(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Episodes"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    min_value = min(cursor.result)

    return min_value

def maxEpisodes(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Episodes"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    max_value = max(cursor.result)

    return max_value


