from sistema_adocao import SistemaAdocao
from animal import Animal 
from adotante import Adotante



def menu():
    while True:
        print(""" 
        ------------- MENU -------------
            
            1 - CADASTRAR ANIMAL 📃
            2 - CADASTRAR ADOTANTE 📃
            3 - LISTAR ANIMAIS 🐶🐱🐦
            4 - PESQUISAR ANIMAL 🔍
            5 - EDITAR ANIMAL ✏️
            6 - REMOVER ANIMAL 🗑️
            7 - EDITAR ADOTANTE ✏️
            0 - SAIR ❌
    """)
        op = input()
        if op == '1':
            animal_cadastro = input('Informe o ID, nome, espécie, sexo, idade, raça e se está disponível: ')
            id, nome, especie, sexo, idade, raca, disponibilidade = animal_cadastro.split()
            SistemaAdocao.cadastrar_Animal(id, nome, especie, sexo, idade, raca, disponibilidade ) # Precisa passar os parâmetros
            print('Cadastrando animal...')
            break 
    
        elif op == '2':
            adotante_cadastrar = input('Informe o iD_Adotante, nome, RG, CPF, Comprovante, Endereço e idade: ')
            id_adotante, nome, rg, cpf, comprovante, endereco, idade = adotante_cadastrar.split
            Adotante.cadastrar_adotante(id_adotante, nome, rg, cpf, comprovante, endereco, idade) # Precisa passar os parâmetros 
            print('Cadastrando adotante...')
            break 

        elif op == '3':
            print(SistemaAdocao.listar_Animais())
            print('Listando animais...')
            break 

        elif op == '4':
            SistemaAdocao.pesquisar_Animal() # Precisa passar o ID do animal 
            print('Pesquisando animais...')
            break

        elif op == '5':
            SistemaAdocao.editar_Animal() # Precisa passar o ID novo do animal
            print('Editando animais...')
            break

        elif op == '6':
            SistemaAdocao.remover_Animal() # Precisa passar o ID do animal
            print('Removendo animai')
            break

        elif op == '7':
            Adotante.editar_adotante() # Precisa passar o ID do adotante
            print('Editando adotante...')
            break

        elif op == '0':
            print('Sair')
            break

        else:
            print('Opção inválida. Tente novamente!')



if __name__ == "__main__":
    menu()
    