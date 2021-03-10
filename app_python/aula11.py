''' Como lançar uma exceção genérica;
Utilizar exceções específicas;
Encadeamento de exceções;
Else e Finally;
Criação de exceções customizadas. '''


lista = [1, 10]

try :
    arquivo= open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    print('Fechando o arquivo!')
except ZeroDivisionError:
    print('Não é possível realizar divisão por zero!')   
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um indice da lista')
except BaseException as ex: #O BaseException é o pai das exceções. 
    print('Erro desconhecido. Erro: {}' .format(ex))
else:
    print('Executa quando não ocorre exceção!')
finally:
    print('Sempre executa!')
    arquivo.close()


