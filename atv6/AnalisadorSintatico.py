# Alunos: André Lopes; Augusto Miguel; Elias Victor; Henrique Bandeira; Pedro Lucas.

class Exp:
    def avaliar(self):
        raise NotImplementedError("")

    def imprimir(self):
        raise NotImplementedError("")

class Const(Exp):
    def __init__(self, valor):
        self.valor = valor

    def avaliar(self):
        return self.valor

    def imprimir(self):
        return str(self.valor)

    def __repr__(self):
        return str(self.valor)

class OpBin(Exp):
    def __init__(self, operador, op_esq, op_dir):
        self.operador = operador
        self.op_esq = op_esq
        self.op_dir = op_dir

    def avaliar(self):
        esq = self.op_esq.avaliar()
        dir = self.op_dir.avaliar()
        if self.operador == '+':
            return esq + dir
        elif self.operador == '-':
            return esq - dir
        elif self.operador == '*':
            return esq * dir
        elif self.operador == '/':
            if dir == 0:
                raise ValueError("Divisão por zero")
            return esq / dir
        else:
            raise ValueError(f"Operador desconhecido: {self.operador}")

    def imprimir(self):
        return f"({self.operador} {self.op_esq.imprimir()} {self.op_dir.imprimir()})"

    def __repr__(self):
        return f"({self.operador} {self.op_esq} {self.op_dir})"

class AnalisadorSintatico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def proximo_token(self):
        if self.pos >= len(self.tokens):
            return None
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def ver_token(self):
        if self.pos >= len(self.tokens):
            return None
        return self.tokens[self.pos]

    def analisar_expressao(self):
        token = self.proximo_token()
        if token.tipo == 'Numero':
            return Const(int(token.lexema))
        elif token.tipo == 'ParenEsq':
            esq = self.analisar_expressao()
            operador = self.proximo_token()
            if operador.tipo not in ['Soma', 'Subtr', 'Mult', 'Div']:
                raise ValueError(f"Operador inválido: {operador}")
            dir = self.analisar_expressao()
            fecha = self.proximo_token()
            if fecha.tipo != 'ParenDir':
                raise ValueError("Parêntese fechando esperado")
            return OpBin(operador.lexema, esq, dir)
        else:
            raise ValueError(f"Token inesperado: {token}")

if __name__ == "__main__":
    from AnalisadorLexico import AnalisadorLexico

    codigo = input("Digite a expressão: ")
    analisador_lexico = AnalisadorLexico(codigo)
    tokens = analisador_lexico.analisar()

    analisador_sintatico = AnalisadorSintatico(tokens)
    try:
        arvore = analisador_sintatico.analisar_expressao()
        print("Árvore Sintática:")
        print(arvore.imprimir())
        print("Resultado:", arvore.avaliar())
    except ValueError as e:
        print("Erro de análise:", e)
