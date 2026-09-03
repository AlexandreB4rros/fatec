# Praticando listas


def fatiando(valor1, valor2):
    listaf = lista[valor1:valor2]
    return listaf

lista = 'Python'
quantidade_letras = len(lista)

valor1 = int(input('Digite o valor 1: '))
valor2 = int(input('Digite o valor 2: '))

resultado = fatiando(valor1,valor2)


mensagem_usuario = f'''
- Levando em consideração a palavra:
{lista}

que possue o total de {quantidade_letras} letras

e o resultado do fatiamento entre o valor {valor1} e o {valor2} é:
--> {resultado}
'''

print('-'*80,'\n', mensagem_usuario, '\n', '-'*80)