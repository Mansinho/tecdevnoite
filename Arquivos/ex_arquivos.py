#faça um programa que reeba do usuário um arquivo texto e mostra na tela quantas 'letras são vogais

def main():
    arquivo = input("Digite o nome do arquivo: ")
    try:
        with open(arquivo, 'r') as file:
            conteudo = file.read()
            vogais = 0
            for letra in conteudo:
                if letra.lower() in 'aeiou':
                    vogais += 1
            print(f"O arquivo {arquivo} tem {vogais} vogais")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()