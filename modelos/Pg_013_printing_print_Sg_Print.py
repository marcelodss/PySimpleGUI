import PySimpleGUI as sg

"""
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-printing

A saída de texto é uma operação muito comum na programação. Seu primeiro programa Python pode ter sido
print('Hello World')

Mas no mundo das GUIs, onde as "impressões" se encaixam? Bem, muitos lugares! 
Claro que você ainda pode usar a instrução print normal. Ele enviará para StdOut (saída padrão), que 
normalmente é o shell de onde o programa foi iniciado.

A impressão no console torna-se um problema, no entanto, quando você inicia usando o Windows pythonw ou 
se inicia o programa de alguma outra maneira que não possui um console. Com PySimpleGUI você tem 
muitas opções disponíveis para você, então não tema.

Estas receitas exploram como reter impressões já existentes em seu código. Digamos que seu código foi escrito 
para um console e você deseja migrar para uma GUI. Talvez existam tantas declarações de impressão que você 
não queira modificar cada uma delas individualmente.

Existem pelo menos 3 maneiras de transformar suas instruções print que exploraremos aqui:
1. A janela de depuração - print = sg.Print
2. O elemento de saída - do_not_reroute_stdout=False
3. O elemento multilinha

As várias formas de "imprimir" às quais você será apresentado que suportam os parâmetros sep e end que 
você encontra nas instruções de impressão normais.
"""

# 1- Defina do_not_reroute_stdout=False para enviar os print para sg.Print
# =============================================================================
for i in range(3):
    sg.Print(f'sg.Print - Re-routing the stdout False {i}', do_not_reroute_stdout=False ,wait=True)

for i in range(3):
    print(f'print - Esta é uma impressão normal que foi redirecionada. False {i}')

sg.Print(f'FIM', do_not_reroute_stdout=False ,wait=True)

# 2- Defina print = sg.Print para enviar o print() para sg.Print()
# =============================================================================
print = sg.Print 
for i in range(3):
    print(f'print = sg.Print. {i}', wait=True)

sg.Print(f'FIM', do_not_reroute_stdout=True ,wait=True)
print('fim de novo')