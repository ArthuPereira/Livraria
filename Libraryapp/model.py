from conect import conect


class Funcionario:
    def __init__(self, cod, nome, login, senha):
        self.cod = cod
        self.nome_info = nome
        self.login_info = login
        self.senha_info = senha

    def ola():
        print('ola, eu sou um funcionario')

class FuncionarioDAO:
    @classmethod
    def logar(cls, login, senha):
        finalResult = False
        with conect() as conexao:
            with conexao.cursor() as cursor:
                query = f'SELECT login, senha FROM funcionario WHERE login = "{login}" AND senha = "{senha}"'
                cursor.execute(query)
                result = cursor.fetchall()

                while result:
                    infoLogin= result[0]['login']
                    infoSenha= result[0]['senha']
                    a = Funcionario()
                    result.pop()
                    finalResult = True
        return finalResult