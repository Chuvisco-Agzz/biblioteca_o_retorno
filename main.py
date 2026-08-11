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

# Função para emprestar um livro
def emprestar_livro():
    isbn = int(input("Digite o ISBN do livro: "))
    for livro in livros:
        if livro["isbn"] == isbn:
            if livro["status"] == "disponível":
                livro["status"] = "emprestado"
                salvar_livros()
                print("\nLivro emprestado com sucesso!")
            else:
                print("\nEsse livro já está emprestado.")
            return
    print("\nLivro não encontrado.")

# Função para devolver um livro
def devolver_livro():
    isbn = int(input("Digite o ISBN do livro: "))
    for livro in livros:
        if livro["isbn"] == isbn:
            if livro["status"] == "emprestado":
                livro["status"] = "disponível"
                salvar_livros()
                print("\nLivro devolvido com sucesso!")
            else:
                print("\nEsse livro já está disponível.")
            return
    print("\nLivro não encontrado.")

# Função para listar todos os livros
def listar_livros():
    if len(livros) == 0:
        print("\nNenhum livro cadastrado.")
    else:
        print("\n===== LIVROS CADASTRADOS =====")
        for livro in livros:
            print("---------------------------")
            print("ISBN:", livro["isbn"])
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("Ano:", livro["ano"])
            print("Status:", livro["status"])

# Função para buscar um livro pelo título ou autor
def buscar():
    pesquisa = input("\nDigite o título ou autor do livro: ").lower()
    encontrado = False
    for livro in livros:
        if pesquisa in livro["titulo"].lower() or pesquisa in livro["autor"].lower():
            print("\nLivro encontrado:")
            print("---------------------------")
            print("ISBN:", livro["isbn"])
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("Ano:", livro["ano"])
            print("Status:", livro["status"])
            encontrado = True
    if encontrado == False:
        print("\nNenhum livro encontrado.")

# Função para ordenar os livros
def ordenar():
    print("\nOrdenar por:")
    print("1 - Título")
    print("2 - Autor")
    print("3 - Ano")

    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        livros.sort(key=lambda livro: livro["titulo"])
    elif opcao == 2:
        livros.sort(key=lambda livro: livro["autor"])
    elif opcao == 3:
        livros.sort(key=lambda livro: livro["ano"])
    else:
        print("\nOpção inválida.")
        return

    salvar_livros()
    print("\nLivros ordenados com sucesso!")
    for livro in livros:
        print("---------------------------")
        print("ISBN:", livro["isbn"])
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
        print("Status:", livro["status"])

# Menu principal da biblioteca
def menu_biblioteca():
    while True:
        print("\n──── MENU DA BIBLIOTECA ────")
        print("1 - Cadastrar livro")
        print("2 - Emprestar livro")
        print("3 - Devolver livro")
        print("4 - Listar livros")
        print("5 - Buscar livro")
        print("6 - Ordenar livros")
        print("7 - Sair")

        opcao = int(input("\nDigite uma opção: "))
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            emprestar_livro()
        elif opcao == 3:
            devolver_livro()
        elif opcao == 4:
            listar_livros()
        elif opcao == 5:
            buscar()
        elif opcao == 6:
            ordenar()
        elif opcao == 7:
            print("\nPrograma encerrado.")
            break
        else:
            print("\nOpção inválida.")

carregar_livros()
menu_biblioteca()

