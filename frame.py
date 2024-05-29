from tkinter import *


janela = Tk()
janela.title('Frame')
janela.geometry('400x400')


frame_1 = Frame(janela, width=400, height=20, bg='white')
frame_1.grid(row=0, column=0, columnspan=3, pady=2, padx=0)

frame_2 = Frame(janela, width=100, height=260, bg='#d6d6d6')
frame_2.grid(row=1, column=0, pady=2, padx=2)

frame_3 = Frame(janela, width=200, height=260, bg='white')
frame_3.grid(row=1, column=1, pady=2, padx=2)

frame_4 = Frame(janela, width=200, height=260, bg='#d6d6d6')
frame_4.grid(row=1, column=2, pady=2, padx=2)





janela.mainloop()
