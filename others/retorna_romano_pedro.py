import sys

def valida_numero(numero):
    try:
        if not 0 < numero < 3999:
            print("Valor fora do range")
            return False
        else:
            print("Numero correto")
            return numero
    except TypeError:
        print("Você digitou uma string")
        return False


def convercao_romana(numero):

    inteiros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    #exemplo:   numero = 20

    i = 0
    resultado = ""
    while numero > 0: #20 maior que 0              |   10 maior que 0
        if numero >= inteiros[i]: #20 >= 10        |   10 >= 10
            resultado += romanos[i]
            numero -= inteiros[i] #20 - 10         | 10 - 10
        else:
            i += 1

    print(resultado)
    return resultado


if __name__ == '__main__':
    numero = int(sys.argv[1])
    convercao_romana(valida_numero(numero))
    print("\n")
