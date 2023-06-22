import PySimpleGUI as sg

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-one_line_progress_meter
"""

limite = 1000

def Bar1(limite=limite):
    for i in range(int(limite/10)):   # this is your "work loop" that you want to monitor
        sg.one_line_progress_meter('Bar 1 SEM Cancel', i + 1, int(limite/10), keep_on_top=True)

def Bar2(limite=limite):
    for i in range(limite):   # this is your "work loop" that you want to monitor
        if not sg.one_line_progress_meter('Bar 2', i + 1, limite,'COM Cancel - Gerado pelo usuário', i*300, orientation='h', keep_on_top=True):
            break

def Bar3(limite=limite):
    for i in range(limite):   # this is your "work loop" that you want to monitor
        if not sg.one_line_progress_meter('Bar 3 COM Cancel - Programa Gerado', i + 1, limite,keep_on_top=True):
            break

        # after 500 iterations, cancel the meter
        if i == 500:
            sg.one_line_progress_meter_cancel()
            sg.popup('Cancelado!', keep_on_top=True)
            break

sg.theme('Default1')

layout = [[sg.Text('Barra de Progresso')],
          [sg.Button('Bar 1', key="Bar1"), sg.Button('Bar 2', key="Bar2"), sg.Button('Bar 3', key="Bar3"), sg.Button('Exit')]]

window = sg.Window('Barra de Progresso', layout, keep_on_top=True)

while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Bar1':
        Bar1()
    if event == 'Bar2':
        Bar2()
    if event == 'Bar3':
        Bar3()

window.close()
