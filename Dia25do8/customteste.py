import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# janela principal
root = ctk.CTk()
root.title("Tela de Login")
root.geometry("450x350")

# Login
label_usuario = ctk.CTkLabel(root, text="Usuário")
label_usuario.pack(pady=(20, 5))
entry_usuario = ctk.CTkEntry(root, placeholder_text="Digite seu usuário:")
entry_usuario.pack(pady=5)

label_senha = ctk.CTkLabel(root, text="Senha")
label_senha.pack(pady=(20, 5))
entry_senha = ctk.CTkEntry(root, placeholder_text="Digite sua senha:")
entry_senha.pack(pady=5)

# Botôes
frame_botoes = ctk.CTkFrame(root)
frame_botoes.pack(pady=20)

btn_entrar = ctk.CTkButton(frame_botoes, text="Entrar")
btn_entrar.grid(row=0, column=0, padx=10)

btn_cancelar = ctk.CTkButton(frame_botoes, text="Cancelar", fg_color="red", hover_color="#a83232")
btn_cancelar.grid(row=0, column=1, padx=10)

root.mainloop()
