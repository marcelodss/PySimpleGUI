import PySimpleGUI as sg

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-clean-simple-inputs

Entradas de linha única
Muitas de nossas primeiras GUIs envolvem a coleta de pequenos bits de informação e, em seguida, 
continuam com o processamento dessa entrada. 

O mais básico deles são os layouts que possuem um Elemento Text e um Elemento Input. Este é um "formulário" 
básico que o usuário preenche. Talvez você já tenha um código parecido com este.
"""

layout = [  [sg.Text('Simple Inputs')],
            [sg.Text('Name'), sg.Input(key='-NAME-')],
            [sg.Text('Address'), sg.Input(key='-ADDRESS-')],
            [sg.Text('City and State'), sg.Input(key='-CITY AND STATE-')],
            [sg.Ok(), sg.Cancel()]]

window = sg.Window('Simple Inputs', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

window.close()

# =============================================================================
"""
Empurre o seu Input Rows
Uma adição fácil ao seu layout é "empurrar" cada linha de entrada para a direita. O efeito é bastante 
agradável e a implementação envolve uma operação simples - adicione um elemento Push ao início de cada 
linha que tenha um Input
"""
layout = [  [sg.Text('Empurre o seu Input Rows')],
            [sg.Push(), sg.Text('Name'), sg.Input(key='-NAME-')],
            [sg.Push(), sg.Text('Address'), sg.Input(key='-ADDRESS-')],
            [sg.Push(), sg.Text('City and State'), sg.Input(key='-CITY AND STATE-')],
            [sg.Ok(), sg.Cancel()]]

window = sg.Window('Simple Inputs', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break


# =============================================================================
"""
Empurre tudo - element_justification='r'

Se você realmente deseja ser inteligente e economizar tempo também, pode fazer uma alteração 
de 1 parâmetro em sua definição Window e obter um resultado semelhante. A única diferença é que os 
botões também serão empurrados.
"""

layout = [  [sg.Text('Empurre tudo')],
            [sg.Text('Name'), sg.Input(key='-NAME-')],
            [sg.Text('Address'), sg.Input(key='-ADDRESS-')],
            [sg.Text('City and State'), sg.Input(key='-CITY AND STATE-')],
            [sg.Ok(), sg.Cancel()]]

window = sg.Window('Simple Inputs', layout, element_justification='r')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

window.close()