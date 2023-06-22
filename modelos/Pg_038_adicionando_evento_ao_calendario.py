import PySimpleGUI as sg

"""
Duas maneiras de obter data:

- Usando um elemento CalendarButton com um enable_events=True elemento Input, 
o evento será a chave do elemento Input.

Usando um elemento Button geral com um elemento Input, o evento será a chave do elemento Button
para chamar a função popup_get_date e atualizar a data para o elemento Input se a data for selecionada.
"""

layout = [
    # First way
    [sg.Input(readonly=True, enable_events=True, key='INPUT 1'),
     sg.CalendarButton('Calendar 1', close_when_date_chosen=True, format='%d-%m-%Y', key='Calendar 1')],
    # Second way
    [sg.Input(readonly=True, key='INPUT 2'),
     sg.Button('Calendar 2')],
]
window = sg.Window('Calendar Button', layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    print(event)
    if event == 'Input 1':
        print(values[event])
    elif event == 'Calendar 2':
        date = sg.popup_get_date(close_when_chosen=True)
        if date:
            m, d, y = date
            window['INPUT 2'].update(f'{y:0>4d}-{m:0>2d}-{d:0>2d}')

window.close()

# ===============================================================================
"""
A maneira de salvar o valor e obter o evento é criar um campo de entrada oculto. 
Habilite eventos para o campo de entrada e você obterá um evento quando o calendário preencher o campo de entrada definido como destino.
"""

layout = [  [sg.Text('Calendar example')],
            [sg.In(key='-CAL-', enable_events=True, visible=False), sg.CalendarButton('Calendar', target='-CAL-', pad=None, font=('MS Sans Serif', 10, 'bold'),
                button_color=('red', 'white'), key='_CALENDAR_', format=('%d %B, %Y'))],
            [sg.Exit()]]

window = sg.Window('Calendar', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
window.close()