import PySimpleGUI as sg

layout = [
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('Date', size=(15,1)),            sg.InputText(key='Date'),
     sg.CalendarButton("Select Date", close_when_date_chosen=True, target="Date", format='%d/%m:%Y', size=(10,1))],
    [sg.Text('Service ID', size=(15,1)),     sg.InputText(key='Msisdn'),],
    [sg.Text('Account Number', size=(15,1)), sg.InputText(key='Account')],
    [sg.Text('Customer Name', size=(15,1)),  sg.InputText(key='Customer')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window = sg.Window('Case entry form', layout)

def clear_input(window):
    for key, element in window.key_dict.items():
        if isinstance(element, sg.Input):
            element.update(value='')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    print(values)
    if event == 'Clear':
        clear_input(window)

window.close()