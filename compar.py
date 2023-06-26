from datetime import date
import time
import random
import string

class Event:
    def __init__(self, nome, data, horario):
        self.nome = nome
        self.data = data
        self.horario = horario
        self.estado = False

agenda = []

def create_event():
    nome = input('Digite o nome do evento: ')
    data = input('Digite a data do evento: ')
    horario = input('Digite o horário do evento: ')
    event = Event(nome, data, horario)
    agenda.append(event)
    print(f'Evento {nome} criado com sucesso.')

def read_event():
    nome = input('Digite o nome do evento que deseja visualizar: ')
    found = False
    for event in agenda:
        if event.nome == nome:
            print('x' * 24)
            print(f'|    Nome: {event.nome}')
            print(f'|    Data: {event.data}')
            print(f'|    Horário: {event.horario}')
            print('x' * 24)
            found = True
            break
    if not found:
        print(f'O evento {nome} não foi encontrado.')

def update_event():
    nome = input('Digite o nome do evento que deseja atualizar: ')
    found = False
    for event in agenda:
        if event.nome == nome:
            data = input('Digite a nova data do evento: ')
            horario = input('Digite o novo horário do evento: ')
            event.data = data
            event.horario = horario
            print(f'Evento {nome} atualizado com sucesso.')
            found = True
            break
    if not found:
        print(f'O evento {nome} não foi encontrado.')

def complete_event():
    nome = input('Digite o nome do evento que deseja concluir: ')
    found = False
    for event in agenda:
        if event.nome == nome:
            event.estado = True
            print(f'Evento {nome} concluido com sucesso.')
            found = True
            break
    if not found:
        print(f'O evento {nome} não foi encontrado.')

def delete_event():
    nome = input('Digite o nome do evento que deseja deletar: ')
    found = False
    for event in agenda:
        if event.nome == nome:
            agenda.remove(event)
            print(f'Evento {nome} deletado com sucesso.')
            found = True
            break
    if not found:
        print(f'O evento {nome} não foi encontrado.')

def filter_events_today():
    current_date = date.today().strftime('%d/%m/%Y')
    events = []
    for event in agenda:
        if event.data == current_date:
            events.append(event)
    events.sort(key=lambda event: event.horario)
    for event in events:
        if not event.estado:
            print('x' * 24)
            print(f'|    Nome: {event.nome}')
            print(f'|    Data: {event.data}')
            print(f'|    Horário: {event.horario}')
            print('x' * 24)

def show_all_events():
    for event in agenda:
        print(f'x' * 24 +
              f'\n|    Nome: {event.nome}'
              f'\n|    Data: {event.data}'
              f'\n|    Horário: {event.horario}'
              f'\n|    Estado: {event.estado}\n'
              + 'x' * 24)
        

def optionmains():
    print('[1 - Criar Evento        ]'
          '\n[2 - Buscar Evento       ]'
          '\n[3 - Atualizar Evento    ]'
          '\n[4 - Deletar Evento      ]'
          '\n[5 - Concluir Evento     ]'
          '\n[6 - Eventos para Hoje   ]'
          '\n[7 - Todos os Eventos    ]')

def options_menu(option: int):
    if option == 1:
        create_event()
        time.sleep(2)
    elif option == 2:
        read_event()
        time.sleep(2)
    elif option == 3:
        update_event()
        time.sleep(2)
    elif option == 4:
        delete_event()
        time.sleep(2)
    elif option == 5:
        complete_event()
        time.sleep(2)
    elif option == 6:
        filter_events_today()
        time.sleep(2)
    elif option == 7:
        show_all_events()
        time.sleep(2)
    else:
        print('Opção inválida')

