import PySimpleGUI as sg
import hashlib

'''
Fonte: https://www.pysimplegui.org/en/latest/cookbook/#password-protection-for-scripts

Você obtém 2 scripts em um.
Use a metade superior para gerar seu código hash. 
Em seguida, cole-o no código na metade inferior. 
Copie e cole 1/2 inferior em seu código para obter proteção por senha para seu script sem colocar a senha em seu código-fonte.

Crie um login seguro para seus scripts sem precisar incluir sua senha no programa.
Crie um código de hash sha1 para sua senha usando a GUI. Cole na variável no programa final
1. Escolha uma senha
2. Gerar um código de hash para a senha escolhida, executando o programa e digitando 'gui' como a senha
3. Digite senha na GUI
4. Copiar e colar a GUI da janela de código de hash em variável chamada login_password_hash
5. Execute o programa novamente e teste seu login!
'''

# Use esta GUI para obter o código de hash da sua senha
def HashGeneratorGUI():
    layout = [[sg.T('Password Hash Generator', size=(30,1), font='Any 15')],
              [sg.T('Password'), sg.In(key='password')],
              [sg.T('SHA Hash'), sg.In('', size=(40,1), key='hash')],
              ]

    window = sg.Window('SHA Generator', layout, auto_size_text=False, default_element_size=(10,1),
                       text_justification='r', return_keyboard_events=True, grab_anywhere=False)


    while True:
        event, values = window.read()
        if event ==  sg.WIN_CLOSED:
              exit(69)

        password = values['password']
        try:
            password_utf = password.encode('utf-8')
            sha1hash = hashlib.sha1()
            sha1hash.update(password_utf)
            password_hash = sha1hash.hexdigest()
            window['hash'].update(password_hash)
        except:
            pass

# ----------------------------- Cole este código em seu programa / script -----------------------------
# Determine se uma senha corresponde à senha secreta comparando os códigos de hash sha1
def PasswordMatches(password, hash):
    password_utf = password.encode('utf-8')
    sha1hash = hashlib.sha1()
    sha1hash.update(password_utf)
    password_hash = sha1hash.hexdigest()
    if password_hash == hash:
        return True
    else:
        return False

login_password_hash = '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'
password = sg.popup_get_text('Password', password_char='*')
if password == 'gui':                # Remova ao colar em seu programa
    HashGeneratorGUI()               # Remova ao colar em seu programa
    exit(69)                         # Remova ao colar em seu programa
if PasswordMatches(password, login_password_hash):
    print('Login SUCCESSFUL')
else:
    print('Login FAILED!!')