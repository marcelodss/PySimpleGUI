import PySimpleGUI as sg

"""
    Fonte: https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_User_Settings_As_Simple_Database.py
    
    Demonstração - Configurações do usuário como um banco de dados

    As APIs de configurações do usuário PySimpleGUI são implementadas para parecer um dicionário para o
    usuário e utilizar arquivos JSON para armazenar os dados. Como resultado, uma "chave" é usada para
    armazenar e recuperar cada "configuração". Esta capacidade pode ser usada para implementar um
    banco de dados simples.
    
    Nesta demonstração, o arquivo de configurações do usuário é usado para armazenar um ID de usuário e dados associados
    com essa identificação. Cada ID de usuário possui um dicionário armazenado no arquivo de configurações do usuário. Esse
    dicionário é construído a partir do dicionário de valores da janela. Existe uma variável de mapa
    chamado data_map que traduz entre os dois dicionários.
    
    Copyright 2022 PySimpleGUI
"""

def get_id_data(user_setting, id):
    return user_setting[id]

def main():
    # Mapeia entre as teclas usadas nas configurações do usuário e a própria janela
    data_map = {'-name-': '-NAME-', '-password-': '-PASSWORD-', '-dept-': '-DEPT-', '-security-': '-SECURITY-'}
    user_data = sg.UserSettings('my_user_data.json')
    INPUT_SIZE=30
    layout = [  [sg.Text('User ID Management')],
                [sg.Push(), sg.Text('User ID:'), sg.Input(key='-ID-', size=INPUT_SIZE)],
                [sg.Push(), sg.Text('Name:'), sg.Input(key='-NAME-', size=INPUT_SIZE,)],
                [sg.Push(), sg.Text('Password:'), sg.Input(key='-PASSWORD-', size=INPUT_SIZE, password_char='*')],
                [sg.Push(), sg.Text('Department:'), sg.Input(key='-DEPT-', size=INPUT_SIZE,)],
                [ sg.Text('Security Level:'), sg.Combo(('Low', 'Medium', 'High'), size=(INPUT_SIZE-2,3), readonly=True, default_value='Low', key='-SECURITY-')],

                [sg.Button('Add/Update'), sg.Button('Load'), sg.Button('Display'), sg.Button('Exit')]  ]

    window = sg.Window('User Settings as Database', layout)

    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Add/Update':
            # Cria um dicionário de dados para o ID que está sendo adicionado/atualizado com base nos valores da janela
            user = values['-ID-']
            data = {}
            for setting_key, values_key in data_map.items():
                data[setting_key] = values[values_key]
            user_data[user] = data
            sg.popup(f'Added or updated user: {values["-ID-"]}')
        elif event == 'Load':
            user = values['-ID-']
            data = user_data[user]
            for setting_key, values_key in data_map.items():
                value = data[setting_key] if data is not None else ''
                window[values_key].update(value)
        elif event == 'Display':
            user = values['-ID-']
            data = user_data[user]
            output = f'Detailed User Information for ID: {user}\n'
            for setting_key, values_key in data_map.items():
                value = data[setting_key] if data is not None else ''
                output += f'{setting_key} = {value}\n'
            sg.popup_scrolled(output, title='Detailed User Data')
if __name__ == '__main__':
    main()