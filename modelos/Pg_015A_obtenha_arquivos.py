import PySimpleGUI as sg

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-get-2-files-by-browsing

Às vezes, você só precisa obter alguns nomes de arquivo. Navegue para obter 2 nomes de 
arquivo que podem ser comparados. Ao usar Input, o usuário pode usar o botão Procurar para navegar e 
selecionar um arquivo ou pode colar o nome do arquivo diretamente no elemento de entrada.
"""
sg.theme('Light Blue 2')

layout = [[sg.Text('Enter 2 files to comare')],
          [sg.Text('File 1', size=(8, 1)), sg.Input(), sg.FileBrowse()],
          [sg.Text('File 2', size=(8, 1)), sg.Input(), sg.FileBrowse()],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('File Compare', layout)

event, values = window.read()
window.close()
print(f'You clicked {event}')
print(f'You chose filenames {values[0]} and {values[1]}')

"""
Há momentos em que você não deseja exibir o arquivo escolhido e deseja que o programa inicie 
quando o usuário escolher um arquivo. Uma maneira de fazer isso é ocultar o campo de entrada 
preenchido pelo "Botão Procurar". Ao habilitar eventos para o campo de entrada, 
você obterá um evento quando esse campo for preenchido.
"""

sg.theme('Dark Red')

layout = [[sg.Text('Browse to a file')],
          [sg.Input(key='-FILE-', visible=False, enable_events=True), sg.FileBrowse()]]

event, values = sg.Window('File Compare', layout).read(close=True)

print(f'You chose: {values["-FILE-"]}')