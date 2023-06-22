import PySimpleGUI as sg

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-callback-function-simulation
"""

sg.theme('Light Blue 3')
# This design pattern simulates button callbacks
# This implementation uses a simple "Dispatch Dictionary" to store events and functions

# The callback functions
def button1():
    print('Callback Botão 1')

def button2():
    print('Botão 2 Callback')

# Lookup dictionary that maps button to function to call
dispatch_dictionary = {'1':button1, '2':button2}

# Layout the design of the GUI
layout = [[sg.Text('Clique em um botão', auto_size_text=True)],
          [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Quit()]]

# Show the Window to the user
window = sg.Window('Exemplo de retorno de chamada do botão', layout)

# Event loop. Read buttons, make callbacks
while True:
    # Read the Window
    event, value = window.read()
    if event in ('Quit', sg.WIN_CLOSED):
        break
    # Lookup event in function dictionary
    if event in dispatch_dictionary:
        func_to_call = dispatch_dictionary[event]   # get function from dispatch dictionary
        func_to_call()
    else:
        print('Não há evento {} no dispatch_dictionary'.format(event))

window.close()

    # All done!
sg.popup_ok('Done')