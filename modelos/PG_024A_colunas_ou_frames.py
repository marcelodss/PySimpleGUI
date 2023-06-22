import PySimpleGUI as sg

"""
Fonte: https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Column_And_Frames.py

Demo sg.Columns e sg.Frames

Demonstra o uso da mistura de elementos SG.Column e SG.Frame para criar um bom layout da janela.
Alguns dos conceitos mostrados aqui incluem:
* Usando sg.columns e sg.frames com tamanhos específicos
* Botões que têm o mesmo texto que são diferenciados usando chaves explícitas
* Uma maneira de codificar o tamanho de um quadro é codificar o tamanho de uma coluna dentro do quadro

    CUIDADO:
O uso de tamanhos explícitos nos elementos da coluna e da estrutura pode não ter o mesmo efeito em
todos os computadores. Às vezes, as partes de hard-code dos layouts não podem ter o mesmo 
resultado em todos os computadores.    
Existem 3 sg.columns. Dois estão lado a lado na parte superior e o terceiro está ao longo da parte inferior
    
Quando houver várias colunas consecutivas, esteja ciente de que o padrão é que essas colunas sejam
alinhado ao longo do centro. Se você quer que eles sejam top-aligned, Então você precisa usar o
função auxiliar vtop para que isso aconteça.

Copyright 2021 PySimpleGUI
"""

col2 = sg.Column([[sg.Frame('Accounts:', [[sg.Column([[sg.Listbox(['Account '+str(i) for i in range(1,16)],
                                                      key='-ACCT-LIST-',size=(15,20)),]],size=(150,400))]])]],pad=(0,0))

col1 = sg.Column([
    # Categories sg.Frame
    [sg.Frame('Categories:',[[ sg.Radio('Websites', 'radio1', default=True, key='-WEBSITES-', size=(10,1)),
                            sg.Radio('Software', 'radio1', key='-SOFTWARE-',  size=(10,1))]],)],
    # Information sg.Frame
    [sg.Frame('Information:', [[sg.Text(), sg.Column([[sg.Text('Account:')],
                             [sg.Input(key='-ACCOUNT-IN-', size=(19,1))],
                             [sg.Text('User Id:')],
                             [sg.Input(key='-USERID-IN-', size=(19,1)),
                              sg.Button('Copy', key='-USERID-')],
                             [sg.Text('Password:')],
                             [sg.Input(key='-PW-IN-', size=(19,1)),
                              sg.Button('Copy', key='-PASS-')],
                             [sg.Text('Location:')],
                             [sg.Input(key='-LOC-IN-', size=(19,1)),
                              sg.Button('Copy', key='-LOC-')],
                             [sg.Text('Notes:')],
                             [sg.Multiline(key='-NOTES-', size=(25,5))],
                             ], size=(235,350), pad=(0,0))]])], ], pad=(0,0))

col3 = sg.Column([[sg.Frame('Actions:',
                            [[sg.Column([[sg.Button('Save'), sg.Button('Clear'), sg.Button('Delete'), ]],
                                        size=(450,45), pad=(0,0))]])]], pad=(0,0))

# The final layout is a simple one
layout = [[col1, col2],
          [col3]]

# A perhaps better layout would have been to use the vtop layout helpful function.
# This would allow the col2 column to have a different height and still be top aligned
# layout = [sg.vtop([col1, col2]),
#           [col3]]


window = sg.Window('Columns and Frames', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break

window.close()