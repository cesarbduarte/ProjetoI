"""
Módulo Proc
Descrição: Este módulo provê funções da calculadora básica;
Autor: César Duarte
Versão: 0.0.1
Data: 29/11/2023

"""

def somadora (num1: float, num2: float) -> float:
    """Esta função pega dois números reais e retorna a soma deles"""
    return num1 + num2

def diminuidora (num1: float, num2: float) -> float:
    """Esta função pega dois números reais e retorna a subtração deles"""
    return num1 - num2

def mult (num1: float, num2: float) -> float:
    """Esta função pega dois números reais e retorna o produto deles"""
    return num1 * num2

def div (num1: float, num2: float) -> float:
    """Esta função pega dois números reais e retorna a razão deles"""
    
    if num2 == 0:
            resultado = "Não existe divisão por zero"
    else: 
            resultado = num1 / num2
                
    return resultado

