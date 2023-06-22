import PySimpleGUI as sg
import os.path

"""
Fonte: https://pysimplegui.trinket.io/demo-programs#/examples-for-reddit-posts/choose-file-from-a-list
Um padrão de demonstração útil para você seguir caso deseje uma interface de usuário com uma lista 
de arquivos ao longo da borda esquerda e algo feito com esses arquivos no lado direito da janela.

Este é um layout PySimpleGUI altamente "responsivo" no sentido de que agirá imediatamente quando o 
usuário interagir com a janela. Você não precisa clicar em um botão para indicar que uma escolha foi feita. 
Você também pode colar o caminho da pasta na caixa de entrada e a caixa de listagem será imediatamente 
preenchida com o conteúdo da pasta correta.
"""

# --------------------------------- Define Layout ---------------------------------

# First the window layout...2 columns

left_col = [[sg.Text('Folder'), sg.In(size=(25,1), enable_events=True ,key='-FOLDER-'), sg.FolderBrowse()],
            [sg.Listbox(values=[], enable_events=True, size=(40,20),key='-FILE LIST-')]]

# For now will only show the name of the file that was chosen
images_col = [[sg.Text('You choose from the list:')],
              [sg.Text(size=(40,1), key='-TOUT-')],
              [sg.Image(key='-IMAGE-')]]

# ----- Full layout -----
layout = [[sg.Column(left_col), sg.VSeperator(), sg.Column(images_col)]]

# --------------------------------- Create Window ---------------------------------
window = sg.Window('Image Viewer', layout)

# ----- Run the Event Loop -----
# --------------------------------- Event Loop ---------------------------------
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == '-FOLDER-':                     # Folder name was filled in, make a list of files in the folder
        folder = values['-FOLDER-']
        try:
            file_list = os.listdir(folder)         # get list of files in folder
        except:
            file_list = []

        fnames = [f for f in file_list if os.path.isfile(
            os.path.join(folder, f)) and f.lower().endswith((".png", ".jpg", "jpeg", ".tiff", ".bmp",))]
        window['-FILE LIST-'].update(fnames)
    elif event == '-FILE LIST-':    # A file was chosen from the listbox
        try:
            filename = os.path.join(values['-FOLDER-'], values['-FILE LIST-'][0])
            window['-TOUT-'].update(filename)
            window['-IMAGE-'].update(filename=filename)

        except:
            pass        # something weird happened making the full filename

# --------------------------------- Close & Exit ---------------------------------

window.close()