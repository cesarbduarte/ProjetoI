# Importação dos módulos

import es
import proc

#Definição de funções

def escolhedora (dados: list) ->float:
    """ esta função escolhe a função adequada de acordo com o usuário """
    if dados[1] == "+":
    resultado = proc.somadora(dados[0][0],dados[0][1])

    elif dados[1] == "-":
        resultado = proc.diminuidora(dados[0][0],dados[0][1])

    elif dados[1] == "*":
        resultado = proc.mult(dados[0][0],dados[0][1])

    elif dados[1] == "/":
        resultado = proc.div(dados[0][0],dados[0][1])
    
    return resultado


def main() -> None:
    dados = es.leitora()
    resultado = escolhedora(dados)
    es.escritora(resultado)

#Execução

if __name__ == "___main___":
    main()
    
    

