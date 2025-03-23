import unittest
from GeradorAssembly import GeradorAssembly

class TestGeradorAssembly(unittest.TestCase):
    
    # Teste de constante
    def teste_constante(self):
        codigo = "222"
        gerador = GeradorAssembly(codigo)
        arvore, assembly = gerador.gerar_assembly()

        assembly_esperado = """
mov $222, %rax
"""
        self.assertEqual(assembly.strip(), assembly_esperado.strip())

    # Teste de soma
    def teste_soma(self):
        codigo = "(7 + 11)"
        gerador = GeradorAssembly(codigo)
        arvore, assembly = gerador.gerar_assembly()

        assembly_esperado = """
mov $7, %rax
push %rax
mov $11, %rax
pop %rbx
add %rbx, %rax
"""
        self.assertEqual(assembly.strip(), assembly_esperado.strip())

    # Teste de subtração
    def teste_subtracao(self):
        codigo = "(3 - 4)"
        gerador = GeradorAssembly(codigo)
        arvore, assembly = gerador.gerar_assembly()

        assembly_esperado = """
mov $3, %rax
push %rax
mov $4, %rax
mov %rax, %rbx
pop %rax
sub %rbx, %rax
"""
        self.assertEqual(assembly.strip(), assembly_esperado.strip())

    # Teste de multiplicação
    def teste_multiplicacao(self):
        codigo = "(5 * 6)"
        gerador = GeradorAssembly(codigo)
        arvore, assembly = gerador.gerar_assembly()

        assembly_esperado = """
mov $5, %rax
push %rax
mov $6, %rax
pop %rbx
imul %rbx, %rax
"""
        self.assertEqual(assembly.strip(), assembly_esperado.strip())

    # Teste de divisão
    def teste_divisao(self):
        codigo = "(10 / 2)"
        gerador = GeradorAssembly(codigo)
        arvore, assembly = gerador.gerar_assembly()

        assembly_esperado = """
mov $10, %rax
push %rax
mov $2, %rax
mov %rax, %rbx
pop %rax
div %rbx, %rax
"""
        self.assertEqual(assembly.strip(), assembly_esperado.strip())

    # Teste de expressão
    def teste_expressao(self):
        codigo = "((427 / 7) + (11 * (231 + 5)))"
        gerador = GeradorAssembly(codigo)
        arvore, assembly = gerador.gerar_assembly()

        assembly_esperado = """
mov $427, %rax
push %rax
mov $7, %rax
mov %rax, %rbx
pop %rax
div %rbx, %rax
push %rax
mov $11, %rax
push %rax
mov $231, %rax
push %rax
mov $5, %rax
pop %rbx
add %rbx, %rax
pop %rbx
imul %rbx, %rax
pop %rbx
add %rbx, %rax
"""
        self.assertEqual(assembly.strip(), assembly_esperado.strip())

if __name__ == "__main__":
    unittest.main()
