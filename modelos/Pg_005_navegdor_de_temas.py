import PySimpleGUI as sg

"""
    Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-theme-browser

    Permite que você "navegue" através das configurações do tema. Clique em um e você verá um
    Janela pop-up usando o esquema de cores que você escolheu.É um pequeno programa simples que também demonstra
    quão rápido a GUI pode se sentir se você ativar os eventos de um elemento, em vez de esperar um clique no botão.
    Neste programa, assim que uma entrada da ListBox for clicada, a leitura retorna.
"""

sg.theme('Dark Brown')


layout = [[sg.Text('Theme Browser')],
          [sg.Text('Clique em uma cor do tema para ver a janela de demonstração')],
          [sg.Listbox(values=sg.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)],
          [sg.Button('Exit')]]

window = sg.Window('Theme Browser', layout)

while True:  # Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    sg.theme(values['-LIST-'][0])
    sg.popup_get_text('Isso é {}'.format(values['-LIST-'][0]))

window.close()