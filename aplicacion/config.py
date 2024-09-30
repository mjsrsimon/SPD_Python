import os
import urllib

import pyodbc

# CADENA DE CONEXION A LA BASE DE DATOS
# https://gist.github.com/josejaguirre/8cafd8818eea2659e3e9c250a3344128

secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

# ojo, tendria que coger estos datos de un fichero de configuracion.


# Configura tu conexión
server = 'EPJRUIZ\\SQLEXPRESS'  # por ejemplo, 'localhost' o 'nombre_del_servidor'
database = 'Mi_PWinR'
username = 'robot'
password = 'farmae'
driver = '{ODBC Driver 17 for SQL Server}'  # Asegúrate de que tienes este driver instalado

# Cadena de conexión
#conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')

# Ahora puedes usar `conn` para interactuar con la base de datos
string_connection='mssql+pyodbc://robot:farmae@EPJRUIZ\\SQLEXPRESS\\/Mi_PWinR?driver=ODBC+Driver+17+for+SQL+Server'

SQLALCHEMY_DATABASE_URI = string_connection
SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = True
# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
# SQLALCHEMY_TRACK_MODIFICATIONS = False
