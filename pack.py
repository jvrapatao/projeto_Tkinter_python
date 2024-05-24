from tkinter import *
# pack() centraliza os labels e para move-los é preciso passar os parâmetro 'size='
janela = Tk()
janela.title('Pack')
janela.geometry('250x250')

label_nome = Label(janela, width=10, height=2, text='Nome:',
                   font=('Ariel 10 bold'), fg='#fc3503', bg='black')
label_nome.pack()
nome = Label(janela, width=10, height=2, text='João Vitor',
             font=('Ariel 10 bold'), fg='#fc3503', bg='black')
nome.pack()


label_idade = Label(janela, width=10, height=2, text='Idade: ',
                    font=('Ariel 10 bold'), fg='#429639', bg='black')
label_idade.pack()
idade = Label(janela, width=10, height=2, text='Xy',
              font=('Ariel 10 bold'), fg='#429639', bg='black')
idade.pack()


label_pais = Label(janela, width=10, height=2, text='Pais: ',
                   font=('Ariel 10 bold'), fg='#6168e8', bg='black')
label_pais.pack()
pais = Label(janela, width=10, height=2, text='Brasil',
             font=('Ariel 10 bold'), fg='#6168e8', bg='black')
pais.pack()


janela.mainloop()
