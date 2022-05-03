from app.infraestructura.adaptador.mysql import crear_db
from app.infraestructura.adaptador.mysql import crear_tabla


def main():

    print("Configurando la base de datos")

    crear_db.crear_base_de_datos()
    crear_tabla.crear_tabla()


if __name__ == "__main__":
    main()
