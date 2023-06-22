import PySimpleGUI as sg
import os

"""
    Fonte: https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_User_Settings_Auto_Load_and_Save.py
    
    Demonstração - API de configuração do usuário para salvar e carregar elementos de entrada automaticamente

    Este programa de demonstração mostra uma maneira fácil de adicionar salvamento e carregamento de elementos de entrada.  
    
    A variável keys_to_save é usada para determinar quais elementos serão salvos no arquivo de configurações do usuário.
    
    A função make_key retorna um dicionário usado como parâmetros de palavra-chave que são passados ​​para os elementos Input. 
    O uso dessa técnica permite que os elementos de entrada no layout se beneficiem das docstrings fornecidas pelo PySimpleGUI. 
    Outra abordagem poderia ser usar uma função que retorna um elemento de entrada, mas que 
    limita a flexibilidade para configurar elementos de entrada.
    Copyright 2023 PySimpleGUI
"""
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = __file__.replace(".py", ".json").replace(".pyw", ".json")

window_contents = sg.UserSettings(path=dir_path, 
                                #   filename=filename
                                  )

keys_to_save = ('-IN1-', '-IN2-', '-IN3-', '-IN4-')

def make_key(key):
    """
    Retorna um dicionário que é usado para passar parâmetros para um elemento Input.
    Outra abordagem poderia ser retornar um elemento de entrada. A desvantagem dessa abordagem é
    a falta de parâmetros e docstrings associados ao criar o layout.

    :param key:
    :return: Dict
    """
    # return {'default_text':sg.user_settings_get_entry(key, ''), 'key':key} # carrega do arquivo padrão: \AppData\Local\PySimpleGUI\settings
    return {'default_text':window_contents[key], 'key':key} # carrega do arquivo definido em window_contents



def main():
    layout = [  [sg.Text('Automatically Load and Save Of Inputs', font='_ 15')],
                [sg.Text('Input 1'), sg.Input(**make_key('-IN1-'))],
                [sg.Text('Input 2'), sg.Input(**make_key('-IN2-'), background_color='green')],
                [sg.Text('Input 3'), sg.Input(**make_key('-IN3-'), text_color='blue')],
                [sg.Text('Input 4'), sg.Input(**make_key('-IN4-'), size=5)],
                [sg.Button('Exit (and save)', key='-EXIT SAVE-'), sg.Button('Exit without save')]  ]

    window = sg.Window('Save / Load Inputs Using User Settings API', layout)

    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit without save':
            sg.popup_quick_message('Saindo sem salvar', text_color='white', background_color='red', font='_ 20')
            break
        elif event == '-EXIT SAVE-':
            sg.popup_quick_message('Salvando configurações e saída', text_color='white', background_color='red', font='_ 20')
            for key in keys_to_save:
                # sg.user_settings_set_entry(key, values[key]) # grava no arquivo padrão: \AppData\Local\PySimpleGUI\settings 
                window_contents[key] = values[key] # grava no arquivo definido em window_contents
            break

    window.close()

if __name__ == '__main__':
    main()