from tkinter import Tk, Label, Button


janela = Tk()
janela.title = ('Botão')
janela.geometry('250x250')


global contador
contador = 0


def executar_botao():
    global contador
    txt1 = 'Numero impar:'
    txt2 = 'Numero par:'

    if contador % 2 == 0:
        resultado = txt2 + str(contador)
        label['text'] = resultado
        label['fg'] = '#24851e'
    else:
        resultado = txt1 + str(contador)
        label['text'] = resultado
        label['fg'] = '#2586c2'
    contador += 1


label = Label(janela, width=20, height=2, text='Texto será apresentado',
              relief='flat', fg='white', bg='#121211')
label.grid(row=0, column=0, padx=5, pady=10)

botao = Button(janela, command=executar_botao, width=8, height=1, text='Clique aqui',
               relief='raised', fg='#fcb503', bg='white')
botao.grid(row=0, column=1, padx=5, pady=10)


janela.mainloop()
