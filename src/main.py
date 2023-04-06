import interfaz as interfaz
import ArangoDB as DB

def main():
    
    conn = DB.connect()
    db = DB.create(conn)
    if db['seriesYPeliculas'].count() == 0:
        DB.loadData(db)
    else:
        print("La base de datos ya está cargada")
    interfaz.inicializar()
    

if __name__ == "__main__":
    main()

