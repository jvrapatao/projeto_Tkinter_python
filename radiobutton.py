from tkinter import *

# criando janela
janela = Tk()
janela.title('radiobutton')
janela.geometry('250x250')

# variável selecionada na aplicação e aceita apenas valores inteiros
selecionado_1 = IntVar()
# variável que se for inserida aceitará apenas valores booleanos
selecionado_2 = BooleanVar()
# variável que se for inserida aceitará apenas strings
selecionado_3 = StringVar()


def obter_dados():
    result_1 = selecionado_1.get()
    label_result_1['text'] = result_1


def obter_dados_2():
    result_2 = selecionado_2.get()
    label_result_2['text'] = result_2


def obter_dados_3():
    result_3 = selecionado_3.get()
    label_result_3['text'] = result_3

 # criando botões
radio1 = Radiobutton(janela, command=obter_dados, text='Primeiro',
                     value=1, variable=selecionado_1, font=('Arial 10 bold'))
radio1.grid(row=0, column=0, padx=5, pady=20)

radio2 = Radiobutton(janela, command=obter_dados_2, text='Segundo',
                     value=False, variable=selecionado_2, font=('Arial 10 bold'))
radio2.grid(row=1, column=0, padx=5, pady=20)

radio3 = Radiobutton(janela, command=obter_dados_3, text='Terceiro',
                     value='Três', variable=selecionado_3, font=('Arial 10 bold'))
radio3.grid(row=2, column=0, padx=5, pady=20)

# Label para visualizar o clique no RadioButton
label_result_1 = Label(janela, text='', font=('Arial 10 bold'), anchor='w')
label_result_1.grid(row=0, column=1, padx=50, pady=5, sticky=NSEW)

label_result_2 = Label(janela, text='', font=('Ariel 10 bold'), anchor='w')
label_result_2.grid(row=1, column=1, padx=50, pady=5, sticky=NSEW)

label_result_3 = Label(janela, text='', font=('Ariel 10 bold'), anchor='w')
label_result_3.grid(row=2, column=1, padx=50, pady=5, sticky=NSEW)


janela.mainloop()
