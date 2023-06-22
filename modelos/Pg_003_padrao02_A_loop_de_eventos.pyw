import PySimpleGUI as sg

'''
fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-pattern-2b-persistent-window-multiple-reads-using-an-event-loop-updates-data-in-window
'''

'''
Esta é uma versão um pouco mais complexa, mas mais realista, que lê a entrada do usuário e exibe essa entrada como texto na janela. 
É provável que seu programa faça essas duas atividades, portanto, esse padrão provavelmente será seu ponto de partida.

Para modificar um elemento em uma janela, você chama seu método update. Isso é feito em 2 etapas. Primeiro você 
pesquisa o elemento, depois chama o método update desse elemento.

A maneira como estamos alcançando a saída aqui é alterando um elemento de texto com esta declaração:

window['-OUTPUT-'].update(values['-IN-'])

window['-OUTPUT-'] retorna o elemento que possui a chave '-OUTPUT-'. Em seguida, o método update para esse elemento é 
chamado para que o valor do elemento de texto seja modificado. Certifique-se de ter fornecido um size que seja grande 
o suficiente para exibir sua saída. Se o tamanho for muito pequeno, a saída será truncada.

Existem dois conceitos importantes ao atualizar elementos!

1- Se você precisar interagir com elementos antes de chamar, window.read() precisará "finalizar" sua janela primeiro 
usando o parâmetro finalize ao criar seu arquivo Window. "Interagir" significa chamar os métodos desse elemento, 
como update, expand, draw_line, etc.

2- Sua alteração não ficará visível na janela até que você:
A. Ligue window.read() novamente
B. Ligue window.refresh()

Dentro do seu loop de eventos
-----------------------------
Para janelas persistentes, depois de criar a janela, você tem um loop de eventos que é executado até você sair da janela. 
Dentro desse loop, você lerá os valores que são retornados da leitura da janela e operará os elementos em sua janela. 
Para operar em elementos, você os procura e chama suas funções de método, como update.

Depois de pesquisar um elemento, a operação executada com mais frequência é update. Existem outros métodos de 
elemento que você pode chamar, como set_tooltip(). Você encontrará  lista de operações disponíveis para cada elemento 
na REFERÊNCIA DE CHAMADA DE ELEMENTO E FUNÇÃO (https://www.pysimplegui.org/en/latest/call%20reference/)

Para chamar qualquer um desses outros métodos, você faz a pesquisa de elemento e, em seguida, adiciona a chamada 
como esta chamada para set_tooltip: window[my_key].set_tooltip('New Tooltip')

OBSERVAÇÃO!
As operações nos elementos não aparecerão na sua janela imediatamente. Se você deseja que eles apareçam imediatamente, 
antes de sua próxima chamada window.read(), você deve ligar window.refresh(). Uma chamada para read ou refresh 
faz com que suas alterações sejam exibidas.

Veja mais:
- Saindo de uma Janela: https://www.pysimplegui.org/en/latest/cookbook/#exiting-a-window
- Convenções de Codificação: https://www.pysimplegui.org/en/latest/cookbook/#coding-conventions
- Navegador de demonstração: https://www.pysimplegui.org/en/latest/cookbook/#recipe-the-demo-browser
- Menu de clique direito simples e padrão: https://www.pysimplegui.org/en/latest/cookbook/#recipe-a-simple-standard-right-click-menu

'''

sg.theme('BluePurple')

layout = [[sg.Text('Seus chars digitados aparecem aqui:'), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Pattern 2B', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # Atualize o elemento de texto "saída" para ser o valor do elemento "entrada"
        window['-OUTPUT-'].update(values['-IN-'])

window.close()