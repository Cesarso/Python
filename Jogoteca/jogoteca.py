from flask import Flask

from flask_mysqldb import MySQL



app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MySQL(app)


#para aplicação rodar, precisa inserir todas as views
from views import *

#isso garante que a aplicação não execute quando importa as views
#não executando essa linha quando executado através de um import ou outro tipo de execução

if __name__ == '__main__':
    app.run(debug=True)
