#Função que lê dois números

def leitora_numeros() ->list:
    """ Essa função armazena dois números inputados pelo usuário """
    i = 0
    numeros = []
    while i<2:
        numeros.append(float(input(f"Digite o {i+1}º número:")))
        i+=1
    return numeros

# Função que lê  que deve ser executada

def leitora_operacao() ->str:
    """ Essa função armazena uma operação inputada pelo usuario """
    operacao = input("Digite a operação (+,-,*,/):")
    return operacao

def leitora() ->list:
    
    lista_numeros = leitora_numeros()
    operacao = leitora_operacao()
    
    return[lista_numeros, operacao]


#função de escrita de resultado
def escritora (resultado: float) -> None:
    """ A função retorna o resultado para o usuário"""
    print(f"O resultado da operação é igual a {resultado}.")