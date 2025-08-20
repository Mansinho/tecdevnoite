import tkinter as tk

#1. Você está criando um programa em Python e precisa abrir a janela principal onde os botões e rótulos serão exibidos.
#👉 Escreva o código necessário para criar a janela principal usando Tkinter.

pagina = tk.Tk()
pagina.title = "Primeira página"
pagina.geometry("300x300")

label = tk.Label(pagina, text="Você está aqui", font=("Arial", 12))
pagina.pack(pady=10)

btn = tk.Button(pagina, text="Fechar", command=pagina.destroy)
btn.pack(pady=5)

pagina.loop()