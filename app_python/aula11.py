''' Como lançar uma exceção genérica;
Utilizar exceções específicas;
Encadeamento de exceções;
Else e Finally;
Criação de exceções customizadas. '''


lista = [1, 10]
try :
    divisao = 10 / 1
    numero = lista[1]
    x = a 
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0!')
except IndexError:
    print('Erro ao acessar um indice da lista')
except BaseException as ex: #O BaseException é o pai das exceções. 
    print('Erro desconhecido. Erro: {}' .format(ex))
