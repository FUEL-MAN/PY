import webbrowser
from tkinter import *  
  
  
def clicked():
    window = Tk()  #определяем "window" как главное окно 
    window.title("Д/З а может и не Д/З")  
    window.geometry('600x600') #ставим размер окна 
    window.configure(bg='lightblue') #ставим цвет фона
    lbl = Label(window, text="Я сделал д/з, но только 8 и 9,", font=("Arial Bold", 30), bg='lightblue')  
    lbl.grid(column=0, row=0)
    lbl = Label(window, text="я просто в матеше не шарю.", font=("Arial Bold", 30), bg='lightblue')  
    lbl.grid(column=0, row=1)
    btn = Button(window, text="GITHUB", command=clickclack, font=("Arial Bold", 25), height = 2, width = 7, bg='lightblue')  
    btn.grid(column=3, row=0)  
    window.mainloop()
    
def clickclack():
    webbrowser.open('https://github.com/FUEL-MAN/PY/blob/main/98.py')
  
window = Tk()  
window.title("Д/З а может и не Д/З")  
window.geometry('600x600')
window.configure(bg='lightblue') #ставим цвет фона
lbl = Label(window, text="Д/З", font=("Arial Bold", 40), bg='lightblue')  
lbl.grid(column=0, row=0)
btn = Button(window, text="Да это мой код", command=clicked, bg='lightblue')  
btn.grid(column=2, row=0)
window.mainloop()
