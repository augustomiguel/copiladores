# Alunos: André Lopes; Augusto Miguel; Elias Victor; Henrique Bandeira; Pedro Lucas.

from atv6.AnalisadorSintatico import Const, AnalisadorSintatico

class Exp:
    def __init__(self):
        self.ec1 = AnalisadorSintatico

    def prim(self):
        token = self.ec1.proximo_token()
        if token.tipo == 'Numero':
            return Const(int(token.lexema))
        elif token.tipo == 'ParenEsq':
            esq = self.exp_a()
            fecha = self.ec1.proximo_token()
            if fecha.tipo != 'ParenDir':
                raise ValueError("Parêntese fechado esperado")
            return esq
        else:
            raise ValueError(f"Token inesperado: {token}")

    def exp_m(self):
        esq = self.prim()
        token = self.ec1.proximo_token()
        while token == '*' or token == '/':
            avancaToken() # TODO
            dir = self.prim()
            if token == '*':
                operador = 'MULT'
            else:
                operador = 'DIV'
            esq = self.ec1.OpnBin(operador, esq, dir)
            token = self.ec1.proximo_token()
        return esq
    
    def exp_a(self):
        esq = self.exp_m()
        token = self.ec1.proximo_token()
        while token == '+' or token == '-':
            avancaToken() # TODO
            dir = self.exp_m()
            if token == '+':
                operador = 'SOMA'
            else:
                operador = 'SUB'

            esq = self.ec1.OpBin(operador, esq, dir)
            token = self.ec1.proximo_token()
        return esq
