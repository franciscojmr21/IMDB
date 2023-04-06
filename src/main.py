import interfaz as interfaz
import ArangoDB as DB

def main():
    
    DB.connect()
    interfaz.inicializar()
    

if __name__ == "__main__":
    main()

