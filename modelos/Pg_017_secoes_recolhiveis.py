import PySimpleGUI as sg

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-collapsible-sections-visible-invisible-elements

Demo - seções "Collapsible" do Windows

Essa demonstração mostra uma técnica para criar uma seção dobrável (coluna) dentro da sua janela.

Ele usa a função "pin" para que você precise da versão 4.28.0+

Vários "aliases de atalho" são usados nos layouts para compactar um pouco as coisas.    
Caso você não tenha encontrado esses atalhos, o significado é:
B = Button, T = Text, I = Input = InputText, k = key
Além disso, foram utilizados os dois métodos para especificar as cores dos botões (tupla / string única)
A Seção 2 os usa mais para mostrar como é usar nomes mais compactos.

Para abrir/fechar uma seção, clique na seta ou nome da seção.
A seção 2 também pode ser controlada usando a caixa de seleção na parte superior da janela apenas para
Mostre que existem várias maneiras de desencadear eventos como esses.
Copyright 2020 PySimpleGUI.org
"""

SYMBOL_UP =    '▲'
SYMBOL_DOWN =  '▼'

def collapse(layout, key):
    """
    Helper function que cria uma coluna que pode ser deixada mais tarde escondida, aparecendo assim "collapsed"
    :param layout: O layout para a seção
    :param key: Chave usada para tornar esta seção visível / invisível
    :return: Uma coluna fixada (oin) que pode ser colocada diretamente em seu layout
    :rtype: sg.pin
    """
    return sg.pin(sg.Column(layout, key=key))


section1 = [[sg.Input('Input sec 1', key='-IN1-')],
            [sg.Input(key='-IN11-')],
            [sg.Button('Button section 1',  button_color='yellow on green'),
             sg.Button('Button2 section 1', button_color='yellow on green'),
             sg.Button('Button3 section 1', button_color='yellow on green')]]

section2 = [[sg.I('Input sec 2', k='-IN2-')],
            [sg.I(k='-IN21-')],
            [sg.B('Button section 2',  button_color=('yellow', 'purple')),
             sg.B('Button2 section 2', button_color=('yellow', 'purple')),
             sg.B('Button3 section 2', button_color=('yellow', 'purple'))]]


layout =   [[sg.Text('Window with 2 collapsible sections')],
            [sg.Checkbox('Blank checkbox'), sg.Checkbox('Hide Section 2', enable_events=True, key='-OPEN SEC2-CHECKBOX')],
            #### Section 1 part ####
            [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC1-', text_color='yellow'), sg.T('Section 1', enable_events=True, text_color='yellow', k='-OPEN SEC1-TEXT')],
            [collapse(section1, '-SEC1-')],
            #### Section 2 part ####
            [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC2-', text_color='purple'),
             sg.T('Section 2', enable_events=True, text_color='purple', k='-OPEN SEC2-TEXT')],
            [collapse(section2, '-SEC2-')],
            #### Buttons at bottom ####
            [sg.Button('Button1'),sg.Button('Button2'), sg.Button('Exit')]]

window = sg.Window('Visible / Invisible Element Demo', layout)

opened1, opened2 = True, True

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event.startswith('-OPEN SEC1-'):
        opened1 = not opened1
        window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened1 else SYMBOL_UP)
        window['-SEC1-'].update(visible=opened1)

    if event.startswith('-OPEN SEC2-'):
        opened2 = not opened2
        window['-OPEN SEC2-'].update(SYMBOL_DOWN if opened2 else SYMBOL_UP)
        window['-OPEN SEC2-CHECKBOX'].update(not opened2)
        window['-SEC2-'].update(visible=opened2)

window.close()