"""
A janela One-shot é aquela que aparece, coleta alguns dados e depois desaparece. 
É mais ou menos um 'formulário' destinado a obter rapidamente algumas informações e depois ser fechado.

Este será o padrão mais comum que você seguirá se não estiver usando um "loop de eventos" 
(sem ler a janela várias vezes). A janela é lida e depois fechada.

Quando você "lê" uma janela, é retornada uma tupla que consiste em um event e um dicionário values.

O event é o que causou o retorno da leitura. Pode ser um pressionamento de botão, algum texto clicado, 
um item de lista escolhido, etc, ou WIN_CLOSED se o usuário fechar a janela usando o X.

O values é um dicionário de valores de todos os elementos de estilo de entrada. Os dicionários usam chaves 
para definir entradas. Se seus elementos não especificarem uma chave, uma será fornecida para você. Essas chaves 
numeradas automaticamente são inteiros começando em zero.

Este padrão de design não especifica um key para o elemento InputText, então sua chave será numerada 
automaticamente e é zero neste caso. Assim, o padrão de design pode obter o valor de tudo o que foi inserido 
referenciando values[0]

Fonte: https://www.pysimplegui.org/en/latest/cookbook/#getting-started-copy-these-design-patterns
"""
import PySimpleGUI as sg      

layout = [[sg.Text('Minha janela one-shot.')],      
                 [sg.InputText()],      
                 [sg.Submit('enviar'), sg.Cancel('cancelar')]]      

window = sg.Window('Título da janela', layout)    

event, values = window.read()    
window.close()

text_input = values[0]    
sg.popup('Você entrou', text_input)


"""
Se você quiser usar uma chave em vez de uma chave gerada automaticamente:  
"""
layout = [[sg.Text('Minha janela one-shot.')],      
                 [sg.InputText(key='-IN-')],      
                 [sg.Submit('vai'), sg.Cancel('saída')]]      

window = sg.Window('Título da janela', layout)    

event, values = window.read()    
window.close()

text_input = values['-IN-']    
sg.popup('Você entrou', text_input)

'''
Para uma janela muito mais compacta, é possível criar, exibir, ler e fechar uma janela em uma única linha de código.
'''
event, values = sg.Window('Login Window',
                  [[sg.T('Enter your Login ID'), sg.In(key='-ID-')],
                  [sg.B('OK'), sg.B('Cancel') ]]).read(close=True)

login_id = values['-ID-']
'''
A parte importante deste trecho de código é close=True. Este é o parâmetro que instrui o PySimpleGUI 
a fechar a janela antes que a leitura retorne.

Esta é uma única linha de código, dividida para facilitar a leitura do layout da janela. Ele irá exibir uma janela, 
deixar o usuário inserir um valor, clicar em um botão e então a janela será fechada e a execução será retornada 
para você com as variáveis event ​​e values sendo retornada.

Observe o uso do nome do elemento "Shortcuts" (usa B em vez de Button, T em vez de Text, I nem vez de InputText, etc.). 
Esses atalhos são fantásticos de usar quando você tem layouts complexos. Ser capaz de "ver" toda a definição 
de sua janela em uma única tela de código traz grandes benefícios. É outra ferramenta para ajudá-lo a obter um código simples.
'''