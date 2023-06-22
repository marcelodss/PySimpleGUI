import PySimpleGUI as sg

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-one-element-updating-another-compound-elements
"""
layout = [[sg.Text('Slider Demonstration'), sg.Text('', key='-OUTPUT-')],
          [sg.T('0',size=(4,1), key='-LEFT-'),
           sg.Slider((0,100), key='-SLIDER-', orientation='h', enable_events=True, disable_number_display=True),
           sg.T('0', size=(4,1), key='-RIGHT-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    window['-LEFT-'].update(int(values['-SLIDER-']))
    window['-RIGHT-'].update(int(values['-SLIDER-']))
    if event == 'Show':
        sg.popup(f'The slider value = {values["-SLIDER-"]}')
window.close()