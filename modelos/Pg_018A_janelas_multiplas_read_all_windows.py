import PySimpleGUI as sg

"""
    Fonte: https://www.pysimplegui.org/en/latest/cookbook/#recipe-multiple-windows-read_all_windows

    Demo - 2 janelas simultâneas usando read_all_window
    Ambas as janelas são imediatamente visíveis.Cada janela atualiza a outra.
    Copyright 2020 PySimpleGUI.org

    Esta receita mostra 2 janelas. Ambos são ativos e podem ser interagidos. 
    Quando você insere algo na janela 1, ele é atualizado na janela 2. Observe que as teclas 
    têm o mesmo nome em ambas as janelas. Isso torna muito fácil escrever um código genérico que 
    atualizará os campos em qualquer janela, a única diferença será qual janela será atualizada.

    Você descobrirá que terá menos chances de problemas como "reutilização de layouts" se colocar 
    o layout e a criação de janelas em uma função. Isso garantirá uma janela "fresca" toda vez que 
    você chamar a função. Se você fechar a janela 2 e clicar no botão "Reabrir" na janela 1, basta 
    chamar a função make_win2 novamente e mover a nova janela para o local abaixo da primeira janela.

    O programa permanece ativo até que ambas as janelas sejam fechadas.
"""

def make_win1():
    layout = [[sg.Text('Window 1')],
              [sg.Text('Enter something to output to Window 2')],
              [sg.Input(key='-IN-', enable_events=True)],
              [sg.Text(size=(25,1), key='-OUTPUT-')],
              [sg.Button('Reopen')],
              [sg.Button('Exit')]]
    return sg.Window('Window Title', layout, finalize=True)


def make_win2():
    layout = [[sg.Text('Window 2')],
              [sg.Text('Enter something to output to Window 1')],
              [sg.Input(key='-IN-', enable_events=True)],
              [sg.Text(size=(25,1), key='-OUTPUT-')],
              [sg.Button('Exit')]]
    return sg.Window('Window Title', layout, finalize=True)


def main():
    window1, window2 = make_win1(), make_win2()

    window2.move(window1.current_location()[0], window1.current_location()[1]+220)

    while True:             # Event Loop
        window, event, values = sg.read_all_windows()

        if window == sg.WIN_CLOSED:     # if all windows were closed
            break
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            if window == window2:       # if closing win 2, mark as closed
                window2 = None
            elif window == window1:     # if closing win 1, mark as closed
                window1 = None
        elif event == 'Reopen':
            if not window2:
                window2 = make_win2()
                window2.move(window1.current_location()[0], window1.current_location()[1] + 220)
        elif event == '-IN-':
            output_window = window2 if window == window1 else window1
            if output_window:           # if a valid window, then output to it
                output_window['-OUTPUT-'].update(values['-IN-'])
            else:
                window['-OUTPUT-'].update('Other window is closed')


if __name__ == '__main__':
    main()