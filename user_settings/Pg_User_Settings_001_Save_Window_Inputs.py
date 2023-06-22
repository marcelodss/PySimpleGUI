import PySimpleGUI as sg
import os

"""
    Fonte: https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_User_Setting_Save_Window_Inputs.py
    
    Demo - API de configuração do usuário para salvar e carregar o conteúdo de uma janela

    O PySimpleGUI "API de configurações do usuário" é uma interface simples para JSON e arquivos de configuração.
    Se você está pensando em criar histórias em um arquivo JSON, considere usar o PySimpleGUI
    
    Chamadas de API de configurações do usuário. Eles fazem os arquivos JSON agirem como dicionários. Não há necessidade
    para carregar nem salvar, pois isso é feito para você.

    Existem 2 interfaces para a API de configurações do usuário.
        1. Chamadas de função - sg.user_settings
        2. Objeto UserSettings - Usa uma interface de classe simples

    Observe que usar a interface Objeto/classe não exige que você escreva uma classe. Se você estiver usando
    PySimpleGUI, você já está usando muitos objetos diferentes. Os elementos e a janela são objetos.

    Nesta demonstração, um objeto UserSetting é usado para salvar os valores dos elementos Input em um arquivo JSON.
    Você também pode recarregar os valores do JSON em sua janela.

    Copyright 2022 PySimpleGUI
"""

# Crie um objeto UserSettings. O arquivo JSON será salvo na mesma pasta que este arquivo .py
# window_contents = sg.UserSettings(path='.', filename='mysettings.json')
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = __file__.replace(".py", ".json").replace(".pyw", ".json")

window_contents = sg.UserSettings(path=dir_path, filename=filename)

def main():
    layout = [  [sg.Text('My Window')],
                [sg.Input(key='-IN1-')],
                [sg.Input(key='-IN2-')],
                [sg.Input(key='-IN3-')],
                [sg.Input(key='-IN4-')],
                [sg.Input(key='-IN5-')],
                [sg.Button('Save'), sg.Button('Load'), sg.Button('Exit')]  ]

    window = sg.Window('Save / Load Inputs Using User Settings API', layout)

    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        # Para SALVAR os valores, percorra todos os elementos no dicionário de valores 
        # e salve seus valores
        if event == 'Save':
            for key in values:
                window_contents[key] = values[key]
        # Para CARREGAR valores de um arquivo de configurações em uma janela, 
        # percorra o dicionário de valores e atualize cada elemento
        if event == 'Load':
            for key in values:
                saved_value = window_contents[key]
                window[key].update(saved_value)

    window.close()

if __name__ == '__main__':
    main()