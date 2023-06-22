from tkinter import *
import tkinter as tk
from tkinter import ttk
root = Tk()
root.geometry("160x180")
frm = ttk.Frame(root, padding=10)
frm.grid()

#----------------------------------
def btnExibirMensagem(msg):
    #Saída do texto
    mensagem.set(msg)
    #Limpar caixa de textos
    txtMensagem.delete(0,"end")
    #Atribuir valor a caixa de textos
    txtMensagem.insert(0,'')
    txtMensagem.focus_force()

#----------------------------------------  


#Criação da caixa de textos
txtMensagem=tk.Entry(frm, justify = CENTER)
ttk.Label(frm, text="Insira a Mensagem").grid(column=0, row=0, pady=5, padx=5, sticky='nswe', columnspan=2)
txtMensagem.grid(column=0, row=1, pady=3, padx=10, sticky='nswe', columnspan=6)
txtMensagem.focus_force()

#Criação de combo box
#combo = ttk.Combobox(values=['Valor1','Valor2','Valor3'])
# combo.grid(column=0, row=3, pady=5, padx=5, sticky='nswe', columnspan=4)

#Criação de botões
ttk.Button(frm, text="Exibir Mensagem", command=lambda:btnExibirMensagem(txtMensagem.get())).grid(column=0, row=2, pady=5, padx=5, sticky='nswe', columnspan=4)

#Exibição do texto
mensagem=StringVar()
lblMensagem=ttk.Label(frm, textvariable=mensagem).grid(column=0, row=3, pady=5, padx=5, sticky='nswe', columnspan=6)

#Para não encerrar a aplicação
root.mainloop()



