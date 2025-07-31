from ControleEmprestimos import sistemaDeEmprestimos
import sys
from PyQt5.QtWidgets import QApplication
from Interface import TelaPrincipal

def menu():
    print()
    print("Menu de opções:")
    print("1 - Registrar empréstimo")
    print("2 - Registrar devolução")
    print("3 - Contar livros emprestados")
    print("4 - Sair")
"""
def main():
    fazerOperacao = sistemaDeEmprestimos()

    while True:
        menu()
        try:
            escolha = int(input("Escolha uma opção: "))
            
            if (escolha == 1):
                result = fazerOperacao.RegistrarEmprestimo()
                print(result)
            elif (escolha == 2):
                result = fazerOperacao.FazerDevolução()
                print(result)
            elif (escolha == 3):
                result = fazerOperacao.ContarLivrosEmprestados()
                print(result)
            elif (escolha == 4):
                print("Encerrando o sistema de empréstimo de livros. Até a próxima!")
                break
            else:
                print("Operação inválida, escolha uma das opções")
        except ValueError:
            print("Valor inválido")
"""
if __name__=="__main__":
    app = QApplication(sys.argv)
    janela = TelaPrincipal()
    janela.show()
    sys.exit(app.exec_())