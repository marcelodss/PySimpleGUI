import PySimpleGUI as sg

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-printing
"""

# =============================================================================
# Imprimir para Elemento Output
"""
Se você deseja redirecionar seu padrão para sua janela, colocar um elemento Outpu tem seu layout fará 
exatamente isso. Quando você chamar "print", seu texto será roteado para esse elemento Output. Observe que 
você só pode ter 1 deles em seu layout porque há apenas 1 stdout.

De todas as técnicas de "impressão", esta é a melhor a ser usada se você não puder alterar suas 
instruções de impressão. O elemento Output é a melhor escolha se suas impressões estiverem em outro módulo 
sobre o qual você não tem controle, de modo que "redefinir / reatribuir" o que print faz não seja uma possibilidade.

Este layout com um elemento Output mostra os resultados de alguns cliques do botão Print.
"""

layout = [  [sg.Text('O que você imprimirá será exibido abaixo:')],
            [sg.Output(size=(50,10), key='-OUTPUT-')],
            [sg.In(key='-IN-')],
            [sg.In(key='-IN2-')],
            [sg.Button('Print'), sg.Button('Print2'), sg.Button('Clear'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values, 'Print e Print2')
    print("Algo ")
    if event == "Print2":
        print(event, values, 'Print2')
        print("Algo Print2")
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Clear':
        window['-OUTPUT-'].update('')
        print(event, values, 'Print e Clear')
        print('Algo e Clear')
window.close()

# =============================================================================
# Imprimir para Element Multiline
"""
A partir da versão 4.18.0, você pode "imprimir" em qualquer elemento Multiline em seus layouts. 
O método Multiline.print age de forma semelhante à função Print descrita anteriormente. Possui os 
parâmetros normais de impressão sep e end; também possui opções de cores. É como uma declaração print super carregada.

"Converter" instruções de impressão exprint para saída para um elemento Multiline pode ser feito:
- Adicionando o elemento Multiline à declaração print para que ele chame o método Multiline.print
- redefinindo print

Foi adicionado na versão 4.25.0 a capacidade de reencaminhar stdout e stderr diretamente para qualquer elemento Multiline. 
Isso é feito usando parâmetros quando você cria a multilinha ou pode chamar métodos de classe para fazer a operação 
de reencaminhamento após a criação do elemento.

Como nem sempre é possível ter acesso à janela ao imprimir, especialmente em códigos que não são seus, 
outro parâmetro foi adicionado: auto_refresh. Se definido como True, a janela será atualizada 
automaticamente toda vez que uma atualização for feita nesse elemento Multiline.
"""
layout = [  [sg.Text('Demonstration of Multiline Element Printing')],
            [sg.MLine(key='-ML1-'+sg.WRITE_ONLY_KEY, size=(40,8))],
            [sg.MLine(key='-ML2-'+sg.WRITE_ONLY_KEY,  size=(40,8))],
            [sg.Button('Go'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout, finalize=True)


# Note, need to finalize the window above if want to do these prior to calling window.read()
window['-ML1-'+sg.WRITE_ONLY_KEY].print(1,2,3,4,end='', text_color='red', background_color='yellow')
window['-ML1-'+sg.WRITE_ONLY_KEY].print('\n', end='')
window['-ML1-'+sg.WRITE_ONLY_KEY].print(1,2,3,4,text_color='white', background_color='green')
counter = 0

while True:             # Event Loop
    event, values = window.read(timeout=100)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Go':
        window['-ML1-'+sg.WRITE_ONLY_KEY].print(event, values, text_color='red')
    window['-ML2-'+sg.WRITE_ONLY_KEY].print(counter)
    counter += 1
window.close()