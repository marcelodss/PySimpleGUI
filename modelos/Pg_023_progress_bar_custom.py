import PySimpleGUI as sg

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-custom-progress-meter-progress-bar
"""

sg.theme('Default1')

BAR_MAX = 1000

def progress_bar():
    for i in range(1000):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = window.read(timeout=10)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            window['-PROG-'].update(0)
            break
            # update bar with loop value +1 so that bar eventually reaches the maximum
        window['-PROG-'].update(i+1)
# done with loop... need to destroy the window as it's still open

# layout the Window
layout = [[sg.Text('A custom progress meter')],
          [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,20), key='-PROG-')],
          [sg.Button('Barra de progresso', key="Bar"), sg.Cancel()]]

# create the Window
window = sg.Window('Custom Progress Meter', layout, keep_on_top=True)
# loop that would normally do something useful

while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Bar':
        progress_bar()

# for i in range(1000):
#     # check to see if the cancel button was clicked and exit loop if clicked
#     event, values = window.read(timeout=10)
#     if event == 'Cancel' or event == sg.WIN_CLOSED:
#         break
#         # update bar with loop value +1 so that bar eventually reaches the maximum
#     window['-PROG-'].update(i+1)
# # done with loop... need to destroy the window as it's still open


window.close()