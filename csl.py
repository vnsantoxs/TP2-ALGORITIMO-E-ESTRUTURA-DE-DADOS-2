from datetime import date
import time


class AVLNode:
    def __init__(self, nome, data, horario):
        self.nome = nome
        self.data = data
        self.horario = horario
        self.estado = False
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, nome, data, horario):
        self.root = self._insert_node(self.root, nome, data, horario)

    def _insert_node(self, root, nome, data, horario):
        if not root:
            return AVLNode(nome, data, horario)
        elif nome < root.nome:
            root.left = self._insert_node(root.left, nome, data, horario)
        else:
            root.right = self._insert_node(root.right, nome, data, horario)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        balance_factor = self._get_balance_factor(root)

        if balance_factor > 1 and nome < root.left.nome:
            return self._rotate_right(root)

        if balance_factor < -1 and nome > root.right.nome:
            return self._rotate_left(root)

        if balance_factor > 1 and nome > root.left.nome:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        if balance_factor < -1 and nome < root.right.nome:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def delete(self, nome):
        self.root = self._delete_node(self.root, nome)

    def _delete_node(self, root, nome):
        if not root:
            return root
        elif nome < root.nome:
            root.left = self._delete_node(root.left, nome)
        elif nome > root.nome:
            root.right = self._delete_node(root.right, nome)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self._get_min_value_node(root.right)
            root.nome = temp.nome
            root.data = temp.data
            root.horario = temp.horario
            root.right = self._delete_node(root.right, temp.nome)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        balance_factor = self._get_balance_factor(root)

        if balance_factor > 1 and self._get_balance_factor(root.left) >= 0:
            return self._rotate_right(root)

        if balance_factor < -1 and self._get_balance_factor(root.right) <= 0:
            return self._rotate_left(root)

        if balance_factor > 1 and self._get_balance_factor(root.left) < 0:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        if balance_factor < -1 and self._get_balance_factor(root.right) > 0:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def _get_min_value_node(self, root):
        if root is None or root.left is None:
            return root

        return self._get_min_value_node(root.left)

    def _get_height(self, root):
        if not root:
            return 0
        return root.height

    def _get_balance_factor(self, root):
        if not root:
            return 0
        return self._get_height(root.left) - self._get_height(root.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))


agenda = AVLTree()


def create_event():
    nome = input('Digite o nome do evento: ')
    data = input('Digite a data do evento: ')
    horario = input('Digite o horário do evento: ')
    agenda.insert(nome, data, horario)
    print(f'Evento {nome} criado com sucesso.')


def read_event():
    nome = input('Digite o nome do evento que deseja visualizar: ')
    event = agenda.root
    while event:
        if event.nome == nome:
            print('x' * 24)
            print(f'|    Nome: {event.nome}')
            print(f'|    Data: {event.data}')
            print(f'|    Horário: {event.horario}')
            print('x' * 24)
            return
        elif nome < event.nome:
            event = event.left
        else:
            event = event.right

    print(f'O evento {nome} não foi encontrado.')


def update_event():
    nome = input('Digite o nome do evento que deseja atualizar: ')
    event = agenda.root
    while event:
        if event.nome == nome:
            data = input('Digite a nova data do evento: ')
            horario = input('Digite o novo horário do evento: ')
            event.data = data
            event.horario = horario
            print(f'Evento {nome} atualizado com sucesso.')
            return
        elif nome < event.nome:
            event = event.left
        else:
            event = event.right

    print(f'O evento {nome} não foi encontrado.')


def complete_event():
    nome = input('Digite o nome do evento que deseja concluir: ')
    event = agenda.root
    while event:
        if event.nome == nome:
            event.estado = True
            print(f'Evento {nome} concluido com sucesso.')
            return
        elif nome < event.nome:
            event = event.left
        else:
            event = event.right

    print(f'O evento {nome} não foi encontrado.')


def delete_event():
    nome = input('Digite o nome do evento que deseja deletar: ')
    agenda.delete(nome)
    print(f'Evento {nome} deletado com sucesso.')


def filter_events_today():
    current_date = date.today().strftime('%d/%m/%Y')
    events = []
    filter_events_today_helper(agenda.root, current_date, events)
    events.sort(key=lambda event: event.horario)

    for event in events:
        if (event.estado == False):
            print('x' * 24)
            print(f'|    Nome: {event.nome}')
            print(f'|    Data: {event.data}')
            print(f'|    Horário: {event.horario}')
            print('x' * 24)


def filter_events_today_helper(node, current_date, events):
    if node is None:
        return

    filter_events_today_helper(node.left, current_date, events)

    if node.data == current_date:
        events.append(node)

    filter_events_today_helper(node.right, current_date, events)


def show_all_events():
    show_all_events_helper(agenda.root)


def show_all_events_helper(node):
    if node is None:
        return

    show_all_events_helper(node.left)
    print(f'x' * 24 +
          f'\n|    Nome: {node.nome}'
          f'\n|    Data: {node.data}'
          f'\n|    Horário: {node.horario}'
          f'\n|    Estado: {node.estado}\n'
          + 'x' * 24)
    show_all_events_helper(node.right)


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
        print('Opção invalida')
