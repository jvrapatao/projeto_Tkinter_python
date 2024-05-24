from tkinter import *

janela = Tk()
janela.title('Place')
janela.geometry('250x250')

label_nome = Label(janela, width=10, height=2, text='Nome:',
                   font=('Ariel 10 bold'), fg='#fc3503', bg='black')
label_nome.place(x=10, y=10)
nome = Label(janela, width=10, height=2, text='João Vitor',
             font=('Ariel 10 bold'), fg='#fc3503', bg='black')
nome.place(x=100, y=10)

label_idade = Label(janela, width=10, height=2, text='Idade: ',
                    font=('Ariel 10 bold'), fg='#429639', bg='black')
label_idade.place(x=10, y=60)
idade = Label(janela, width=10, height=2, text='XY',
              font=('Ariel 10 bold'), fg='#429639', bg='black')
idade.place(x=100, y=60)

label_pais = Label(janela, width=10, height=2, text='Pais: ',
                   font=('Ariel 10 bold'), fg='#6168e8', bg='black')
label_pais.place(x=10, y=110)
pais = Label(janela, width=10, height=2, text='Brasil',
             font=('Ariel 10 bold'), fg='#6168e8', bg='black')
pais.place(x=100, y=110)


janela.mainloop()
