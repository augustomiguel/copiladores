"""
as --64 -o novo.o novo.s
ld -o novo novo.o
"""

import os
nomeArq = 'entrada.ci'

try:
    with open(nomeArq, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        linha = linhas[0].strip()
        try :
            numero = int(
                linha)
            #print(f"O número é {numero}.")
        except ValueError:
            print("A primeira linha não é um número válido.")

except FileNotFoundError:
    print(f"Erro: Arquivo '{nomeArq}' não encontrado.")
except Exception as e:
    print(f"Erro ao abrir arquivo '{nomeArq}': {e}")
    
comando= 'mov ${}, %rax'.format(numero)
nomeArq = 'novo.s'
modelo = '''
 .section .text
 .globl _start

_start:
  {}
  call imprime_num
  call sair

  .include "runtime.s"
  
  '''.format(comando)
        
with open(nomeArq, "w", encoding="utf-8") as arquivo:
    arquivo.write(modelo)

print("\nassembly \n")

os.system('as --64 -o novo.o novo.s')
os.system('ld -o novo novo.o')
os.system('./novo')

