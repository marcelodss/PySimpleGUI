import PySimpleGUI as sg

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-1-shot-window-simple-data-entry-return-values-auto-numbered

Lembre-se de como as chaves são essenciais para entender os elementos PySimpleGUI? 

Se você não especificar uma chave e o elemento for um elemento de entrada, uma chave será fornecida para você 
na forma de um inteiro, começando a numeração com zero. Se você não especificar nenhuma chave, 
parecerá que os valores retornados a você estão sendo retornados como uma lista porque as 
chaves são inteiros sequenciais.

Este exemplo não possui chaves especificadas. Os 3 campos de entrada terão as chaves 0, 1, 2. Seu primeiro 
elemento de entrada será acessado como values[0], exatamente como uma lista.
"""

sg.theme('default1')      # Adicione um pouco de cor à janela

# Janela muito básica. Retornar valores usando chaves numeradas

layout = [
    [sg.Text('Por favor, insira seu nome, endereço, telefone ')],
    [sg.Text('Nome', size=(15, 1)), sg.InputText()],
    [sg.Text('Endereço', size=(15, 1)), sg.InputText()],
    [sg.Text('Telefone', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Janela de entrada de dados simples', layout)
event, values = window.read()
window.close()
print(type(values))
print(event, values[0], values[1], values[2])    # Os dados de entrada parecem uma lista simples 