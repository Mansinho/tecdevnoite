import customtkinter as ctk


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


janela = ctk.CTk()
janela.title("Exemplo com CustomTkinter")
janela.geometry("400x250")


def testar_entrada():
    texto = entrada.get()
    resultado.configure(text=f"Você digitou: {texto}")

titulo = ctk.CTkLabel(janela, text="Digite algo:", font=ctk.CTkFont(size=20, weight="bold"))
titulo.pack(pady=10)

entrada = ctk.CTkEntry(janela, placeholder_text="Escreva aqui...")
entrada.pack(pady=10)

botao = ctk.CTkButton(janela, text="Testar", command=testar_entrada)
botao.pack(pady=10)

resultado = ctk.CTkLabel(janela, text="")
resultado.pack(pady=10)



janela.mainloop()
