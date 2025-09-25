from animal import Animal

class SistemaAdocao:
    list_animais = []

    @classmethod
    def cadastrar_Animal(cls, id, nome, especie, sexo, idade, raca, disponibilidade):
        for pet in cls.list_animais:
            if pet.id == id:
                return "Animal já cadastrado."

        animal = Animal(id, nome, especie, sexo, idade, raca, disponibilidade)
        cls.list_animais.append(animal)
        return "Animal cadastrado com sucesso."

    @classmethod
    def pesquisar_Animal(cls, id_animal):
        for animal in cls.list_animais:
            if animal.id == id_animal:
                return animal
        return "Animal não encontrado."

    @classmethod
    def editar_Animal(cls, id_animal):
        for animal in cls.list_animais:
            if animal.id == id_animal:
                animal.nome = input("Digite o novo nome do animal: ")
                animal.especie = input("Digite a nova espécie do animal: ")
                animal.sexo = input("Digite o novo sexo do animal: ")
                animal.idade = input("Digite a nova idade do animal: ")
                animal.raca = input("Digite a nova raça do animal: ")
                animal.disponibilidade = input("Digite a disponibilidade do animal: ")
                return "Animal atualizado com sucesso."
            
            else:
                return "Animal nao encontrado."

    @classmethod
    def listar_Animais(cls):
        if not cls.list_animais:
            return "Nenhum animal cadastrado."
        
        resultado = "\n---------------- Animais cadastrados ----------------\n"

        for animal in cls.list_animais:
            resultado += f"ID: {animal.id}\n"
            resultado += f"Nome: {animal.nome}\n"
            resultado += f"Espécie: {animal.especie}\n"
            resultado += f"Sexo: {animal.sexo}\n"
            resultado += f"Idade: {animal.idade}\n"
            resultado += f"Raça: {animal.raca}\n"
            resultado += f"Disponibilidade: {animal.disponibilidade}\n"
            resultado += "-" * 40 + "\n"
        return resultado
    
    @classmethod
    def remover_Animal(cls, id_animal):
        for animal in cls.list_animais:
            if animal.id == id_animal:
                cls.list_animais.remove(animal)
                return "Animal removido com sucesso."
        return "Animal nao encontrado."
    
# class Animal:
#     def __init__(self, id, nome, especie, sexo, idade, raca, disponibilidade):
#         self.id = id
#         self.nome = nome
#         self.especie = especie
#         self.sexo = sexo
#         self.idade = idade
#         self.raca = raca
#         self.disponibilidade = disponibilidade


# class Adotante:
#     def __init__(self, nome, idade, rg, cpf, comprovante):
#         self.__nome = nome
#         self.__idade = idade
#         self.__rg = rg
#         self.__cpf = cpf
#         self.__comprovante = comprovante

#     @property
#     def mostrar_nome (self):
#         return self.__nome

#     @property
#     def mostrar_idade (self):
#         return self.__idade
    
#     @classmethod
#     def editar_adotante (cls, novo_id):
#         if novo_id in Adotante.cadastro_adotante:
#             print('Este é o mesmo ID utilizado. Tente outro.')
#             return

#         print('ID foi atualizado')
#         id_adotante = novo_id 
#         print(f'Esse é o novo ID {id_adotante}')

    
sistema = SistemaAdocao()
sistema.cadastrar_Animal(1, "Luna", "Cachorro", "Fêmea", "2 anos", "Labrador", "Sim")
sistema.cadastrar_Animal(2, "Rex", "Cachorro", "Macho", "3 anos", "Vira-lata", "Sim")
sistema.cadastrar_Animal(3, "Toby", "Gato", "Macho", "1 ano", "Siames", "Sim")
sistema.cadastrar_Animal(4, "Charlie", "Gato", "Macho", "2 anos", "Persa", "Sim")

# print(sistema.listar_Animais())

# print(sistema.pesquisar_Animal(2))

# print(sistema.listar_Animais())

# print(sistema.editar_Animal(2)) 

# print(sistema.listar_Animais()) 

print(sistema.remover_Animal(2))

# print(sistema.listar_Animais())