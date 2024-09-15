from tkinter import * # Importa tudo, sem precisar prefixar, exemplo: tk.window

'''window = Tk() #
window.title("Welcome nerds")
window.geometry("350x200") # Outra forma de definir o tamanho da janela é com
# window.minsize(), passando os valores dessa forma: (width=500, height=300)
window.config(bg="#292929") # Ou cor1 = "#292929", bg=cor1

lbl = Label(window, text="Olá") # Para adicionar uma fonte diferente à janela, pode-se usar
# font=() dentro da Label, dessa forma: Label(window, text="Texto", font="Arial, 24")
lbl.pack() # Posiciona o label de cima para baixo, por padrão

btn = Button(window, text="Clique aqui")
btn.pack()

window.mainloop()'''

# Criando uma tela
window = Tk()
window.title("Minha janela")
window.minsize(width=500, height=300) #Tamanho mínimo da janela

lbl = Label(window, text="Formulário")
lbl.pack()

lbl = Label(window, text="Nome: ")
lbl.place(x=10, y=15)
txtfld = Entry(window, text="Campo de entrada", bd=5)
txtfld.place(x=60, y=15)

lbl = Label(window, text="Idade:")
lbl.place(x=10, y=50)
txtfld = Entry(window, text="Campo de entrada", bd=5)
txtfld.place(x=60, y=50)

lbl = Label(window, text="Sexo:")
lbl.place(x=10, y=80)
txtfld = Entry(window, text="Campo de entrada", bd=5)
txtfld.place(x=60, y=80)

btn = Button(window, text="Salvar dados:")
btn.place(x=60, y=110)

window.mainloop()