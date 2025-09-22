<<<<<<< Updated upstream
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
            SistemaAdocao.cadastrar_Animal() # Precisa passar os parâmetros
            print('Cadastrando animal...')
            break 
    
        elif op == '2':
            Adotante.cadastrar_adotante() # Precisa passar os parâmetros 
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
=======
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
            SistemaAdocao.cadastrar_Animal() # Precisa passar os parâmetros
            print('Cadastrando animal...')
            break 
    
        elif op == '2':
            Adotante.cadastrar_adotante() # Precisa passar os parâmetros 
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
>>>>>>> Stashed changes
    