import PySimpleGUI as sg

"""
    Demonstração - Caixa de listagem usando objetos

    Vários elementos podem receber não apenas strings, mas objetos. O Listsbox é um deles.
    Esta demonstração mostra como você pode usar objetos diretamente em um Listbox de forma que você possa acessar
    informações sobre cada objeto que são diferentes do que é mostrado na Janela.

    A parte importante desse padrão de design é o uso do método __str__ em seus objetos de item.
    Este método é o que determina o que é mostrado na janela.

    Copyright 2022 PySimpleGUI

"""

class Item():
    def __init__(self, internal, shown):
        self.internal = internal
        self.shown = shown

    def __str__(self):
        return self.shown

# make list of some objects
my_item_list = [Item(f'Internal {i}', f'shown {i}') for i in range(100)]

layout = [  [sg.Text('Select 1 or more items and click "Go"')],
            [sg.Listbox(my_item_list, key='-LB-', s=(20,20), select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED)],
            [sg.Output(s=(40,10))],
            [sg.Button('Go'), sg.Button('Exit')]  ]

window = sg.Window('Listbox Using Objects', layout)

while True:
    event, values = window.read()
    # print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Go':
        print('You selected:')
        for item in values['-LB-']:
            print(item.internal)
window.close()