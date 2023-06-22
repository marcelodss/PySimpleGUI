import PySimpleGUI as sg      


"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-pattern-2a-persistent-window-multiple-reads-using-an-event-loop
"""

def one_function(event, values):
    print('one_function', event, values)


sg.theme('DarkAmber') # Mantenha as coisas interessantes para seus usuários

layout = [[sg.Text('Janela persistente')],      
          [sg.Input(key='-IN-')],      
          [sg.Button('Ler'), sg.Exit('Sair')]]      

window = sg.Window('Janela que permanece aberta', layout)      

while True: # O loop de eventos
    event, values = window.read() 
    print('print: ', event, values)       
    one_function(event, values)
    if event == sg.WIN_CLOSED or event == 'Sair':
        break      

window.close()