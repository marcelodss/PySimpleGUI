import PySimpleGUI as sg
import sys

"""
Fonte:https://www.pysimplegui.org/en/latest/cookbook/#recipe-add-gui-to-front-end-of-script

Adicione rapidamente uma GUI que permite ao usuário procurar um nome de arquivo se um nome de arquivo 
não for fornecido na linha de comando usando esta GUI simples. É o melhor dos dois mundos. 
Se você quiser linha de comando, pode usá-la. Se você não especificar, a GUI será iniciada.
"""

if len(sys.argv) == 1:
    event, values = sg.Window('Meu script',
                    [[sg.Text('Documento para abrir')],
                    [sg.In(), sg.FileBrowse()],
                    [sg.Open('Abrir'), sg.Cancel('Cancelar')]]).read(close=True)
    fname = values[0]
else:
    fname = sys.argv[1]

if not fname:
    sg.popup("Cancelado", "Nenhum nome de arquivo fornecido")
    raise SystemExit("Cancelamento: Nenhum nome de arquivo fornecido")
else:
    sg.popup('O nome do arquivo que você escolheu foi', fname)