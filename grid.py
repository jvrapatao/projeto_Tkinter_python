from tkinter import *

janela = Tk()
janela.title('Grid')
janela.geometry('250x250')

label_nome = Label(janela, width=10, height=2, text='Nome:',
                   font=('Ariel 10 bold'), fg='#fc3503', bg='black')
label_nome.grid(row=0, column=0)
nome = Label(janela, width=10, height=2, text='João Vitor',
             font=('Ariel 10 bold'), fg='#fc3503', bg='black')
nome.grid(row=0, column=1, padx=5, pady=10)


label_idade = Label(janela, width=10, height=2, text='Idade: ',
                    font=('Ariel 10 bold'), fg='#429639', bg='black')
label_idade.grid(row=1, column=0)
idade = Label(janela, width=10, height=2, text='Xy',
              font=('Ariel 10 bold'), fg='#429639', bg='black')
idade.grid(row=1, column=1, padx=5, pady=10)


label_pais = Label(janela, width=10, height=2, text='Pais: ',
                   font=('Ariel 10 bold'), fg='#6168e8', bg='black')
label_pais.grid(row=2, column=0)
pais = Label(janela, width=10, height=2, text='Brasil',
             font=('Ariel 10 bold'), fg='#6168e8', bg='black')
pais.grid(row=2, column=1, padx=5, pady=10)

janela.mainloop()
