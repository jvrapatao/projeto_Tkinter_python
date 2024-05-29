from tkinter import *


janela = Tk()
janela.title('Entry')
janela.geometry('400x250')


# funcao obter
def obter_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    pais = entry_pais.get()

    label_nome_resp['text'] = nome
    label_idade_resp['text'] = idade
    label_pais_resp['text'] = pais

    entry_nome.delete(0, END)
    entry_idade.delete(0, END)
    entry_pais.delete(0, END)


label_nome = Label(janela, width=10, height=2, text='Nome:',
                   font=('Ariel 10'), anchor='w')
label_nome.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)
entry_nome = Entry(janela, width=10, font=('Arial 10'))
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_idade = Label(janela, width=10, height=2,
                    text='Idade:', font=('Ariel 10'), anchor='w')
label_idade .grid(row=1, column=0, padx=10, pady=5, sticky=NSEW)
entry_idade = Entry(janela, width=10, font=('Arial 10'))
entry_idade.grid(row=1, column=1, padx=10, pady=5)

label_pais = Label(janela, width=10, height=2, text='Pais:',
                   font=('Ariel 10'), anchor='w')
label_pais .grid(row=2, column=0, padx=10, pady=5, sticky=NSEW)
# state='disabled' desativa o entry
entry_pais = Entry(janela, width=10, font=('Arial 10'), state='disabled')
entry_pais.grid(row=2, column=1, padx=10, pady=5)


label_nome_resp = Label(janela, width=15, height=2,
                        text='', font=('Ariel 10'), anchor='w')
label_nome_resp.grid(row=0, column=2, padx=10, pady=5, sticky=NSEW)

label_idade_resp = Label(janela, width=15, height=2,
                         text='', font=('Ariel 10'), anchor='w')
label_idade_resp.grid(row=1, column=2, padx=10, pady=5)

label_pais_resp = Label(janela, width=15, height=2,
                        text='', font=('Ariel 10'), anchor='w')
label_pais_resp.grid(row=2, column=2, padx=10, pady=5, sticky=NSEW)

botao = Button(janela, command=obter_dados, width=8, height=1, text='Dados',
               relief='raised', bg='white')
botao.grid(row=3, column=0, padx=5, pady=20)

janela.mainloop()
