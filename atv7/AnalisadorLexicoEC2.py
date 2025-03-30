# Alunos: André Lopes; Augusto Miguel; Elias Victor; Henrique Bandeira; Pedro Lucas.

import re

class Token:
    def __init__(self, tipo, lexema, posicao):
        self.tipo = tipo
        self.lexema = lexema
        self.posicao = posicao

    def __repr__(self):
        return f"<{self.tipo}, \"{self.lexema}\", {self.posicao}>"

class AnalisadorLexico:
    TOKEN_REGEX = [
        (r'\d+', 'Numero'),
        (r'\+', 'Soma'),
        (r'-', 'Subtr'),
        (r'\*', 'Mult'),
        (r'/', 'Div'),
        (r'\(', 'ParenEsq'),
        (r'\)', 'ParenDir'),
        (r'\s+', None),
    ]

    def __init__(self, codigo):
        self.codigo = codigo
        self.posicao = 0
        self.parenteses_balanceados = 0

    def proximo_token(self):
        if self.posicao >= len(self.codigo):
            return None

        for padrao, tipo in self.TOKEN_REGEX:
            regex = re.compile(padrao)
            match = regex.match(self.codigo, self.posicao)
            if match:
                lexema = match.group(0)
                posicao = self.posicao
                self.posicao += len(lexema)
                if tipo:
                    if tipo == 'ParenEsq':
                        self.parenteses_balanceados += 1
                    elif tipo == 'ParenDir':
                        self.parenteses_balanceados -= 1
                    return Token(tipo, lexema, posicao)
                return self.proximo_token()

        raise ValueError(f"Caractere inesperado '{self.codigo[self.posicao]}' na posição {self.posicao}")

    def verificar_erro(self, tokens):
        ultimo_token = None
        for token in tokens:
            if ultimo_token:
                if ultimo_token.tipo in ['Soma', 'Subtr', 'Mult', 'Div'] and token.tipo in ['Soma', 'Subtr', 'Mult', 'Div', 'ParenDir']:
                    raise ValueError(f"Operador '{ultimo_token.lexema}' sem operando na posição {ultimo_token.posicao}")
            ultimo_token = token

        if self.parenteses_balanceados != 0:
            raise ValueError("Parênteses desbalanceados")


    def analisar(self):
        if self.codigo.isdigit():
            tokens = []
            while self.posicao < len(self.codigo):
                token = self.proximo_token()
                if token:
                    tokens.append(token)
            return tokens
        
        tokens = []
        while self.posicao < len(self.codigo):
            token = self.proximo_token()
            if token:
                tokens.append(token)

        self.verificar_erro(tokens)
        return tokens

def analisar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    for num_linha, linha in enumerate(linhas, start=1):
        linha = linha.strip()
        if not linha:
            continue

        analisador = AnalisadorLexico(linha)
        try:
            tokens = analisador.analisar()
            print(f"{num_linha}ª EC1:")
            for token in tokens:
                print(token)
            print()
        except ValueError as e:
            print(f"Erro na {num_linha}ª EC1: {e}")

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo: ")
    try:
        analisar_arquivo(nome_arquivo)
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except ValueError as e:
        print(f"Erro léxico encontrado: {e}")
