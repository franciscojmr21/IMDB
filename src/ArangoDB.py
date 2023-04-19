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

def consulta(db, title, date, rate, votes, duration, episodes, genre, type, certificate, nudity, alcohol, violence, profanity, frightening, databaseName):
    conn = Connection(username="root", password="root")

    # Construir la consulta
    aql = """
           FOR doc IN seriesYPeliculas
                FILTER (@title == "" OR LOWER(doc.Name) LIKE LOWER(CONCAT("%", @title, "%")))
                FILTER (@date == "" OR doc.Date >= @date)
                FILTER (@rate == "" OR doc.Rate >= @rate)
                FILTER (@votes == "" OR doc.Votes >= @votes)
                FILTER (@duration == "" OR doc.Duration >= @duration)
                FILTER (@episodes == "" OR doc.Episodes >= @episodes)
                FILTER (doc.Genre ANY IN @genre OR @genre == [])
                FILTER (doc.Type IN @type OR @type == [])
                FILTER (@certificate == "ALL" OR doc.Certificate == @certificate)
                FILTER (@nudity == "ALL" OR doc.Nudity == @nudity)
                FILTER (@alcohol == "ALL" OR doc.Alcohol == @alcohol)
                FILTER (@violence == "ALL" OR doc.Violence == @violence)
                FILTER (@profanity == "ALL" OR doc.Profanity == @profanity)
                FILTER (@frightening == "ALL" OR doc.Frightening == @frightening)
                RETURN doc
                """

    # Definir los parámetros de la consulta
    bind_vars = {
        "title": title,
        "genre": genre,
        "date": date,
        "rate": str(rate),
        "votes": votes,
        "duration": duration,
        "episodes": episodes,
        "type": type,
        "certificate": certificate,
        "nudity": nudity,
        "alcohol": alcohol,
        "violence": violence,
        "profanity": profanity,
        "frightening": frightening
        }

    # Ejecutar la consulta
    cursor = db.AQLQuery(aql, bindVars=bind_vars)
    results = [document for document in cursor]
    # expresión regular para extraer la información de cada película
    expresion = r"{.*?Name': '(.*?)', 'Date': '(.*?)', 'Rate': '(.*?)', 'Votes': (.*?), 'Genre': (.*?), 'Duration': (.*?), 'Type': '(.*?)', 'Certificate': '(.*?)', 'Episodes': (.*?), 'Nudity': '(.*?)', 'Violence': '(.*?)', 'Profanity': '(.*?)', 'Alcohol': '(.*?)', 'Frightening': '(.*?)'}"
    # Buscar todas las coincidencias
    coincidencias = re.findall(expresion, str(results))
     # Eliminar corchetes y espacios
    #generos = coincidencias[0][4].replace("[", "").replace("]", "")
    return coincidencias


def dropDatabase(conn, databaseName):
    url = f'{conn.getURL()}/database/{databaseName}'
    conn.session.delete(url)
    print(f'Base de datos {databaseName} borrada correctamente')



