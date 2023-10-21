from conect import conect


class Funcionario:
    def __init__(self, cod, nome, login, senha):
        self.cod = cod
        self.nome_info = nome
        self.login_info = login
        self.senha_info = senha

    def ola():
        print('ola, eu sou um funcionario')

