# gera-codigo(arv) : gera assmebly p/ arv. resultado em rax


# codigo fonte 
# 42

# saida:
# mov $42, rax

# codigo-fonte
# (7+10)

# saida:
# mov $7, rax
# mov %rax, rbx
# mov $11, %rax
# add $rbx, $rax


# exercicio escreva a saida para o codigo	fonte 
# (7+(8+15))

# operando esquerdo
# mov $7, %rax
# mov %rax, %rcx

# operando direito
# mov $8, %rax
# mov %rax, %rbx
# mov $15, %rax
# add %rbx, %rax

# add %rcx, %rax


# com a pilha 

# operando esquerdo
# mov $7, %rax
# push %rax

# operando direito
# mov $8, %rax
# push %rax
# mov $15, %rax
# pop %rbx
# add %rbx, %rax

# pop %rbx
# add %rbx, %rax

# RSP (Starck pointer)


gera_codigo(arv):
    if (arv constante):
        'mov ${valor}, %rax
    else
    op_esq = gera_codigo(esq)
    op_dir = gera_codigo(dir)

    result = 
    op_esq
    push %rax
    op_dir
    pop %rbx
    
    
    


