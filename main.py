from sistema_adocao import SistemaAdocao
from animal import Animal 


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
            print('Cadastrando animal...')
            break 
    
        elif op == '2':
            print('Cadastrando adotante...')
            break 

        elif op == '3':
            print('Listando animais...')
            break 

        elif op == '4':
            print('Pesquisando animais...')
            break

        elif op == '5':
            print('Editando animais...')
            break

        elif op == '6':
            print('Removendo animai')
            break

        elif op == '7':
            print('Editando adotante...')
            break

        elif op == '0':
            print('Sair')
            break

        else:
            print('Opção inválida. Tente novamente!')



if __name__ == "__main__":
    menu()
    