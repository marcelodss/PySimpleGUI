import PySimpleGUI as sg

"""
Fonte: https://pysimplegui.trinket.io/demo-programs#/advanced/focus-events-routing-custom-events-through-window-read

Extending PySimpleGUI using the tkinter event bindings

A idéia aqui é permitir que você receba "eventos" tkinter personalizados que serão 
retornados a você por meio de sua chamada para window.read()

Nesse caso, os eventos desejados são quando uma janela recebe e perde o foco. Este é um recurso 
avançado que a maioria dos aplicativos não precisa, mas é bom saber que está disponível caso você precise.

O mesmo tipo de construção pode ser usado para vincular cliques com o botão direito a botões, por exemplo.

Os elementos e as janelas têm um método de ligação. 
window.bind(tkinter_event_string, key) ou element.bind(tkinter_event_string, key_modifier)
O primeiro parâmetro é a sequência de eventos Tkinter, coisas como <FocusIn> <Button-1> <Button-3> <Enter>
O segundo parâmetro para a janela é uma chave inteira, pois os elementos são algo adicionado a uma chave.  
Essa chave ou chave modificada é o que é retornado quando você lê a janela.
Se o modificador de chave for o texto e a chave for o texto, a chave retornada da leitura será 
os 2 concatenados juntos.  Caso contrário, seu evento será uma tupla que contém o valor key_modifier 
que você passa e a chave pertencente ao elemento que o evento aconteceu.
"""
sg.theme('Dark Blue 3')

layout = [  [sg.Text('Move mouse over me', key='-TEXT-')],
            [sg.In(key='-IN-')],
            [sg.Button('Right Click Me', key='-BUTTON-'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout, finalize=True)

window.bind('<FocusOut>', '+FOCUS OUT+')

window['-BUTTON-'].bind('<Button-3>', '+RIGHT CLICK+')
window['-TEXT-'].bind('<Enter>', '+MOUSE OVER+')
window['-TEXT-'].bind('<Leave>', '+MOUSE AWAY+')
window['-IN-'].bind('<FocusIn>', '+INPUT FOCUS+')

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
window.close()