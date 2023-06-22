import PySimpleGUI as sg

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-exception-handling-of-a-console-less-application
"""
def inicio():
    layout = [  [sg.Text('My Window')],
                [sg.Input(key='-IN-')],
                [sg.Button('Go'), sg.Button('Exit')]  ]

    window = sg.Window('Window Title', layout)

    try:
        while True:             # Event Loop
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            if event == 'Go':
                bad_call()
    except Exception as e:
        # sg.Print('Exceção no meu loop de eventos para o programa:', f'\n\n{sg.__file__}', f'\n\n{e}', keep_on_top=True, wait=True)
        sg.Print('Exceção no meu loop de eventos para o programa:', f'\n\n{sg.__file__}', f'\n\n{e}', keep_on_top=True)
        sg.popup_error_with_traceback('Problema no meu loop de evento!', e)

    window.close()

if __name__ == '__main__':
    inicio()