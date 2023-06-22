import PySimpleGUI as sg

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-input-validation

Às vezes, você deseja restringir o que um usuário pode inserir em um campo. Talvez você tenha um 
campo de CEP e queira garantir que apenas números sejam inseridos e que não tenham mais de 5 dígitos.

Talvez você precise de um número de ponto flutuante e queira permitir apenas '0-9', '.' e '-'. Uma maneira 
de restringir a entrada do usuário apenas a esses caracteres é obter um evento sempre que o usuário 
inserir um caractere e, se o caractere não for válido, removê-lo.

Você já viu (anteriormente) que para obter um evento imediato quando um elemento interage de alguma forma, 
você define o parâmetro enable_events.
"""

"""
    Restrinja os caracteres permitidos em um elemento de entrada em dígitos e "." ou "-"
    removendo a entrada do último caractere, se não for um caractere válido
"""
layout = [  [sg.Text('Input only floating point numbers')],
            [sg.Input(key='-IN-', enable_events=True)],
            [sg.Button('Exit')]  ]

window = sg.Window('Floating point input validation', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    # if last character in input element is invalid, remove it
    if event == '-IN-' and values['-IN-']:
        try:
            in_as_float = float(values['-IN-'])
        except:
            if len(values['-IN-']) == 1 and values['-IN-'][0] == '-':
                continue
            window['-IN-'].update(values['-IN-'][:-1])
window.close()