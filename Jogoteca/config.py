import os

# Colocamos em caixa auta variaveis deste config

SECRET_KEY = 'alura'

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "Cs123!@#"
MYSQL_DB = "jogoteca"
MYSQL_PORT = 3306

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) \
              + '/uploads'