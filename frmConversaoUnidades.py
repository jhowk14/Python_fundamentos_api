from tkinter import *
import tkinter as tk
from tkinter import ttk
root = Tk()
root.geometry("1366x768")
frm = ttk.Frame(root, padding=10)
frm.grid()

#----------------------------------
def btnExibirMedida(unidade):
    #Saída do texto
    medidaCm = float(txtMedida.get())
    #Verificação da unidade e cálculo de conversão
    if unidade=='Polegada':
        medidaConvertida = medidaCm/2.54
    elif unidade=='Pé':
        medidaConvertida = medidaCm/30.48
    elif unidade=='Pé':
        medidaConvertida = medidaCm/91.44
    
    #Exibição do resultado
    medida.set(f'{medidaCm}cm em {unidade}s é {medidaConvertida:.4f}')
    #Limpar caixa de textos
    txtMedida.delete(0,"end")
    #Atribuir valor a caixa de textos
    txtMedida.insert(0,'')
    txtMedida.focus_force()

#----------------------------------------  


#Criação da caixa de textos
txtMedida=tk.Entry(frm, justify = CENTER)
ttk.Label(frm, text="Insira a Mensagem").grid(column=0, row=0, pady=5, padx=5, sticky='nswe', columnspan=2)
txtMedida.grid(column=0, row=1, pady=3, padx=10, sticky='nswe', columnspan=6)
txtMedida.focus_force()

#Criação de combo box
cmbUnidade = ttk.Combobox(frm, values=['Polegada','Pé','Jarda'])
cmbUnidade.grid(column=0, row=2, pady=5, padx=5, sticky='nswe', columnspan=4)

#Criação de botões
ttk.Button(frm, text="Converter Medida", command=lambda:btnExibirMedida(cmbUnidade.get())).grid(column=0, row=3, pady=5, padx=5, sticky='nswe', columnspan=4)

#Exibição do texto
medida=StringVar()
lblMedida=ttk.Label(frm, textvariable=medida).grid(column=0, row=4, pady=5, padx=5, sticky='nswe', columnspan=6)

#Para não encerrar a aplicação
root.mainloop()



