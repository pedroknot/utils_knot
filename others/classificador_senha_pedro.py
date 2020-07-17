import sys
import re

pwd = str(sys.argv[1:])


def classificador_de_senhas(pwd):
    len_pwd = len(pwd)
    char_pwd = re.findall("[a-z]", pwd)  # capturo letras minúsculas
    char_pwd_upper = re.findall("[A-Z]", pwd)  # capturo letras maiúsculas
    char_pwd_number = re.findall("[0-9]", pwd)  # capturo números
    char_pwd_special = re.findall("[!@#$%&*]", pwd)  # capturo caracteres especiais

    # verifico se o tamanho do pwd > 8 e se contem letra minúscula, letra maiúscula, números e caracteres especiais
    if len_pwd >= 8 and len(char_pwd) and len(char_pwd_upper) and len(char_pwd_number) and len(char_pwd_special) > 0:
        print("Nível de senha: 2")
        return 2

    # verifico se o tamanho do pwd >= 6 e se contem letra minúscula, letra maiúscula ou números ou caracteres especiais
    elif len_pwd >= 6:
        if len(char_pwd) and len(char_pwd_upper) or len(char_pwd_number) or len(char_pwd_special) > 0:
            print("Nível de senha: 1")
            return 1
        else:
            print("Nível de senha: 0")
            return 0

    else:
        print("Nível de senha: 0")
        return 0


if __name__ == '__main__':
    classificador_de_senhas(pwd)
