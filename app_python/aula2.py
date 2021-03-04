a = int(input('Entre com o primeiro valor: '))
b =  int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = ('Soma: {soma}. \nSubtração: {subtracao}.'
        '\nMultiplicação: {multiplicacao}'
        '\nDivisao: {divisao}' 
        '\nResto: {resto}' .format(soma=soma, 
                                    subtracao=subtracao,
                                    divisao=divisao,
                                    multiplicacao=multiplicacao,
                                    resto=resto))
print(resultado)
'''print('soma:' + str(soma)) #fez uma concatenação!
print(subtracao)
print(multiplicacao)
print(int(divisao))
print(divisao)
print(resto)
x = '1'
soma2 = int(x) + 1
print(soma2)'''