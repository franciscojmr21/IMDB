import interfaz as interfaz
import ArangoDB as DB
import sys

def main():

    if((len(sys.argv) - 1) != 1):
        print("Debes especificar el nombre de la base de datos")
        return
    else:
        databaseName = sys.argv[1]
        conn = DB.connect()
        db = DB.create(conn, databaseName)
        DB.loadData(db)
        interfaz.initialize(db, databaseName)
        DB.dropDatabase(conn, databaseName)


# spaninglish
# en las funciones select de interfaz.py no se usa el parametro valor (quitar??)
# los filtros funcionan???


if __name__ == "__main__":
    main()

