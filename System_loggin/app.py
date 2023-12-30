import customtkinter as ctk 


def usuario_logado():

    nome_inserido = nome.get()
    senha_inserida = senha.get()

    if nome_inserido == 'admin' and senha_inserida == 'admin':
        print('Login realizado com sucesso')
    else:
        print('Usuário e senha invalidos')


window = ctk.CTk()
window.title('App')
window.geometry('400x200')
ctk.set_appearance_mode('dark')

nome = ctk.CTkEntry(window, width=300, height=30, placeholder_text='Digite seu nome: ')
nome.place(relx=0.5, rely=0.3, anchor='center')

senha = ctk.CTkEntry(window, width=300, height=30, placeholder_text='Digite sua senha: ')
senha.place(relx=0.5, rely=0.6, anchor='center')

btn_login = ctk.CTkButton(window, text='Logar', width=150, command=usuario_logado)
btn_login.place(relx=0.5, rely=0.8, anchor='center')

window.mainloop()