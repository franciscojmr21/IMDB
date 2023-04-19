from pyArango.connection import *
import csv
import re



def connect():
    # Establecer conexión con ArangoDB
    conn = Connection(arangoURL='http://localhost:8529', username='root', password='root')
    return conn  

def create(conn, databaseName):

    db = conn.createDatabase(name=databaseName)
    print(f'Se ha creado la base de datos {databaseName}.')

    db.createCollection(name="seriesYPeliculas")
    print(f'Se ha creado la colección seriesYPeliculas.')

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

            genreList = fila[4]
            genreList = genreList.split(",") # Separar los géneros por comas
            genreList_OK = []
            for i in genreList:
                i = i.lstrip()
                i = i.rstrip()
                genreList_OK.append(i)

            data['Genre'] = genreList_OK

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
        for j in i:
            j = j.strip() # Eliminar espacios en blanco
            if j not in genre:
                genre.append(j)
    return sorted(genre)

def typeList(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Type"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    type = []
    for i in cursor.result:
        i = i.strip() # Eliminar espacios en blanco
        if i not in type:
            type.append(i)

    return sorted(type)


def certificateList(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Certificate"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    certificate = []
    for i in cursor.result:
        i = i.strip() # Eliminar espacios en blanco
        if i not in certificate:
            certificate.append(i)

    return ["ALL"]+sorted(certificate)


def nudityList(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Nudity"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    nudity = []
    for i in cursor.result:
        i = i.strip() # Eliminar espacios en blanco
        if i not in nudity:
            nudity.append(i)

    return ["ALL"]+sorted(nudity)


def violenceList(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Violence"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    violence = []
    for i in cursor.result:
        i = i.strip() # Eliminar espacios en blanco
        if i not in violence:
            violence.append(i)

    return ["ALL"]+sorted(violence)




def profanityList(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Profanity"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    profanity = []
    for i in cursor.result:
        i = i.strip() # Eliminar espacios en blanco
        if i not in profanity:
            profanity.append(i)

    return ["ALL"]+sorted(profanity)


def alcoholList(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Alcohol"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    alcohol = []
    for i in cursor.result:
        i = i.strip() # Eliminar espacios en blanco
        if i not in alcohol:
            alcohol.append(i)

    return ["ALL"]+sorted(alcohol)



def frighteningList(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Frightening"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    frightening = []
    for i in cursor.result:
        i = i.strip() # Eliminar espacios en blanco
        if i not in frightening:
            frightening.append(i)

    return ["ALL"]+sorted(frightening)

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

def cretateIndexes(db):
    print("Creando índices...")
    collection = db["seriesYPeliculas"]
    # Crear el índice hash para un campo string
    collection.ensureHashIndex(fields=["Name"])
    collection.ensureHashIndex(fields=["Type"])
    collection.ensureHashIndex(fields=["Certificate"])
    collection.ensureHashIndex(fields=["Nudity"])
    collection.ensureHashIndex(fields=["Alcohol"])
    collection.ensureHashIndex(fields=["Violence"])
    collection.ensureHashIndex(fields=["Profanity"])
    collection.ensureHashIndex(fields=["Frightening"])
    # Crear el índice skiplist para un campo nunérico
    collection.ensureSkiplistIndex(fields=["Rate"])
    collection.ensureSkiplistIndex(fields=["Date"])
    collection.ensureSkiplistIndex(fields=["Votes"])
    collection.ensureSkiplistIndex(fields=["Duration"])
    # Crear el índice hash para una lista de strings
    collection.ensureSkiplistIndex(fields=["Genre[*]"])

    print("Índices creados")




def consulta(db, title, date, rate, votes, duration, episodes, genre, type, certificate, nudity, alcohol, violence, profanity, frightening, databaseName):
    expresion = {"Name": {title}, "Date": {date}, "Rate": {rate}, "Votes": {votes}, "Genre": {genre}, "Duration": {duration}, "Type": {type}, "Certificate": {certificate}, "Episodes": {episodes}, "Nudity": {nudity}, "Violence": {violence}, "Profanity": {profanity}, "Alcohol": {alcohol}, "Frightening": {frightening}}
    
    # Crear un objeto de ejemplo con el campo "Rate" especificado para utilizar el índice skip-list
    example_obj = {"Rate": {"$gte": 8.5}, "use_index": "Rate"}

    # Realizar la consulta utilizando el índice skip-list en el campo "Rate"
    results = db.fetchByExample(example_obj)

    return results


def dropDatabase(conn, databaseName):
    url = f'{conn.getURL()}/database/{databaseName}'
    conn.session.delete(url)
    print(f'Base de datos {databaseName} borrada correctamente')



