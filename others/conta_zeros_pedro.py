import re
import sys

# recebo o texto independente de ter espaços ou não, vou contar todos os zeros e pegar a maior sequência
texto = str(sys.argv[1:])


def conta_zeros(texto):

    try:
        zeros_encontrados = re.findall("0+", texto)  # procuro uma ou mais ocorrências e as retorno em uma lista
        maior_quantidade_zeros = len(max(zeros_encontrados))  # pego o maior valor da lista e retorno o tamanho dele
        print(f' maior quantidade {maior_quantidade_zeros} zero(s) juntos!')
        return (maior_quantidade_zeros)

    except ValueError:
        print('Nenhum zero encontrado !')
        return 0


if __name__ == '__main__':
    conta_zeros(texto)
