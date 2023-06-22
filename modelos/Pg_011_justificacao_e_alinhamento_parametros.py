import PySimpleGUI as sg

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-element-justification-and-alignment

Você pode usar elementos de contêiner (Column, Frame, Tab and Window também) para justificar várias 
linhas por vez. O parâmetro element_justification controla como os elementos dentro de um contêiner 
ou janela são justificados.

Neste exemplo, todos os elementos da janela estão centralizados
"""

layout = [[sg.Text('*'*50)],
          [sg.Text('Todos os elementos centralizados')],
          [sg.Button('Ok'), sg.Button('Cancel')]]

window = sg.Window('Elemento Justificado', layout, element_justification='c')

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

window.close()

# ###############################################################################

"""
Alinhamento - linhas únicas

"Alinhamento" é o termo usado para descrever o posicionamento vertical dos elementos. Dentro de uma única linha, o 
alinhamento é executado usando um elemento contêiner ou usando uma das "layout helper functions" de alinhamento. 
Você encontrará as funções auxiliares de layout na documentação de referência de chamada aqui:
https://pysimplegui.readthedocs.io/en/latest/call%20reference/#layout-helper-funcs

Existem 3 funções em particular que afetam o posicionamento vertical:
* vtop - Alinha um elemento ou uma linha inteira ao "topo" da linha 
* vbottom - Alinha um elemento ou uma linha inteira ao "fundo" da linha 
* vcenter - Alinhe um elemento ou uma linha inteira ao "centro" da linha

Por padrão, o alinhamento em cada linha é centralizado.

Este programa usa o alinhamento padrão que centralizará os elementos em cada linha.
"""

layout = [[sg.Listbox(list(range(10)), size=(5,5)), sg.Multiline(size=(25,10))],
          [sg.Button('Ok'), sg.Button('Cancel')]]

window = sg.Window('Alinhamento de elementos', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

window.close()

# ###############################################################################
"""
Se você quiser ter a caixa de listagem e a multilinha alinhadas na parte superior, use a função auxiliar vtop. 
Como a caixa de listagem tem a altura mais curta, você pode adicionar vtop apenas a esse elemento. Ou você pode 
usar vtop e passar a linha inteira para que eles permaneçam alinhados no topo, se o tamanho de um desses elementos 
mudar no futuro e o o Multiline seja mais curto.

Abaixo estão 3 maneiras de realizar esta operação.
"""

# Alinhe apenas o único elemento
# ==============================
layout = [
          [sg.Text('Alinhe apenas o Listbox')],
          [sg.vtop(sg.Listbox(list(range(10)), size=(5,5))), sg.Multiline(size=(25,10))],
          [sg.Button('Ok'), sg.Button('Cancel')]]

window = sg.Window('Alinhamento de elementos', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

window.close()

# Alinhar toda a linha
# ====================

layout = [     
          [sg.Text('Alinhe toda a linha')],
          sg.vtop([sg.Listbox(list(range(10)), size=(5,5)), sg.Multiline(size=(25,10))]),
          [sg.Button('Ok'), sg.Button('Cancel')]]

window = sg.Window('Element Alignment', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

window.close()

"""
Observe como usar vtop no exemplo acima substitui toda a linha apenas pela chamada vtop. A razão para isso é 
que a função  vtopretorna uma lista (ou seja, uma linha). Isso significa que colchetes não são necessários. 
Mas parece um pouco estranho e torna mais difícil ver onde estão as linhas.

As versões mais recentes do PySimpleGUI permitem um conjunto extra de colchetes [ ]
para que o layout pareça ainda ser uma lista por linha.
"""

layout = [
          [sg.Text('vtop com CONCHETES')],
          [sg.vtop([sg.Listbox(list(range(10)), size=(5,5)), sg.Multiline(size=(25,10))])],
          [sg.Button('Ok'), sg.Button('Cancel')]]

window = sg.Window('Alinhamento de elementos', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

window.close()

"""
Alinhamento - VPush

Assim como o elemento Push "empurra" os elementos de maneira horizontal, o elemento 
VPush empurra grupos inteiros de linhas para cima e para baixo dentro do contêiner em que estão.

Se você tiver um único VPush em seu layout, o layout será empurrado para cima ou para baixo. Normalmente, 
os layouts são alinhados para cima por padrão, portanto, não há necessidade de ter um único VPush na parte inferior. 
Se você tiver dois elementos VPush, ele centralizará os elementos entre eles.

Um dos melhores exemplos de uso VPush é quando o tamanho de uma janela foi codificado. 
Codificar o tamanho de uma janela não é recomendado em PySimpleGUI. O motivo é que o conteúdo interno 
pode não caber no tamanho codificado em alguns computadores. Geralmente é melhor permitir que o tamanho 
da janela "flutue" e seja dimensionado automaticamente para caber no conteúdo.

Talvez um exemplo melhor seria se você quisesse permitir que sua janela fosse redimensionada e tivesse o conteúdo 
alinhado verticalmente após o redimensionamento.

Mas, se você está determinado a codificar um tamanho e deseja centralizar verticalmente seus elementos nessa janela, 
esse VPush é um bom caminho a seguir.

Esta janela de exemplo tem 300 pixels por 300 pixels. O layout é justificado ao centro e alinhado ao centro. 
Isso é feito usando uma combinação de elementos Push e VPush.
"""

layout = [[sg.VPush()],
          [sg.Push(), sg.Text('VPush: Centralizado na janela'), sg.Push()],
          [sg.Push(), sg.Button('Ok'), sg.Button('Cancel'), sg.Push()],
          [sg.VPush()]]

window = sg.Window('VPush', layout, resizable=True, size=(300, 300))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

