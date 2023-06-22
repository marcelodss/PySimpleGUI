import PySimpleGUI as sg    

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#tabs
As guias trazem não apenas um nível extra de sofisticação ao layout da janela, mas também 
espaço extra para adicionar mais elementos. As guias são um dos 3 elementos do contêiner, 
elementos que contêm ou contêm outros elementos. 
Os outros dois são os elementos Column e Frame.
"""

tab1_layout =  [[sg.T('This is inside tab 1')]]    

tab2_layout = [[sg.T('This is inside tab 2')],    
               [sg.In(key='in')]]    

layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout, tooltip='tip'), sg.Tab('Tab 2', tab2_layout)]], tooltip='TIP2')],    
          [sg.Button('Read')]]    

window = sg.Window('My window with tabs', layout, default_element_size=(12,1))    

while True:    
    event, values = window.read()    
    print(event,values)    
    if event == sg.WIN_CLOSED:           # always,  always give a way out!    
        break  