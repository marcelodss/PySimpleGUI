import PySimpleGUI as sg

"""
- Themes - Window "Beautification": https://www.pysimplegui.org/en/latest/cookbook/#themes-window-beautification
"""

'''
Para ver a visualização acima para sua versão do PySimpleGUI, faça esta chamada para gerar uma visualização de todos os temas disponíveis:
'''
# sg.theme_previewer(columns=10, scrollable = True) # ou
sg.preview_all_look_and_feel_themes(columns=10, scrollable = True)


"""
Você também pode obter a lista de nomes de temas chamando theme_list
"""
# theme_name_list = sg.theme_list()
# print(theme_name_list)