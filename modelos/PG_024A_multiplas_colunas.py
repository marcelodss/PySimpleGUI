import PySimpleGUI as sg      

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-multiple-columns

Uma coluna é necessária quando você tem um elemento alto à esquerda de elementos menores.

Neste exemplo, há uma caixa de listagem à esquerda com 3 linhas de altura. 
À direita dela estão 3 linhas únicas de texto e entrada. Essas 3 linhas estão em um elemento de coluna.

Para facilitar a visualização da Coluna na janela, o plano de fundo da Coluna foi sombreado em azul. 
O código é mais extenso do que o normal devido ao sombreamento azul. 
Cada elemento na coluna precisa ter a cor definida para corresponder ao fundo azul.
"""

sg.theme('BlueMono')      

# Column layout      
col = [[sg.Text('col Row 1', text_color='white', background_color='blue')],      
        [sg.Text('col Row 2', text_color='white', background_color='blue'), sg.Input('col input 1')],      
        [sg.Text('col Row 3', text_color='white', background_color='blue'), sg.Input('col input 2')]]      

layout = [[sg.Listbox(values=('Listbox Item 1', 'Listbox Item 2', 'Listbox Item 3'), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, size=(20,3)), sg.Column(col, background_color='blue')],      
            [sg.Input('Last input')],      
            [sg.OK()]]      

# Display the Window and get values    

event, values = sg.Window('Compact 1-line Window with column', layout).Read()  

sg.popup(event, values, line_width=200)   