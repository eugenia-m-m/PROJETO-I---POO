class Adotante:
    cadastro_adotantes = []

    def __init__(self, nome, idade, rg, cpf, comprovante):
        self.__nome = nome
        self.__idade = idade
        self.__rg = rg
        self.__cpf = cpf
        self.__comprovante = comprovante
        Adotante.cadastro_adotantes.append(self)
    
    @property
    def mostrar_nome (self):
        return self.__nome

    @property
    def mostrar_idade (self):
        return self.__idade
    
    @classmethod
    def listar_adotantes(cls):
        return cls.cadastro_adotantes  
    
    @classmethod
    def cadastrar_Animal(cls, id, nome, idade, rg, cpf, comprovante, endereco):
        for canditato in cls.cadastro_adotantes:
            if canditato.id == id:
                return "Adotante já cadastrado."

        animal = Adotante(id, nome, idade, rg, cpf, comprovante, endereco)
        cls.cadastro_adotantes.append(animal)
        return "Adotante cadastrado com sucesso."

    
    @classmethod
    def editar_adotante (cls, novo_id):
        if novo_id in Adotante.cadastro_adotante:
            print('Este é o mesmo ID utilizado. Tente outro.')
            return

        print('ID foi atualizado')
        id_adotante = novo_id 
        print(f'Esse é o novo ID {id_adotante}')
