from tkinter import *
import tkinter

cor1 = 'black'
cor2 = 'white'
cor3 = 'green'
cor4 = 'red'
cor5 = 'gray'
cor6 = 'blue'

# criandoo janela
janela = Tk()
janela.title = 'cronômetro'
janela.geometry('300x180')
janela.configure(bg=cor1)
janela.resizable(width=False, height=False)

# variáveis globais
global tempo
global rodar
global contador
global limitador

limitador = 59

tempo = '00:00:00'
rodar = False
contador = -5


def iniciar():
    global tempo
    global contador
    global limitador

    if rodar:
        if contador <= -1:
            inicio = 'Começando em ' + str(contador)
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Arial 10'

        else:
            label_tempo['font'] = 'Times 50 bold'
            temporaria = str(tempo)
            h, m, s = map(int, temporaria.split(':'))
            h = int(h)
            m = int(m)
            s = int(contador)

            if (s >= limitador):
                contador = 0
                m += 1

            s = str(0) + str(s)
            m = str(0) + str(m)
            h = str(0) + str(h)

            # atualzando os valores atuais
            temporaria = str(h[-2:])+':' + str(m[-2:]) + ':' + str(s[-2:])
            label_tempo['text'] = temporaria
            tempo = temporaria

        label_tempo.after(1000, iniciar)
        contador += 1


# funcao para dar inicio
def start():
    global rodar
    rodar = True
    iniciar()


# funcao para dar pausar
def pausar():
    global rodar
    rodar = False


# funcao para dar reiniciar
def reiniciar():
    global contador
    global tempo
    # reiniciando o contador
    contador = 0
    # reiniciando o tempo
    tempo = '00:00:00'
    label_tempo['text'] = tempo


# criando label
label_app = Label(janela, text='Cronômetro',
                  font=('Arial 10'), bg=cor1, fg=cor2)
label_app.place(x=20, y=5)

# criando label tempo
label_tempo = Label(janela, text=tempo, font=(
    'Times 50 bold'), bg=cor1, fg=cor4)
label_tempo.place(x=20, y=30)

# criando botao iniciar
botao_iniciar = Button(janela, command=start, text='Iniciar', width=10,
                       height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_iniciar.place(x=20, y=130)

botao_pausar = Button(janela, command=pausar, text='Pausar', width=10,
                      height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_pausar.place(x=105, y=130)

botao_riniciar = Button(janela, command=reiniciar, text='Riniciar', width=10,
                        height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_riniciar.place(x=190, y=130)


janela.mainloop()
