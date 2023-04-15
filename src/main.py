import interfaz as interfaz
import ArangoDB as DB
import sys

def main():

    if((len(sys.argv) - 1) != 1):
        print("Usage: python main.py <databaseName>")
        return
    else:
        databaseName = sys.argv[1]
        conn = DB.connect()
        db = DB.create(conn, databaseName)
        DB.loadData(db)
        interfaz.initialize(db, databaseName)
        DB.dropDatabase(conn, databaseName)

# probar a borrar la base de datos y poner el logo de la app
# spaninglish
# búsqueda vacía
# dejar espacio a la tabla (margin-top)


if __name__ == "__main__":
    main()

