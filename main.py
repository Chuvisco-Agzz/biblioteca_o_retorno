import csv
livros = []

# Função para salvar os livros no arquivo CSV
def salvar_livros():
    with open("livros.csv", "w", newline="", encoding="utf-8") as arquivo:
        campos = ["isbn", "titulo", "autor", "ano", "status"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        for livro in livros:
            escritor.writerow(livro)

# Função para carregar os livros do arquivo CSV
def carregar_livros():
    with open("livros.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for livro in leitor:
            livro["isbn"] = int(livro["isbn"])
            livros.append(livro)

# Funcao para adicionar um livro à lista
def cadastrar():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano de publicação: ")
    ISBN = int(input("Digite o ISBN do livro: "))
    livro = {
        "isbn": ISBN,
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "status": "disponível"
    }
    livros.append(livro)
    salvar_livros()
    print("\nLivro cadastrado com sucesso!")