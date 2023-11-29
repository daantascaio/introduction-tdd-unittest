import requests


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obter_todos_os_dados(self):
        response = requests.get('www.google.com.br')

        if response.ok:
            self.dados_obtidos = True
            return '🟢 CONNECTED'
        else:
            self.dados_obtidos = False
            return '🔴 ERRO_404'
