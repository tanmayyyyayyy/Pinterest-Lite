#Rodando esse File, Cria um banco de dados dentro do folder "instance"
#Rode apenas para criar um banco de dados, e só se a pasta "instance" estiver vazia

from pinterestlite import database, app
from pinterestlite.models import Usuario, Foto

with app.app_context():
    database.create_all()