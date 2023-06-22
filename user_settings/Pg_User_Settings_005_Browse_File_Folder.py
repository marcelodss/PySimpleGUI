import PySimpleGUI as sg

"""
    Fonte: https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_User_Settings_Auto_Load_and_Save.py
    
    Demonstração de uma janela de entrada de arquivo/pasta melhor

    Essa construção é muito comum em PySimpleGUI.
        [sg.InputText(size=(50,1), key='-FILENAME-'), sg.FileBrowse()],

    As novas APIs de configurações do usuário podem melhorar significativamente a experiência. Agora ao invés de ser
    mostrado um elemento de entrada em branco, o usuário vê sua entrada anterior e um histórico de sua
    entradas anteriores para escolher.

    Dois novos recursos são apresentados nesta demonstração
    1. Recuperando a última entrada
    2. Recuperar um histórico de todas as entradas anteriores como um Combo em vez de um Elemento de entrada

    As operações anteriores que você está acostumado permanecem. Você pode colar um nome de arquivo/caminho completo no combo.
    Você também pode usar o botão de navegação como antes.

    Mas você também obtém os 2 recursos do histórico - última entrada usada, lista de opções anteriores.

    Se sua janela não for de one-shot, adicione um loop de evento em vez de uma leitura com parâmetro de fechamento

    Copyright 2020 PySimpleGUI.org
"""

# ------------------- The Old Way -------------------
layout = [[sg.Text('The Old Way')],
          [sg.InputText(size=(50, 1), key='-FILENAME-'), sg.FileBrowse()],
          [sg.Button('Go'), sg.Button('Exit')]]

event1, values1 = sg.Window('Normal Filename', layout).read(close=True)

# ------------------- The New Way with history -------------------
layout = [[sg.Text('The New Way with history')],
          [sg.Combo(sg.user_settings_get_entry('-filenames2-', []), default_value=sg.user_settings_get_entry('-last filename2-', ''), size=(50, 1), key='-FILENAME-'),
           sg.FileBrowse()],
          [sg.Button('Go'), sg.Button('Exit')]]

event, values = sg.Window('Filename with History', layout).read(close=True)

if event == 'Go':
    sg.user_settings_set_entry('-filenames2-', list(set(sg.user_settings_get_entry('-filenames2-', []) + [values['-FILENAME-'], ])))
    sg.user_settings_set_entry('-last filename2-', values['-FILENAME-'])

# ------------------- The New Way with history and clear -------------------
layout = [[sg.Text('The New Way with history and clear')],
          [sg.Combo(sg.user_settings_get_entry('-filenames3-', []), default_value=sg.user_settings_get_entry('-last filename3-', ''), size=(50, 1), key='-FILENAME-'),
           sg.FileBrowse()],
          [sg.Button('Go'), sg.B('Clear'), sg.Button('Exit')]]

window = sg.Window('Filename History Clearable', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Go':
        sg.user_settings_set_entry('-filenames3-', list(set(sg.user_settings_get_entry('-filenames3-', []) + [values['-FILENAME-'], ])))
        sg.user_settings_set_entry('-last filename3-', values['-FILENAME-'])
        window['-FILENAME-'].update(values=list(set(sg.user_settings_get_entry('-filenames3-', []))))
    elif event == 'Clear':
        sg.user_settings_set_entry('-filenames3-', [])
        sg.user_settings_set_entry('-last filename3-', '')
        window['-FILENAME-'].update(values=[], value='')