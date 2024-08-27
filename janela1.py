# Primeira janela com a biblioteca customtkinter

# nome = input('\nInforme seu nome: ')
# print(f'Seja bem-vindo Sr(a) {nome}')

import customtkinter as ctk

def boasvindas():
	if entry_nome.get() != '':
		lbl_saida.configure(text=f'Bem-vindo {entry_nome.get()}')
	
janela = ctk.CTk()
janela.geometry('500x300+500+100')

# Label título
lbl_titulo = ctk.CTkLabel(janela,
	text='Tela de boas vindas',
	font=("Helvetica", 35),
	text_color='#778899')
lbl_titulo.pack(padx=10, pady=10)

# Caixa de entrada [Entry box]
entry_nome = ctk.CTkEntry(janela,
	placeholder_text='Informe seu nome',
	width=280, height=40,
	font=("Monospace", 25),
	corner_radius =30,
	placeholder_text_color='#ff0000',
	text_color='#0000ff')
entry_nome.pack(padx=10, pady=20)


# Botão enviar
btn_enviar = ctk.CTkButton(janela,
	command=boasvindas,
	width=200, height=40,
	font=('Monospace', 20, 'bold'),
	corner_radius=30,
	text='Enviar',
	text_color='#000000',
	fg_color='#1E90FF',
	hover_color='#4169E1'
)
btn_enviar.pack(padx=10, pady=40)



# Label saída
lbl_saida = ctk.CTkLabel(janela,
	text='',
	font=('Helvetica', 25, 'bold'),
	text_color='#000000'
	)
lbl_saida.pack(padx=10, pady=10)


janela.mainloop()
