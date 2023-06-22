import PySimpleGUI as sg
import time

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-long-operations-multi-threading
"""
def func(win, index, teste):
    for i in range(0, 51):
        print(teste, i)
        time.sleep(0.1)
        win.write_event_value('Update', (f'P{index}', i))

sg.theme('DarkBlue3')
layout = [
    [sg.Text('', size=(50, 1), relief='sunken', font=('Courier', 11), text_color='yellow', background_color='black',key=f'P{i}')] for i in (1, 2)] + [
    [sg.Button('Start')],
]
window = sg.Window("Title", layout, keep_on_top=True)
sg.theme('DarkBlue4')

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Start':
        window['Start'].update(disabled=True)
        window['P1'].update('')
        window['P2'].update('')
        window.perform_long_operation(lambda win=window, index=1, teste='a: ':func(win, index, teste), "P1 Done")
    elif event == "P1 Done":
        if sg.popup_yes_no("Step 2 ?") == 'Yes':
            window.perform_long_operation(lambda win=window, index=2, teste='b':func(win, index, teste), "P2 Done")
        else:
            window['Start'].update(disabled=False)
    elif event == "P2 Done":
        window['Start'].update(disabled=False)
    elif event == 'Update':
        key, i = values[event]
        window[key].update('█'*i)

window.close()