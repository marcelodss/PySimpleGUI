import PySimpleGUI as sg

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-highly-responsive-inputs

Às vezes, é desejável começar a processar as informações de entrada quando um usuário faz uma seleção, 
em vez de exigir que o usuário clique em um botão OK.

Digamos que você tenha uma caixa de listagem de entradas e um usuário possa selecionar um item dela.
"""

# # Exemplo com botão OK
# # ====================
choices = ('Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Chartreuse')

layout = [  [sg.Text('Qual a sua cor preferida? Clique OK!!!')],
            [sg.Listbox(choices, size=(15, len(choices)), key='-COLOR-')],
            [sg.Button('Ok')]  ]

window = sg.Window('Escolha uma cor', layout)

while True:                  # the event loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Ok':
        if values['-COLOR-']:    # if something is highlighted in the list
            sg.popup(f"Sua cor favorita é {values['-COLOR-'][0]}")
window.close()

# Exemplo sem botão OK
# ====================
choices = ('Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Chartreuse')

layout = [  [sg.Text('Qual a sua cor preferida?')],
            [sg.Listbox(choices, size=(15, len(choices)), key='-COLOR-', enable_events=True)] ]

window = sg.Window('Escolha uma cor', layout)

while True:                  # the event loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if values['-COLOR-']:    # if something is highlighted in the list
        sg.popup(f"Sua cor favorita é {values['-COLOR-'][0]}")
window.close()