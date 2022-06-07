# Plantilla Arquitectura Hexagonal en Python

Requisitos:

- Python > 3.8
- Pipenv

# INSTALL

Pipenv es un manejador de dependencias para los proyectos de Python,
para instalar
Install:

     pip install --user pipenv

Instalamos las librerías del proyecto

    pipenv install --dev

# VARIABLES DE ENTORNO

se necesita configurar las siguientes variables de entorno, en el respectivo archivo ´.env´

    USUARIO_DB = el usuario de la base de datos MysQL
    PASSWORD_DB = el password de la base de datos MySQL
    HOST_DB = La ip del servidor de MySQL, para pruebas locales "localhost"
    NAME_DB = Nombre de la base de datos.

# DATABASE

Iniciamos el entorno de trabajo:

    pipenv shell

ejecutamos

    pipenv run python setup_db.py

# REST

Iniciamos el entorno de trabajo:

    pipenv shell

Iniciamos el servicio en el puerto 8084, en modo desarrollador:

    uvicorn app.main:app --port 8084 --reload

para ver la documentación de la API podemos ingresar a
http://localhost:8084/docs.

# TEST

Para ejecutar el test, con el entorno de trabajo activado (`pipenv shell`):

    pytest
