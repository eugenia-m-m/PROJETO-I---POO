class Adotante:
    def __init__(self, nome, idade, rg, cpf, comprovante):
        self.__nome = nome
        self.__idade = idade
        self.__rg = rg
        self.__cpf = cpf
        self.__comprovante = comprovante

    @property
    def mostrar_nome (self):
        return self.__nome

    @property
    def mostrar_idade (self):
        return self.__idade
    
    @classmethod
    def editar_adotante (cls, novo_id):
        if novo_id in Adotante.cadastro_adotante:
            print('Este é o mesmo ID utilizado. Tente outro.')
            return

        print('ID foi atualizado')
        id_adotante = novo_id 
        print(f'Esse é o novo ID {id_adotante}')
