# Conjuntos são valores que nunca se repetem.

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6 ,7, 8}
conjunto_uinao = conjunto.union(conjunto2) #une um conjunto ao outro
print('União: {}' .format(conjunto_uinao))
conjunto_interseccao = conjunto.intersection(conjunto2) #faz a intersecção do conjunto.
print('Intersecção: {}' .format (conjunto_interseccao))
conjunto_diferenca1 = conjunto.difference(conjunto2) #mostra os números que estão diferentes
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2: {}'.format (conjunto_diferenca1))
print('Diferença entre 2 e 1: {}'.format (conjunto_diferenca2))
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica)) #traz a diferença entre um e outro conjunto.

#pertinencia
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: {}'.format (conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a) #superconjunto
print('B é um um superconjunto de A: {}'.format(conjunto_superset))

# se estivermos trabalhando com uma lista, e quisermos tirar a duplicidade dela:

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)




'''conjunto = {1, 2, 3, 4}
conjunto.add(5)    #adiciono elementos no meu conjunto;
conjunto.discard(2) #removo elementos do meu conjunto;
print(conjunto)'''