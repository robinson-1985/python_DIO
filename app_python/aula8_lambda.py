# é a mesma função do contador de letras.
# é para algo que dê para reolver em uma linha, e não códigos complexos.

contador_letras = lambda lista: [len(x) for x in lista] 

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b 
subtracao = lambda a, b: a - b

print(soma(5, 10))
print(subtracao(10, 5))

# consigo criar uma calculadora inteira em lambda.

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
# o código acima é igual a soma = lambda a, b: a + b
multiplicacao = calculadora['multiplicacao']
print('A soma é: {}' .format (soma(10, 5)))
print('A multiplicação é: {}' .format(multiplicacao(10, 2)))