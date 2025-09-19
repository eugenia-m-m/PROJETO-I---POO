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
            print('Cadastrar')
            break 
    

        elif op == '2':
            print('Listar')
            break 

        elif op == '3':
            print('Sair')
            break

        else:
            print('Opção inválida. Tente novamente!')



if __name__ == "__main__":
    menu()
    