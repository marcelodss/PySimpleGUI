import PySimpleGUI as sg

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-element-justification-and-alignment

Existem 2 termos usados ​​no PySimpleGUI em relação ao posicionamento: 
* Justificação - Posicionamento no eixo horizontal (esquerda, centro, direita) 
* Alinhamento - Posicionamento no eixo vertical (topo, meio, baixo)

Justificação
A justificação de elementos pode ser realizada usando 2 métodos.
1. Use um elemento de coluna com o parâmetro element_justification 
2. Use o elemento Push

O Push foi adicionado em 2021 à porta tkinter. A porta PySimpleGUIQt já possui um elemento chamado 
Stretch que funciona de maneira semelhante. Você poderia dizer que Push é um alias para Stretch, 
embora Stretch não fosse um elemento tkinter anteriormente.

Push
A maneira de pensar sobre os elementos Push é pensar neles como um elemento que "repele" ou 
empurra outros elementos. Push trabalha em uma base de linha por linha. Cada linha que você deseja impactar 
com Push precisará ter um ou mais elementos Push nessa linha.

Normalmente, cada linha é justificada à esquerda em PySimpleGUI (a menos que você tenha definido um parâmetro no 
objeto Window ou a linha esteja em um elemento Column que tenha uma configuração que afete a justificação.

Pense nas laterais de uma janela como uma parede que não pode se mover. Os elementos podem se mover, 
mas as paredes laterais não. Se você colocar um elemento Push no lado esquerdo de outro elemento, ele "empurrará"
o elemento para a direita. Se você colocar um Push no lado direito, ele "empurrará" o elemento para a esquerda. 
Se você usar DOIS elementos Push e colocar um em cada lado de um elemento, o elemento será centralizado.

Esta receita demonstra o uso de um elemento Push para criar linhas com justificação diferente acontecendo em cada linha.

A primeira linha do layout tem 50 caracteres para que a janela seja larga o suficiente para que a justificação 
de cada linha tenha algum espaço para se mover.

A segunda linha não precisa de um elemento Push para que o elemento seja justificado à esquerda. 
No entanto, se toda a sua janela estiver justificada à direita, usar o Push no lado direito de um 
elemento fará com que ela seja justificada à esquerda.

Observe a última linha do layout. Existem 2 botões juntos com um Push em cada lado. Isso faz com que esses 
2 botões fiquem centralizados.
"""

layout = [[sg.Text('*'*50)],
          [sg.Text('Justificado à esquerda'), sg.Push()],
          [sg.Push(), sg.Text('Justificado à direita')],
          [sg.Push(), sg.Text('Centro justificado'), sg.Push()],
          [sg.Push(), sg.Button('Ok'), sg.Button('Cancel'), sg.Push()]]

window = sg.Window('Elemento push', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

window.close()