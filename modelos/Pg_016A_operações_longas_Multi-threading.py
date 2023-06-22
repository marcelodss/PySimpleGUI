import PySimpleGUI as sg
import time
import datetime

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-long-operations-multi-threading

As etapas básicas usando perform_long_operation:
 1. Passe o nome da função e uma chave para a chamada para window.perform_long_operation 
 2. Continue executando o loop de eventos da GUI 
 3. Windows pend usando sua window.read() chamada típica 4. 
 Você obterá o evento quando sua função retornar 
 5. O values dicionário irá contém o valor de retorno da sua função. 
 A chave será a mesma do evento. Então, values[event] é o valor de retorno da sua função.

Se você precisar passar parâmetros para sua função, precisará fazer uma 
alteração simples ... adicionar um lambda.

"""

# My function that takes a long time to do...
def my_long_operation(a):
    print(a, datetime.datetime.now())
    time.sleep(10)
    return f'My return value'


def main():
    layout = [  [sg.Text('My Window')],
                [sg.Input(key='-IN-')],
                [sg.Text(key='-OUT-')],
                [sg.Button('Go'), sg.Button('Threaded'), sg.Button('Dummy')]  ]

    window = sg.Window('Window Title', layout, keep_on_top=True)

    while True:             # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        window['-OUT-'].update(f'{event, values}')  # show the event and values in the window
        window.refresh()                            # make sure it's shown immediately

        if event == 'Go':
            return_value = my_long_operation("AAAA")
            window['-OUT-'].update(f'direct return value = {return_value}')
        elif event  == 'Threaded':
            # Let PySimpleGUI do the threading for you...
            window.perform_long_operation(lambda a='lambda':my_long_operation("BBBB"), "-OPERATION DONE-")
        elif event  == '-OPERATION DONE-':
            window['-OUT-'].update(f'indirect return value = {values[event]}')

    window.close()

if __name__ == '__main__':
    main()