import peewee
from playhouse.mysql_ext import MySQLConnectorDatabase

class BaseModel(peewee.Model):

    def __init__(self, *args, **kwargs):
        try:
            self.create_table()
        except peewee.OperationalError as erro:
            print(erro)
        super().__init__(*args, **kwargs)

    class Meta:
        database = MySQLConnectorDatabase(
            'estoque',
            user='root',
            password='',
            port='3306',
            charset='utf8mb4'
        )


class Fornecedor(BaseModel):
    nome = peewee.CharField(100)


class Produto(BaseModel):
    nome = peewee.CharField(100)
    preco = peewee.DecimalField(max_digits=12, decimal_places=2)
    marca = peewee.CharField(100)
    quant = peewee.IntegerField()
    desc = peewee.CharField(400)
    fornecedor = peewee.ForeignKeyField(Fornecedor, on_delete='CASCADE', backref='alunos')
