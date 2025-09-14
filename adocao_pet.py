# Criar classes bases para: animais (cachorro, gato, aves), adotante, adoção (provavelmente vamos utilizar composição)
# As informações serão armazenadas em JSON
# Vamos ter funções para pesquisar e adicionar animais

# Paramêtros de animais = nome, espécie, sexo, idade, raça, tipo de comida q come
# Paramêtros de adotante = nome, idade (+18), rg, cpf, comprovante de residencia
# Paramêtro de adoção = classe apenas para ligar o animal ao adotante. Vamos ter o histórico armazenado aqui tbm


class Animais:
    def __init__(self, nome, especie, sexo, idade, raca):
        self.nome = nome
        self.__especie = especie
        self.__sexo = sexo
        self.__idade = idade
        self.__raca = raca
    
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
    