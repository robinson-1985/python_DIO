# criando arquivos

import shutil

def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0) # função pop () é usado para remover um elemento na lista (por padrão, o último elemento)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4 #list comprehension
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

''' sum - Somar todos os elementos de algum conjunto é uma tarefa bastante comum em 
programação. Sendo assim, o Python também tem uma função nativa dedicada ao 
cálculo da soma de todos os elementos de uma lista - a função sum()!

list comprehension - Uma compreensão de lista é uma construção sintática disponível em algumas 
linguagens de programação para criação de uma lista baseada em listas existentes.
Ela segue a forma da notação de definição de conjunto matemática como forma 
distinta para uso de funções de mapa e filtro. '''

def copia_arquivo(nome_arquivo):
   shutil.copy(nome_arquivo, 'notas_alunos.txt')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'notas_alunos.txt')



if __name__ == '__main__':
    move_arquivo('notas.txt')
    #copia_arquivo('notas.txt')
    #lista_media = media_notas('notas.txt')
    #print(lista_media)
    #escrever_arquivo('Primeira linha. \n')
    #aluno = '\nCesar, 7, 9, 3, 8\n'
    #atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')



'''arquivo = open('teste.txt', 'w')
arquivo.write('Segunda linha')
arquivo.close()

se for só escrever usa o w, agora se for atualizar usa o a'''