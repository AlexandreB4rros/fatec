from asyncio import sleep
import os

valor = 0

def separador():
    """Imprime uma linha de separação no console"""
    print("-" * 80)

def limpar_tela():
    """Função para limpar a tela do console"""
    os.system('clear')

limpar_tela()
separador()

print(" --> Dando início a primeira aula de algoritimos em Python")
separador()

print("\n Primeiro desafio:\n   Crie um programa que receba um valor e informe se ele é par ou ímpar.")

def par_ou_impar(valor: int) -> str:
    """Função que recebe um valor inteiro e retorna se ele é par ou ímpar"""    
    if valor % 2 == 0:
        return "PAR"
    else:
        return "ÍMPAR"
    
        return "Você informou um valor inválido. Por favor, digite um número inteiro."

## Recebe o valor que o usuário digitar    
valor = int(input("     Para saber se o valor é par ou ímpar, digite um valor inteiro: "))

## Chama a função par_ou_impar e imprime o resultado
print("\n         O valor {} é: {}".format(valor, par_ou_impar(valor)))
