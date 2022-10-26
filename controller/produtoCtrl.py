from model.models import Fornecedor

class FonecedorCtrl:

    def cadastrar_atualizar(self, nome, id=None):

        try:
            fornecedor = Fornecedor()
            if id is not None:
                fonecedor = Fornecedor.get_by_id(id)
            fornecedor.nome = nome
            fornecedor.save()
            return 'Fonecedor salvo!'
        except Exception as e:
            print(e)
            return 'Não foi possível cadastrar ou atualizar o fonecedor'
