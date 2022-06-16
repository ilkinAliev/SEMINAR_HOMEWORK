import tkinter as tk
from yt_down import yt_down
from tkinter.ttk import Combobox

window = tk.Tk()
window.title("Скачай весь Youtube!!!")
window.geometry('500x300') #фиксируем размер окна
window.resizable(width=False, height=False) #запрет на изменение размеров окна
# window.minsize(300, 300) #предельный минимальный размер окна
# window.maxsize(600, 600)
def clicked():
    video_adres = txt.get()
    save_path = txt2.get()
    yt_down(video_adres, save_path)


lb1 = tk.Label(window, text='введите адрес видео ', font=('Arial', 14 ))
lb1.grid(row=0, column=0)

lb2 = tk.Label(window, text='куда сохраняем? ', font=('Arial', 14 ))
lb2.grid(row=2, column=0)

btn = tk.Button(window, text='скачать', font=('Arial', 14), bg='green', command=clicked)
btn.grid(row=6, column=0)

txt = tk.Entry(window, width=100) # окно ввода
txt.grid(row = 0, column=1)
txt.focus() # фокусировка курсора на окне ввода

txt2 = tk.Entry(window, width=100) # окно ввода
txt2.grid(row = 2, column=1)
# combo = Combobox(window)
# combo['values'] = ('C:\Youtube', "Текст")  
# combo.current(0)  # установите вариант по умолчанию  
# combo.grid(row=2, column=1)  
window.mainloop()