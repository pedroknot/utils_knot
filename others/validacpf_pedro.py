import re


# funcao para retirar caracteres nao numericos
def retira_formatacao(num_cpf):
    num_cpf_limpo= re.sub('[^0-9]', '', num_cpf)
    return num_cpf_limpo


def valida_cpf(num_cpf_limpo):

    num_cpf_limpo_validador = num_cpf_limpo[0:9]  # eliminando os digitos
    multiplicador = 10                            # multiplicador entra valendo 10
    retorno = 0                                   # retorno soma o resultado da multiplicação feita entre o numero do cpf e o multiplicador
    for numero in num_cpf_limpo_validador:
        resultado = int(numero) * int(multiplicador)
        retorno = retorno + resultado
        multiplicador -= 1
    retorno2 = (retorno * 10) % 11 % 10           # resto do algoritimo que deve ser igual ao primeiro digito do cpf para ser valido

    num_cpf_limpo_validador = num_cpf_limpo[0:10]
    multiplicador = 11
    retorno = 0
    for numero in num_cpf_limpo_validador:
        resultado = int(numero) * int(multiplicador)
        retorno = retorno + resultado
        multiplicador -= 1
    retorno3 = (retorno * 10) % 11 % 10     # resto do algoritimo que deve ser igual ao segundo digito do cpf para ser valido

    # verificando se o cpf é diferente de 11 numeros inteiros
    if len(num_cpf_limpo) != 11:
        return False

    # verificando se ambos os retornos (restos) da validação são iguais aos respectivos 2 digitos do cpf
    if int(num_cpf_limpo[9]) != int(retorno2) or int(num_cpf_limpo[10]) != int(retorno3):
        return False

    # verificando numero que passam como cpfs válidos, mas são inválidos
    lista_cpfs_invalidos = ['00000000000', '11111111111', '22222222222', '33333333333', '44444444444', '55555555555', '66666666666', '77777777777', '88888888888', '99999999999' ]
    if num_cpf_limpo in lista_cpfs_invalidos:
        return False

    return True
