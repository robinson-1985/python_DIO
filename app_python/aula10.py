''' DATE - como recuperar a data atual;
Como trabalhar coma a data, alterando sua formatação;
Comgerar um horário (TIME);
Retornar data e hora atual(DATETIME);
Alterar a formação do DATETIME;
Realizar soma e subtração de datas com TIMEDELTA.'''

# Função date

from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y')) #data
    print(data_atual.strftime('%H:%M:%S')) #hora
    print(data_atual.strftime('%c')) #esse comando mostra dia, mês, hora e ano.
    print(data_atual.day) # traz o dia
    print(data_atual.year) # traz o ano
    print(data_atual.hour) # traz a hora
    print(data_atual.minute) # traz os minutos
    print(data_atual.second) # traz os segundos
    print(data_atual.date()) # traz a data
    print(data_atual.weekday()) # traz o dia da semana
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()]) #para retornar o dia da semana.
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada) #posso repetir usando o código abaixo:
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019  12:20:22' # para converter string em datetime:
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    print(data_convertida.weekday()) #dia da semana
    nova_data = data_convertida + timedelta(days=365, hours=2, minutes=15)
    print(nova_data) #timedelta nesse caso soma o valor da data atribuida.
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data) #timedelta aqui subtrai o valor da data atribuida.


def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %B  %Y')
    print(data_atual)   #estilo de data estadunidense.
    print(data_atual.strftime('%d/%m/%y')) #estilo de data brasileira. 
    print(data_atual.strftime('%A %B  %Y')) #para aparecer dia da semana, mês e ano. 
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S:')
    print(horario_str)
    print(type(horario_str))

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()