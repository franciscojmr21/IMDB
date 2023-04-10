import interfaz as interfaz
import ArangoDB as DB

def main():
    
    conn = DB.connect()
    db = DB.create(conn)
    if db['seriesYPeliculas'].count() == 0:
        DB.loadData(db)
    else:
        print("La base de datos ya está cargada")
    interfaz.initialize(db)

# probar a borrar la base de datos y poner el logo de la app
# spaninglish
# case sensitive
# búsqueda vacía


if __name__ == "__main__":
    main()

