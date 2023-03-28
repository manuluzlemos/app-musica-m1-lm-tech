# Estudante: Emanuelle da Luz Lemos (manuluz.lemos@gmail.com)
# Arquivo principal do programa 

from interface_administrador import menu_admin
from interface_usuario import menu_user
from excecoes import *

# função principal do programa
def main():
    continuar = True
    while continuar:
        print("\n\n**** APP DE MÚSICA ****")
        print("1) Logar como admin")
        print("2) Logar como usuário")
        print("0) Sair\n")

        try:
            opcao = int(input("Informe a opção desejada: "))
        except ValueError:
            print("Atenção. A opção deve ser um número. Tente novamente!")
        else:
            if opcao == 0:
                print("** Programa encerrado **")
                continuar = False
            elif opcao == 1:
                menu_admin()
            elif opcao == 2:
                menu_user()
            else:
                print("Opção inválida. Tente novamente!")

if __name__ == '__main__':
    main()