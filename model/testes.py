from model.models import Fornecedor, Produto

"""
fornecedor = Fornecedor()
fornecedor.nome = 'Multilaser'
print(fornecedor.save())
"""
produto = Produto()
produto.nome = 'Roteador AC1200'
produto.preco = 250.00
produto.marca = 'Multilaser'
produto.quant = 10
produto.desc = 'Roteador Gigabit, possui 4 portas lan e uma 1 wan'
fornecedor = Fornecedor.get_by_id(1)
produto.fornecedor = fornecedor
print(produto.save())