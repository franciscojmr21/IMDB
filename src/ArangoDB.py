from pyArango.connection import *
from pyArango.collection import Collection, Field
import csv


def connect():
    # Establecer conexión con ArangoDB
    conn = Connection(arangoURL='http://localhost:8529', username='root', password='root')

    # Crear una nueva base de datos
    db_nombre = 'nombre_de_tu_base_de_datos'
    if not conn.hasDatabase('IMDB'):
        db = conn.createDatabase(name='IMDB')
        print(f'Se ha creado la base de datos IMDB.')
    else:
        db = conn['IMDB']
        print(f'La base de datos IMDB ya existe.')


    if not db.hasCollection("seriesYPeliculas"):
        db.createCollection(name="seriesYPeliculas")
    collection = db["seriesYPeliculas"]

    # Realizar una consulta AQL para obtener los documentos que cumplan cierta condición
    consulta = "FOR doc IN collection FILTER doc.propiedad = 'valor' RETURN doc"
    resultado = db.AQLQuery(consulta)

    # Imprimir los documentos
    for documento in resultado:
        print(documento)
