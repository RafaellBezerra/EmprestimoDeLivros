from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QInputDialog, QMessageBox)
from ControleEmprestimos import sistemaDeEmprestimos
from unittest.mock import patch

class TelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Empréstimos")
        self.resize(400, 300)

        self.sistema = sistemaDeEmprestimos()

        botaoRegistrar = QPushButton("Registrar empréstimo")
        botaoFazerDevolucao = QPushButton("Fazer devolução")
        botaoContarLivros = QPushButton("Contar total de livros emprestados")
        botaoSair = QPushButton("Sair")

        layout = QVBoxLayout(self)
        layout.addWidget(botaoRegistrar)
        layout.addWidget(botaoFazerDevolucao)
        layout.addWidget(botaoContarLivros)
        layout.addWidget(botaoSair)

        botaoRegistrar.clicked.connect(self.RegistrarEmprestimo)
        botaoFazerDevolucao.clicked.connect(self.FazerDevolucao)
        botaoContarLivros.clicked.connect(self.ContarLivrosEmprestados)
        botaoSair.clicked.connect(self.close)

    def RegistrarEmprestimo(self):
        nome,ok1 = QInputDialog.getText(self, "emprestimo", "Digite o nome da pessoa")
        if (not (ok1 and nome)):
            return
        
        livro,ok2 = QInputDialog.getText(self, "emprestimo", "Digite o título do livro")
        if (not (ok2 and livro)):
            return

        # troca o valor original do input pelo valor minusculo das informações pedidas
        with patch("builtins.input", side_effect=[nome.lower(), livro.lower()]):
            resultado = self.sistema.RegistrarEmprestimo()
            
        QMessageBox.information(self, "Resultado", resultado)
    
    def FazerDevolucao(self):
        nome,ok1 = QInputDialog.getText(self, "devolucao", "Digite o nome da pessoa")
        nome = nome.lower()

        if (not (ok1 and nome)):
            return
        if (nome not in self.sistema.Registros):    
            QMessageBox.information(self, "Falha", f"{nome.title()} não foi encontrado")
            return
        
        livro,ok2 = QInputDialog.getText(self, "devolucao", "Digite o título do livro")
        livro = livro.lower()
        
        if (not (ok2 and livro)):
            return
        if (livro not in self.sistema.Registros[nome]):    
            QMessageBox.information(self, "Falha", f"O livro '{livro.title()}' não está entre os livros emprestados de {nome.title()}.")
            return

        with patch("builtins.input", side_effect=[nome, livro]):
            resultado = self.sistema.FazerDevolução()
        
        QMessageBox.information(self, "Resultado", resultado)

    def ContarLivrosEmprestados(self):
        resultado = self.sistema.ContarLivrosEmprestados()
        
        QMessageBox.information(self, "Resultado", resultado)