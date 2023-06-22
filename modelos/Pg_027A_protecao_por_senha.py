import PySimpleGUI as sg

"""
Fonte: https://pysimplegui.trinket.io/demo-programs#/examples-for-reddit-posts/login

Solicita um nome de usuário e uma senha. A senha é protegida contra visualização durante a digitação.

Você pode usar a tecla Return ou o botão de login para enviar as informações inseridas.
"""

layout = [[sg.Text('Username:'), sg.Push(), sg.Input(key='-USER-')],
          [sg.Text('Password'), sg.Push(), sg.Input(password_char='*', key='-PW-')],
          [sg.Button('Login', bind_return_key=True), sg.Button('Quit')]  ]

window = sg.Window('Login', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    if event == 'Login':
        sg.popup(f'Username = {values["-USER-"]}\nPassword = {values["-PW-"]}', title='You Entered')

window.close()