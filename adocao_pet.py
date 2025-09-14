# Criar classes bases para: animais (cachorro, gato, aves), adotante, adoção (provavelmente vamos utilizar composição)
# As informações serão armazenadas em JSON
# Vamos ter funções para pesquisar e adicionar animais

# Paramêtros de animais = nome, espécie, sexo, idade, raça, tipo de comida q come
# Paramêtros de adotante = nome, idade (+18), rg, cpf, comprovante de residencia
# Paramêtro de adoção = classe apenas para ligar o animal ao adotante. Vamos ter o histórico armazenado aqui tbm


class Animais:
    def __init__(self, id, nome, especie, sexo, idade, raca, disponibilidade):
        self.__id = id
        self.nome = nome
        self.__especie = especie
        self.__sexo = sexo
        self.__idade = idade
        self.__raca = raca
        self.__disponibilidade = disponibilidade
    
    @property
    def mostrar_id (self):
        return self.__id
    @property
    def mostrar_especie (self):
        return self.__especie
    
    @property
    def mostrar_sexo (self):
        return self.__sexo
    
    @property
    def mostrar_idade (self):
        return self.__idade
    
    @property
    def mostrar_raca (self):
        return self.__raca
    
    @property
    def mostrar_disponibilidade (self):
        return self.__disponibilidade
    
    def cadastrar_Animal (self, animal): # Função para cadastrarAnimal
        if animal not in list_animais:
            for animal in list_animais:
                id = input("Digite o id do animal: ")
                nome = input("Digite o nome do animal: ")
                especie = input("Digite a especie do animal: ")
                sexo = input("Digite o sexo do animal: ")
                idade = input("Digite a idade do animal: ")
                raca = input("Digite a raca do animal: ")
                disponibilidade = input("Digite a disponibilidade do animal: ")
                animal = Animais (id, nome, especie, sexo, idade, raca, disponibilidade)
            
            list_animais.append(animal)
            return True
        else:
            return "Animal já cadastrado."

    
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

class Adocao:
    