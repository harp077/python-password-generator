from tkinter import *
from tkinter import ttk
from random import *
from tkinter.messagebox import showinfo
#import sv_ttk

alfavitListChars= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alfavitListTiny = alfavitListChars + ['0','1','2','3','4','5','6','7','8','9']
alfavitListBig  = alfavitListTiny  + ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','[',']','{','}','|',':',';','"',',','<','>','.','?','/']

def get_passw():
    dlinaPassw=0
    result=''
    shuffle(alfavitListTiny)
    shuffle(alfavitListBig)
    shuffle(alfavitListChars)
    simvol = ''
    while dlinaPassw < int(comboboxDlinaPassw.get()):
        if use_big.get() == 1:
            simvol = choice(alfavitListBig)
        if use_big.get() == 0:
            simvol = choice(alfavitListTiny)
        if dlinaPassw == 0:
            simvol = choice(alfavitListChars)
        dlinaPassw += 1
        result = result + simvol
    if uppercase.get() == 1:
        result = result.upper()
    entry.delete(0, END)
    entry.insert(0, result)
    return

root = Tk()

def copy_clip():
    root.clipboard_clear()
    root.clipboard_append(entry.get())
    
def open_info(): 
    showinfo(title="Clipboard", message=get_clipboard_text())
    
def about_info(): 
    showinfo(title="About", message=" Made by harp07, \n Saratov city, Russia \n mail=harp07@mail.ru, \n home: \n https://github.com/harp077")    
    
def get_clipboard_text():
    try:
        txt = root.clipboard_get()
        return txt
    except BaseException as e:
        print(e)
        return ""
    
def clear(): 
    entry.delete(0, END)
    root.clipboard_clear()
    return

root.title(" Python Password Generator ")
root.geometry("+222+222")
#root.geometry("555x200+222+222")

ttk.Style().theme_use("alt")
#ttk.Style().configure(".",  foreground="#0000ff", background="#ffff00", padding=5)
for theme in ttk.Style().theme_names():
    print(theme)

entry=ttk.Entry(root)
#entry.configure(background="#ffff00")
entry.grid(row=0, column=0, columnspan=4, padx=11, pady=22, sticky=EW)

use_big = IntVar()
checkbutton_use_big = ttk.Checkbutton(root, text="use special chars ", variable=use_big)
checkbutton_use_big.grid(row=1, column=0, padx=11, pady=11)

uppercase = IntVar()
checkbutton_uppercase = ttk.Checkbutton(root, text="uppercase ", variable=uppercase)
checkbutton_uppercase.grid(row=1, column=1, padx=11, pady=11)

label = ttk.Label(root, text="Password length = ")
label.grid(row=1, column=2, padx=11, pady=11)

dlinaPasswMax = [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
dlinaPasswMax_var = StringVar(value=dlinaPasswMax[0])   
comboboxDlinaPassw = ttk.Combobox(root, textvariable=dlinaPasswMax_var, values=dlinaPasswMax, width=5)
comboboxDlinaPassw.grid(row=1, column=3, padx=11, pady=11)

btnGet = ttk.Button(root, text=" Generate Password ", command=get_passw) # создаем кнопку из пакета ttk
btnGet.grid(row=2, column=0, padx=11, pady=11)

btnCopyToClip = ttk.Button(root, text=" Copy to ClipBoard ", command=copy_clip) # создаем кнопку из пакета ttk
btnCopyToClip.grid(row=2, column=1, padx=11, pady=11)

info_button = ttk.Button(root, text=" Show Clipboard ", command=open_info)
info_button.grid(row=2, column=2, padx=11, pady=11)

clear_button = ttk.Button(root, text=" Clear all ", command=clear)
clear_button.grid(row=2, column=3, padx=11, pady=11)

#button = ttk.Button(root, text=" Toggle theme ", command=sv_ttk.toggle_theme)
#button.grid(row=3, column=1, padx=11, pady=11)

#sv_ttk.set_theme("dark")
#sv_ttk.use_dark_theme()
#sv_ttk.use_light_theme()

about_button = ttk.Button(root, text=" About ", command=about_info)
about_button.grid(row=3, column=2, padx=11, pady=11)

root.mainloop()


