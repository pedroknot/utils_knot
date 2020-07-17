from random import choice


def gera_senha():

    Algarismos = ("a1A2b3B4c5C6d7D@e9E0fghijklmnopq1FGHI2JKLP5Qrstuvxy6zRSTUVX9YZ")
    senha_final = ""
    cont = 0
    while cont <= 15:
        senha_final += choice(Algarismos)
        cont += 1

    print(senha_final)
    return senha_final


if __name__ == '__main__':
    gera_senha()
