from sistema_adocao import SistemaAdocao
from animal import Animal 


def menu():
    while True:
        print(""" 
        MENU
            
            1- CADASTRAR
            2- LISTAR
            3- SAIR
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