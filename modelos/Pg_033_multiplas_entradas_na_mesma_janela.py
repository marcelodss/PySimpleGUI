import PySimpleGUI as sg

"""
For Reddit - Input a value, then enter another 3 more into same input box. Store in a list

Fonte: https://pysimplegui.trinket.io/demo-programs#/examples-for-reddit-posts/multiple-entry-in-same-window

Aqui está um pequeno programa de demonstração em resposta a este pedido de ajuda no Reddit:
https://www.reddit.com/r/learnprogramming/comments/h884vg/is_there_any_easy_gui_maker_for_python/

A ideia é obter um valor inicial em uma caixa de entrada e, em seguida, obter mais 3 valores na mesma caixa.
Nesta implementação, você pode pressionar o botão "Enter" ou a tecla Enter para inserir um valor.
O resultado é colocado em uma única lista que é mostrada no final.
"""

layout = [  [sg.Text('Multiple Data Entry')],
            [sg.Text('Initial Value', justification='r', size=(12,1), key='-TEXT-'), sg.Input(size=(8,1),do_not_clear=False, key='-IN-')],
            [sg.Button('Enter', bind_return_key=True), sg.Button('Exit')]  ]

window = sg.Window('Muleiple Data Entry', layout)

counter = 0
stuff_entered = []
while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Enter':
        stuff_entered.append(values['-IN-'])
        if counter > 2:
            break
        window['-TEXT-'].update(f'Input Value {counter+1}')
        counter += 1

window.close()
sg.popup(f'You entered {stuff_entered}')
