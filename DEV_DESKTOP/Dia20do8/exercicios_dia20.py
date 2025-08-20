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

import tkinter as tk
from tkinter import messagebox

def resultado_escolar():
    try:
        nota = int(input("Digite a nota do aluno: "))
        if nota >= 7 and nota <= 10:
            messagebox.showinfo("Resultado", "O aluno foi aprovado!")

        elif nota >= 5 and nota < 7:
            messagebox.showinfo("Resultado", "O aluno está de recuperação!")

        elif nota < 5 and nota >= 0:
            messagebox.showinfo("Resultado", "O aluno foi reprovado!")

        else:
            messagebox.showinfo("Resultado", "Nota inválida.")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite apenas números.")

    root = tk.Tk()
    root.title("Resultado escolar")
    root.geometry("300x300")

    tk.Label(root, text=nota).pack(pady=5)

