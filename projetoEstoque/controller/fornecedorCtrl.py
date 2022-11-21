from model.models import Fornecedor

class FonecedorCtrl:

    def cadastrar_atualizar(self, nome, id=None):

        try:
            fornecedor = Fornecedor()
            if id is not None:
                fornecedor = Fornecedor.get_by_id(id)
            fornecedor.nome = nome
            fornecedor.save()
            return 'Fonecedor salvo!'
        except Exception as e:
            print(e)
            return 'Não foi possível cadastrar ou atualizar o fonecedor'

    def excluirFornecedor(self, id):
        try:
            Fornecedor.delete_by_id(id)
            return 'Fornecedor excluído com sucesso!'
        except Exception as e:
            print(e)
            return 'Não foi possível excluir o fornecedor!'

    def buscar_por_id(self, id):
        try:
            fornecedor = Fornecedor.get_by_id(id)
            return({"id": fornecedor.id,
                   "nome": fornecedor.nome})
        except Exception as e:
            print(e)
            return {"Erro":"Fornecedor não encontrado!"}

    def buscar_por_nome(self,nome):
        fornecedor = Fornecedor.select().where(Fornecedor.nome.contains(nome))
        fornecedores = []
        for i in fornecedor.dicts():
            fornecedores.append(i)
        return fornecedores

    def buscar_todos(self):
        try:
            fornecedor = Fornecedor.select()
            todos_for = []
            for f in fornecedor.dicts():
                todos_for.append(f)
            return todos_for
        except Exception as e:
            print(e)
            return [{"Erro":"Não foi possível realizar a busca!"}]
