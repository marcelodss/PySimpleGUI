import PySimpleGUI as sg

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-persistent-window-with-text-element-updates

Este programa simples mantém uma janela aberta, recebendo valores de entrada até que o 
usuário finalize o programa usando o botão "X".

Esta receita tem vários conceitos. 
* Aliases de nome de elemento - Txt e In são usados ​​no layout 
* Vincule a tecla de retorno para que, em vez de clicar no botão "Calcular", o usuário pressione a tecla de retorno 
* Sem botão de sair/fechar. A janela é fechada usando o "X" 
* try/except para capturar erros com o ponto flutuante 
* Exibindo resultados usando um elemento de texto - Observação: certifique-se de definir o tamanho para um valor grande o suficiente
"""

sg.theme('Dark Green 7')

layout = [ [sg.Txt('Enter values to calculate')],
           [sg.In(size=(8,1), key='-NUMERATOR-')],
           [sg.Txt('_'  * 10)],
           [sg.In(size=(8,1), key='-DENOMINATAOR-')],
           [sg.Txt(size=(8,1), key='-OUTPUT-')  ],
           [sg.Button('Calculate', bind_return_key=True)]]

window = sg.Window('Math', layout)

while True:
    event, values = window.read()

    if event != sg.WIN_CLOSED:
        try:
            numerator = float(values['-NUMERATOR-'])
            denominator = float(values['-DENOMINATAOR-'])
            calc = numerator/denominator
        except:
            calc = 'Invalid'

        window['-OUTPUT-'].update(calc)
    else:
        break