lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista_animal[0] = 'macaco' # a lista pode variar de valor, porém, a tupla não!!!!
print(lista_animal)

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla) #converte a tupla para lista
print(type(lista_numerica))
print(lista_numerica)
lista_numerica[0] = 100
print(lista_numerica)



'''print(lista_animal[1])
nova_lista = lista_animal * 3
print(nova_lista) 
lista.sort()   #ordena por ordem alfabética. 
lista_animal.sort()
print(lista)
print(lista_animal)
lista_animal.reverse() #ordena do final para o começo.
print(lista_animal)

if 'lobo' in lista_animal:              # para procurar algo na lista. 
    print('Existe um lobo na lista!')
else:
    print('Não existe um lobo na lista!')
    lista_animal.append('lobo')   # o .append inclui algo.
    print(lista_animal)

lista_animal.pop()    # o .pop retira sempre a última inclusão, aqui será o lobo.
print(lista_animal)

lista_animal.pop(0)    # o .pop retira pela posição também, no 0 será o cachorro.
print(lista_animal)

lista_animal.remove('elefante') # se quiser remover um elemento que já conheço uso o .remove
print(lista_animal)'''





    

#print(max(lista_animal))  maior valor

#print(sum(lista)) #soma

'''soma = 0
for x in lista_animal:
    print(x)
    soma += x
print(soma)'''