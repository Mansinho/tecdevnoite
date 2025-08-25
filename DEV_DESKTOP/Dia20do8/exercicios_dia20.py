# EXERCICIO 1
# import tkinter as tk
# from tkinter import messagebox

# def verificar_idade():
#     try:
#         idade = int(entry_idade.get())
#         if idade > 0 and idade < 18:
#             messagebox.showinfo("Resultado", "Você é menor de idade.")

#         elif idade >= 18 and idade <= 100:
#             messagebox.showinfo("Resultado", "Você é maior de idade.")

#         else:
#             messagebox.showinfo("Resultado", "Digite uma opção válida.") 

#     except ValueError:
#         messagebox.showerror("Erro", "Por favor, digite um número inteiro.")


# root = tk.Tk()
# root.title("Verificação de Idade")
# root.geometry("400x400")

# tk.Label(root, text="Digite sua idade:").pack(pady=5)
# entry_idade = tk.Entry(root)
# entry_idade.pack(pady=5)

# tk.Button(root, text="Verificar", command=verificar_idade).pack(pady=10)

# root.mainloop()



# EXERCICIO 2
# import tkinter as tk
# from tkinter import messagebox

# def resultado_escolar():
#     try:
#         nota = float(entry_nota.get())
#         if nota >= 7 and nota <= 10:
#             messagebox.showinfo("Resultado", "O aluno foi aprovado!")

#         elif nota >= 5 and nota < 7:
#             messagebox.showinfo("Resultado", "O aluno está de recuperação!")

#         elif nota < 5 and nota >= 0:
#             messagebox.showinfo("Resultado", "O aluno foi reprovado!")

#         else:
#             messagebox.showinfo("Resultado", "Nota inválida.")

#     except ValueError:
#         messagebox.showerror("Erro", "Por favor, digite apenas números.")

# root = tk.Tk()
# root.title("Resultado escolar")
# root.geometry("300x300")

# tk.Label(root, text="Digite a nota do aluno: ").pack(pady=15)
# entry_nota = tk.Entry(root)
# entry_nota.pack(pady=10)

# tk.Button(root, text="Confirmar", command=resultado_escolar).pack(pady=10)

# root.mainloop()



# EXERCICIO 3
# import tkinter as tk
# from tkinter import messagebox 

# def numeros_inteiros():
#     try:
#         numero =int(entry_numero.get())
#         if numero < 0:
#             messagebox.showinfo("Resultado", "O número é negativo.")
        
#         elif numero > 0:
#             messagebox.showinfo("Resultado", "O número é positivo.")

#         else:
#             messagebox.showinfo("Resultado", "Digite um número inteiro!")
        
#     except ValueError:
#         messagebox.showerror("Erro", "Por favor, digite apenas números inteiros!")

# root =  tk.Tk()
# root.title("Verificar números inteiros.")
# root.geometry("300x300")

# tk.Label(root, text="Digite um número inteiro: ").pack(pady=15)
# entry_numero = tk.Entry(root)
# entry_numero.pack(pady=10)

# tk.Button(root, text="Confirmar", command=numeros_inteiros).pack(pady=10)

# root.mainloop()



# EXERCICIO 3
# import tkinter as tk
# from tkinter import messagebox
# def verificar_numero():
#     try:
#         numero = float(entry_numero.get())
#         if numero > 0:
#             messagebox.showinfo(title="Resultado", message="Número positivo")

#         elif numero < 0:
#             messagebox.showinfo(title="Resultado", message="Número negativo")

#         else:
#             messagebox.showinfo(title="Resultado", message="Número igual a zero")
#     except ValueError:
#         messagebox.showerror(title="Erro", message="Digite um valor numérico válido.")

# app = tk.Tk()
# app.title("Identificador de Números")
# app.geometry("600x400")

# tk.Label(app, text="Digite um número:").pack(pady=5)
# entry_numero = tk.Entry(app)
# entry_numero.pack(pady=5)

# tk.Button(app, text="Verificar", command=verificar_numero).pack(pady=20)

# app.mainloop()


# EXERCICIO 4
# import tkinter as tk
# from tkinter import messagebox
# def verificar_senha():
#     senha = entry_senha.get()
#     if senha == '1234':
#         messagebox.showinfo(title="Acesso", message="Acesso permitido")

#     else:
#         messagebox.showerror(title="Acesso", message="Acesso negado")

# app = tk.Tk()
# app.title("Sistema de Senha")
# app.geometry("600x400")

# tk.Label(app, text="Digite a senha:").pack(pady=5)
# entry_senha = tk.Entry(app, show='*')
# entry_senha.pack(pady=5)

# tk.Button(app, text="Verificar Senha", command=verificar_senha).pack(pady=20)

# app.mainloop()


# EXERCICIO 5 
# import tkinter as tk
# from tkinter import messagebox
# def mostrar_preco():
#     opcao = entry_opcao.get()
#     if opcao == '1':
#         messagebox.showinfo(title="Cardápio", message="Pizza – R$ 30,00")

#     elif opcao == '2':
#         messagebox.showinfo(title="Cardápio", message="Hambúrguer – R$ 20,00")

#     elif opcao == '3':
#         messagebox.showinfo(title="Cardápio", message="Refrigerante – R$ 5,00")

#     else:
#         messagebox.showerror(title="Erro", message="Opção inválida")

# app = tk.Tk()
# app.title("Cardápio Interativo")
# app.geometry("600x400")

# tk.Label(app, text="Escolha uma opção do cardápio:").pack(pady=5)
# tk.Label(app, text="1. Pizza – R$ 30,00").pack()
# tk.Label(app, text="2. Hambúrguer – R$ 20,00").pack()
# tk.Label(app, text="3. Refrigerante – R$ 5,00").pack(pady=5)
# entry_opcao = tk.Entry(app)

# entry_opcao.pack(pady=5)
# tk.Button(app, text="Ver Preço", command=mostrar_preco).pack(pady=20)

# app.mainloop()