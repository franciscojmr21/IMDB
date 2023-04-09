from pyArango.connection import *
from pyArango.query import AQLQuery
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

    return ["ALL"]+sorted(certificate)


def nudityList(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Nudity"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    nudity = []
    for i in cursor.result:
        nudities= i.split(",")
        for j in nudities:
            if j not in nudity:
                nudity.append(j)

    return ["ALL"]+sorted(nudity)


def violenceList(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Violence"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    violence = []
    for i in cursor.result:
        violences= i.split(",")
        for j in violences:
            if j not in violence:
                violence.append(j)

    return ["ALL"]+sorted(violence)




def profanityList(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Profanity"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    profanity = []
    for i in cursor.result:
        profanities= i.split(",")
        for j in profanities:
            if j not in profanity:
                profanity.append(j)

    return ["ALL"]+sorted(profanity)


def alcoholList(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Alcohol"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    alcohol = []
    for i in cursor.result:
        alcoholes= i.split(",")
        for j in alcoholes:
            if j not in alcohol:
                alcohol.append(j)

    return ["ALL"]+sorted(alcohol)



def frighteningList(db):
    query = "FOR doc IN seriesYPeliculas RETURN doc.Frightening"
    cursor = db.AQLQuery(query, batchSize=100000000, rawResults=True)
    frightening = []
    for i in cursor.result:
        frighten= i.split(",")
        for j in frighten:
            if j not in frightening:
                frightening.append(j)

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

def consulta(db, title, date, rate, votes, duration, episodes, genre, type, certificate, nudity, alcohol, violence, profanity, frightening):
    print("Consulta")

    conn = Connection(username="root", password="root")
    db = conn["IMDB"]

    if "seriesYPeliculas" in db.collections:
        print("La colección existe.")
    else:
        print("La colección no existe.")

    query = """
            FOR doc IN seriesYPeliculas
                FILTER (@title == "" OR doc.Name LIKE CONCAT("%", @title, "%"))
                FILTER (@date == "" OR doc.Date == @date)
                FILTER (@rate == "" OR doc.Rate >= @rate)
                FILTER (@votes == "" OR doc.Votes >= @votes)
                FILTER (@duration == "" OR doc.Duration >= @duration)
                FILTER (@episodes == "" OR doc.Episodes >= @episodes)
                FILTER (@certificate == "" OR doc.Certificate == @certificate)
                FILTER (@nudity == "" OR doc.Nudity == @nudity)
                FILTER (@alcohol == "" OR doc.Alcohol == @alcohol)
                FILTER (@violence == "" OR doc.Violence == @violence)
                FILTER (@profanity == "" OR doc.Profanity == @profanity)
                FILTER (@frightening == "" OR doc.Frightening == @frightening)
                RETURN doc
        """
    cursor = db.AQLQuery(query, bindVars={
        "Name": title,
        "Date": date,
        "Rate": rate,
        "Votes": votes,
        "Duration": duration,
        "Episodes": episodes,
        "Certificate": certificate,
        "Nudity": nudity,
        "Alcohol": alcohol,
        "Violence": violence,
        "Profanity": profanity,
        "Frightening": frightening
    })

    return [doc for doc in cursor]



