class sistemaDeEmprestimos:
    def __init__(self):
        self.Registros = {}

    def RegistrarEmprestimo(self):
        nome = input("Digite o nome da pessoa que está pegando o livro emprestado: ").lower()
        livroEmprestado = input("Digite o título do livro a ser emprestado: ").lower()

        totalLivros = sum(livros.get(livroEmprestado, 0) for livros in self.Registros.values())

        if (totalLivros >= 5):
            return f"Estoque do livro {livroEmprestado.title()} esgotado"

        if (nome not in self.Registros):
            self.Registros[nome] = {}
        
        if (livroEmprestado not in self.Registros[nome]):
            self.Registros[nome][livroEmprestado] = 0   

        self.Registros[nome][livroEmprestado] += 1
        
        return f"*Livro '{livroEmprestado.title()}' emprestado para {nome.title()}.*"

    def FazerDevolução(self):
        nome = input("Digite quem está devolvendo o livro: ").lower()
        if (nome not in self.Registros):
            return f"{nome.title()} não foi encontrado"
        
        livro_a_ser_Devolvido = input("Digite o título do livro a ser devolvido: ").lower()
        
        if (livro_a_ser_Devolvido in self.Registros[nome]):
            del self.Registros[nome][livro_a_ser_Devolvido]

            if (self.Registros[nome] == {}):
                del self.Registros[nome]

            return f"*Livro '{livro_a_ser_Devolvido.title()}' devolvido com sucesso.*"
    
        return f"O livro '{livro_a_ser_Devolvido.title()}' não está entre os livros emprestados de {nome.title()}."

    def ContarLivrosEmprestados(self):
        print(self.Registros)
        totalDeLivrosEmprestados = sum(sum(livros.values()) for livros in self.Registros.values())

        return f"*Atualmente, há {totalDeLivrosEmprestados} livro(s) emprestado(s).*"