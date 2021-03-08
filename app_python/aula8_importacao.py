''' Veremos:
- como realizar a importação de um módulo;
- entender a importância de se trabalhar com vários módulos;
- acessando a classe e métodos de um módulo;
- entendendo e trabalhando com funções anônimas (lâmbda)'''

#import aula7_televisao

from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_palavras import contador_letras

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('Total de letras por palavra de lista: {}' .format(total_letras))