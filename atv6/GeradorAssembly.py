# Alunos: André Lopes; Augusto Miguel; Elias Victor; Henrique Bandeira; Pedro Lucas.

from AnalisadorLexico import AnalisadorLexico
from AnalisadorSintatico import AnalisadorSintatico, OpBin, Const

class GeradorAssembly:
    def __init__(self, codigo):
        self.codigo = codigo
        self.analisador_lexico = AnalisadorLexico(codigo)
        self.tokens = self.analisador_lexico.analisar()
        self.analisador_sintatico = AnalisadorSintatico(self.tokens)

    def gerar_assembly(self):
        try:
            arvore = self.analisador_sintatico.analisar_expressao()
            assembly = self.gerar_assembly_da_arvore(arvore)
            return arvore, "\n".join(assembly)
        except ValueError as e:
            return f"Erro na análise sintática: {e}"

    def gerar_assembly_da_arvore(self, arvore):
        if isinstance(arvore, Const):
            return [f"mov ${arvore.valor}, %rax"]

        elif isinstance(arvore, OpBin):
            assembly = []

            assembly.extend(self.gerar_assembly_da_arvore(arvore.op_esq)) 
            assembly.append("push %rax")

            assembly.extend(self.gerar_assembly_da_arvore(arvore.op_dir))

            if arvore.operador == "+":
                assembly.append("pop %rbx")
                assembly.append("add %rbx, %rax")
            elif arvore.operador == "-":
                assembly.append("mov %rax, %rbx")
                assembly.append("pop %rax")
                assembly.append("sub %rbx, %rax")
            elif arvore.operador == "*":
                assembly.append("pop %rbx")
                assembly.append("imul %rbx, %rax")
            elif arvore.operador == "/":
                assembly.append("mov %rax, %rbx")
                assembly.append("pop %rax")
                assembly.append("div %rbx, %rax")
            else:
                raise ValueError(f"Operador desconhecido: {arvore.operador}")

            return assembly

if __name__ == "__main__":
    codigo = input("Digite a expressão: ")
    gerador = GeradorAssembly(codigo)
    arvore, assembly = gerador.gerar_assembly()

    print("Árvore Sintática:")
    print(arvore.imprimir())

    print(f"""
    .section .text
    .globl _start

    _start:
        {assembly}

        call imprime_num
        call sair

    .include "runtime.s"
    """)
