import PySimpleGUI as sg
import os

"""
    Fonte: https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_User_Settings.py
    Demonstração - Configurações do usuário

    Use as chamadas de API "user_settings" para criar uma "janela de configurações"

    Esta demonstração é muito básica. As funções user_settings são usadas diretamente sem uma tabela de pesquisa
    ou algum outro mecanismo para mapear entre as chaves PySimpleGUI e as chaves de configurações do usuário.
    
    Duas janelas são mostradas. Um é um "salvar nome de arquivo inserido anteriormente" super simples
    A outra é uma "janela de configurações" maior, onde várias configurações são salvas/carregadas
    
    Copyright 2020 PySimpleGUI.org
"""

# SETTINGS_PATH = '.'
SETTINGS_PATH = os.path.dirname(os.path.relpath(__file__))

def make_window():
    """
    Cria uma nova janela. Os valores padrão para alguns elementos são extraídos diretamente do
    "User Settings" sem o uso de variáveis ​​temporárias.

    Algumas chamadas get_entry não têm um valor padrão, como theme, porque houve uma chamada inicial
    que teria definido o valor padrão se a configuração não estivesse presente. Ainda poderia colocar o padrão
    value se você quiser, mas seriam 2 lugares para alterar se você quisesse um valor padrão diferente.

    O uso de uma tabela de pesquisa para mapear entre as chaves do elemento e as configurações do usuário pode ser adicionado. 
    Esta demonstração é feito intencionalmente sem um para mostrar como usar as APIs de configuração da forma mais básica,
    maneira direta.

    Se o seu aplicativo permite alterar o tema, é bom ter uma função make_window para que você possa fechar e recriar uma janela facilmente.
    :return: (sg.Window) A janela que foi criada
    """

    sg.theme(sg.user_settings_get_entry('-theme-', 'DarkBlue2'))  # set the theme

    layout = [[sg.Text('Settings Window')],
              [sg.Input(sg.user_settings_get_entry('-input-', ''), k='-IN-')],
              [sg.Listbox(sg.theme_list(), default_values=[sg.user_settings_get_entry('theme')], size=(15, 10), k='-LISTBOX-')],
              [sg.CB('Option 1', sg.user_settings_get_entry('-option1-', True), k='-CB1-')],
              [sg.CB('Option 2', sg.user_settings_get_entry('-option2-', False), k='-CB2-')],
              [sg.T('Settings file = ' + sg.user_settings_filename())],
              [sg.Button('Save'), sg.Button('Exit without saving', k='Exit')]]

    return sg.Window('A Settings Window', layout)


def settings_window():
    """
    Create and interact with a "settings window". You can a similar pair of functions to your
    code to add a "settings" feature.
    """

    window = make_window()
    current_theme = sg.theme()

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
        if event == 'Save':
            # Save some of the values as user settings
            sg.user_settings_set_entry('-input-', values['-IN-'])
            sg.user_settings_set_entry('-theme-', values['-LISTBOX-'][0])
            sg.user_settings_set_entry('-option1-', values['-CB1-'])
            sg.user_settings_set_entry('-option2-', values['-CB2-'])

        # if the theme was changed, restart the window
        if values['-LISTBOX-'][0] != current_theme:
            current_theme = values['-LISTBOX-'][0]
            window.close()
            window = make_window()


def save_previous_filename_demo():
    """
    Saving the previously selected filename....
    A demo of one of the likely most popular use of user settings
    * Use previous input as default for Input
    * When a new filename is chosen, write the filename to user settings
    """
    # Notice that the Input element has a default value given (first parameter) that is read from the user settings
    layout = [[sg.Text('Enter a filename:')],
              [sg.Input(sg.user_settings_get_entry('-filename-', ''), key='-IN-'), sg.FileBrowse()],
              [sg.B('Save'), sg.B('Exit Without Saving', key='Exit')]]

    window = sg.Window('Filename Example', layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
        elif event == 'Save':
            sg.user_settings_set_entry('-filename-', values['-IN-'])

    window.close()


if __name__ == '__main__':
    sg.user_settings_filename(path=SETTINGS_PATH)  # Set the location for the settings file
    # Run a couple of demo windows
    save_previous_filename_demo()
    settings_window()