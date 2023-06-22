import PySimpleGUI as sg

"""
Fonte: https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Combo_Filechooser_With_History_And_Clear.py

Demo Combo File Chooser - with clearable history

Este é um padrão de design que é muito útil para programas que você executa com frequência que requer
um nome de arquivo será inserido. Você tem 4 opções a serem usadas para obter seu nome de arquivo com este padrão:
1. Copie e cole um nome de arquivo no elemento combinado
2. Use o último item usado que será visível quando você criar a janela
3. Escolha um item na lista de itens usados anteriormente
4. Navegue por um novo nome

Para limpar a lista de entradas anteriores, clique no botão "Limpar histórico".

O histórico é armazenado em um arquivo JSON usando as APIs de configurações de usuário do PysimpleGui

O código é o mais esparso possível para permitir fácil integração em seu código.

Copyright 2021 PySimpleGUI
"""



layout = [[sg.Combo(sorted(sg.user_settings_get_entry('-filenames-', [])), default_value=sg.user_settings_get_entry('-last filename-', ''), size=(50, 1), key='-FILENAME-'), sg.FileBrowse(), sg.B('Clear History')],
          [sg.Button('Ok', bind_return_key=True),  sg.Button('Cancel')]]

window = sg.Window('Filename Chooser With History', layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if event == 'Ok':
        # If OK, then need to add the filename to the list of files and also set as the last used filename
        sg.user_settings_set_entry('-filenames-', list(set(sg.user_settings_get_entry('-filenames-', []) + [values['-FILENAME-'], ])))
        sg.user_settings_set_entry('-last filename-', values['-FILENAME-'])
        break
    elif event == 'Clear History':
        sg.user_settings_set_entry('-filenames-', [])
        sg.user_settings_set_entry('-last filename-', '')
        window['-FILENAME-'].update(values=[], value='')

window.close()