#Formulário GUI - MEAS
from tkinter import *

arquivo = open("dados.txt", "a+", encoding="UTF-8")
#listaDados = []

def salva():
    nome = str(t1.get())
    endereco = str(t2.get())
    cpf = str(t3.get())
    idade = int(t4.get())
    
    if nome:
        listbox.insert(END, nome + "," + cpf)
        
        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)
        t4.delete(0, END)

        linha = f"{nome}, {endereco}, {cpf}, {idade}\n"
        #listaDados.append((nome, endereco, cpf, idade))
        
        arquivo.write(linha)
        arquivo.flush()

def insere():
    arquivo = open("dados.txt", "r", encoding="UTF-8")
    for linha in arquivo:
        dados = linha.split(",")
        listbox.insert(END, dados[0] + "," + dados[2]) 
        
def deleta():
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)

def seleciona(event):
    arquivo = open("dados.txt", "r", encoding="UTF-8")   

    indice = listbox.curselection() 

    if indice:
        linhaSelecionada = listbox.get(indice)
        ls = linhaSelecionada.split(",")
        for d in arquivo:
            da = d.split(",")
            if (da[0] == ls[0]):
                deleta()
                t1.insert(END, da[0])
                t2.insert(END, da[1])
                t3.insert(END, da[2])
                t4.insert(END, da[3])

win = Tk()
win.title('Meu primeiro formulário')
win.geometry("400x300+10+10")

lbl1 = Label(win, text='Nome: ')
lbl2 = Label(win, text='Endereço: ')
lbl3 = Label(win, text='CPF: ')
lbl4 = Label(win, text='Idade: ')
lbl5 = Label(win, text='Agenda: ')

listbox = Listbox(win, width=20, height=5)
insere()

t1 = Entry()
t2 = Entry()
t3 = Entry()
t4 = Entry()

b1 = Button(win, text='Salvar', command=salva)
b2 = Button(win, text='Deletar', command=deleta)

lbl1.place(x=80, y=50)
lbl2.place(x=80, y=90)
lbl3.place(x=80, y=130)
lbl4.place(x=80, y=170)
lbl5.place(x=80, y=240)

listbox.place(x=200, y=240)
listbox.bind('<<ListboxSelect>>', seleciona)

t1.place(x=200, y=50)
t2.place(x=200, y=90)
t3.place(x=200, y=130)
t4.place(x=200, y=170)
b1.place(x=200, y=205)
b2.place(x=270, y=205)

b2.bind('<<Button-1>>', deleta)

win.mainloop()