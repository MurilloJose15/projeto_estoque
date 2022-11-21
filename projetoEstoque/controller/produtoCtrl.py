from model.models import Produto, Fornecedor

class ProdutoCtrl:

    def salvar_atualizar(self, nome, preco, marca, quant, desc, idFornecedor, id=None):
        try:
            produto = Produto()
            if id is not None:
                produto = Produto.get_by_id(id)
            produto.nome = nome
            produto.preco = preco
            produto.marca = marca
            produto.quant = quant
            produto.desc = desc
            produto.idFornecedor = Fornecedor.get_by_id(idFornecedor)
            produto.save()
            return 'Produto salvo!'
        except Exception as e:
            print(e)
            return 'Não foi possível salvar ou atualizar!'

    def excluirProduto(self,id):
        try:
            Produto.delete_by_id(id)
            return 'Produto excluído com sucesso!'
        except Exception as e:
            print(e)
            return 'Não foi possível excluir o produto!'

    def buscar_por_id(self,id):
        try:
            produto = Produto.get_by_id(id)
            return ({"id": produto.id,
                "nome": produto.nome,
                "preço": produto.preco,
                "marca": produto.marca,
                "quant": produto.quant,
                "descrição": produto.desc,
                "fornecedor": produto.idFornecedor.nome})
        except Exception as e:
            print(e)
            return {"Erro":"Produto não encontrado"}

    def buscar_por_nome(self,nome):
        produto = Produto.select().where(Produto.nome.contains(nome))
        produtos = []
        for i in produto.dicts():
            produtos.append(i)
        return produtos

    def buscar_todos(self):
        try:
            produto = Produto.select()
            todos_pro = []
            for p in produto.dicts():
                todos_pro.append(p)
            return todos_pro
        except Exception as e:
            print(e)
            return [{"Erro":"Não foi possível realizar a busca!"}]