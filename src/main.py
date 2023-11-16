from area import menu_area
from distancia import menu_distancia
from massa import menu_massa
from velocidade import menu_velocidade
from volume import menu_volume


def menu():
    """ função para gerir o menu principal.
    Apresenta um menu e de acordo com a opção escolhida pelo utilizador entra num submenu de conversão
    ou sai da aplicação
    """

    while True:
        print("""
        ----------------------------------  Menu -----------------------------------
        (D)istancia        (V)olume        (M)assa        (A)rea        V(e)locidade

                                           (S)air
        ----------------------------------------------------------------------------""")

        op = input("opcao?").upper()

        if op == "D":
            menu_distancia()
        elif op == "V":
            menu_volume()
        elif op == "A":
            menu_area()
        elif op == "M":
            menu_massa()
        elif op == "E":
            menu_velocidade()
        elif op == "S":
            print("A sair...")
            break
        else:
            print("opção invalida")


if __name__ == "__main__":
    menu()
