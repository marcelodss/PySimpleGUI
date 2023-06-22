import PySimpleGUI as sg
import os

"""
Fonte: https://www.tutorialspoint.com/pysimplegui/pysimplegui_popup_windows.htm
"""

popup = sg.popup("Hello World popup")
print(popup)
popup = sg.popup_ok_cancel("Hello World popup_ok_cancel ")
print(popup)
popup = sg.popup_cancel("Hello World popup_cancel ")
print(popup)
popup = sg.popup_yes_no("Hello World popup_yes_no ")
print(popup)
popup = sg.popup_error("Hello World popup_error ")
print(popup)
popup = sg.popup_get_text('Enter your name', title="Textbox")
print(popup)
popup = sg.popup_get_file('Select a file',  title="File selector")
print(popup)
popup = sg.popup_get_folder('Get folder', title="Folder selector")
print(popup)

# Pop-up com rolagem
with open('zen.txt', 'a', encoding='utf-8') as f:
    print('teste', file=f)
file=open("zen.txt")
text=file.read()
sg.popup_scrolled(text, title="Scrolled Popup", font=("Arial Bold", 16), size=(50,10))

# medidor de progresso
size = os.path.getsize('zen.txt')
file=open("zen.txt")
i=0
while True:
   text=file.read(1)
   i=i+1
   if text=="":
      file.close()
      break
   print (text,end='')
   sg.one_line_progress_meter(
      'Progress Meter', i, size,
      'Character Counter'
   )

# Pop-up de depuração
f=99
num=int(sg.popup_get_text("enter a number: "))
for x in range(1, num+1):
   f=f*x
   sg.Print (f,x)
print ("factorial of {} = {}".format(x,f))