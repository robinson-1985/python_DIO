# 1. Entender o que são pacotes;
# 2. Aprender a instalar e utilizar pacotes;
# 3. Aprender a fazer requisições http(chamada de APIs)

import requests

def retorna_dados_cep(cep):
    response = requests.get('http://viacep.com.br/ws/{}/json/' .format(cep))
    print(response.status_code) # retorna o código de acesso http.
    print(response.json())
    print(response.json) # retorna como dictionary.
    print(type(response.text)) # retorna as strings (o texto).
    dados_cep = response.json()

    print(dados_cep['logradouro']) # vai para o cep! 
    print(dados_cep['complemento']) # vai para o complemento! 
    print(dados_cep['localidade']) # vai para a localidade!
    return dados_cep

def retorna_dados_pokemon(pokemon): 
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/' .format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    #retorna_dados_cep('22041001') 
    #dados_pokemon = retorna_dados_pokemon('pikachu')
    #print(dados_pokemon)
    #print(dados_pokemon['sprites']['front_shiny'])
    response = retorna_response('https://digitalinnovation.one/sign-in')
    print(response)