#Formulário GUI
from tkinter import *

dados = []

def salva():
    t5.delete(END)
    nome = str(t1.get())
    endereco = str(t2.get())
    cpf = str(t3.get())
    idade = int(t4.get())
    dados.append((nome, endereco, cpf, idade))

    t5.insert(END, str(dados))

win = Tk()
win.title('Meu primeiro formulário')
win.geometry("400x300+10+10")

lbl1 = Label(win, text='Nome: ')
lbl2 = Label(win, text='Endereço: ')
lbl3 = Label(win, text='CPF: ')
lbl4 = Label(win, text='Idade: ')
lbl5 = Label(win, text='Resultado: ')

t1 = Entry()
t2 = Entry()
t3 = Entry()
t4 = Entry()
t5 = Entry()

b1 = Button(win, text='Salvar', command=salva)

lbl1.place(x=80, y=50)
lbl2.place(x=80, y=90)
lbl3.place(x=80, y=130)
lbl4.place(x=80, y=170)
lbl5.place(x=80, y=240)

t1.place(x=200, y=50)
t2.place(x=200, y=90)
t3.place(x=200, y=130)
t4.place(x=200, y=170)
b1.place(x=200, y=205)
t5.place(x=200, y=240)


win.mainloop()