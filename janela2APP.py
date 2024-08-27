#usa a janela customtkinter

# idade_fat =int(input('\ninforme seu numero: '))
# print (f'Dobro da idade : {idade_fat * 2}')





import customtkinter as ctk

def dobro_idade():
    if entry_idade.get () != "":   
        idade = int (entry_idade.get ())
        end_calc.configure(text=f'Dobro da idade: {idade*2}')






ctk.set_appearance_mode('Light')

# JA TA criando o freme
root = ctk.CTk()
root.geometry('500x350+500+100')
root.title('Calcula o dobro da idade')
root.resizable(False,False)

# label tituloJANELA  
lbl_titulo = ctk.CTkLabel(root,
    text=('Calcule o dobro da idade'),
    font=('monospace', 20),
    text_color='blue'
    )
lbl_titulo.pack(padx=10, pady=10)

# Caixa de entrada [Entry box]
entry_idade = ctk.CTkEntry(root,
	placeholder_text=('Digite sua idade'),
	width=280, height=40,
	font=("Monospace", 25, 'bold'),
    corner_radius=30,
	placeholder_text_color=('black'),
	text_color='#000000')
entry_idade.pack(padx=10, pady=35)

# botao para enviar a conta
btn_enviar =ctk.CTkButton (root,
    text = 'Enviar',
    width= 200, height= 30,
    font= ("monospace", 25, 'bold'),
    text_color= '#ffffff',
    fg_color= '#4169E1',
    corner_radius=30,
    hover_color = '#0000CD',
    command= dobro_idade
)
btn_enviar.pack(padx=10, pady=30)


# fazer um label para mostrar o resultado da conta
end_calc = ctk.CTkLabel(root,
    text='',
    font=('monospace', 20),
    text_color='blue',
    )
end_calc.pack(padx=10, pady=30)


root.mainloop()



