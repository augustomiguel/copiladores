1. Preparação do ambiente:
    -> Tenha o Python instalado;
    -> O projeto usa apenas bibliotecas nativas do Python, não sendo necessário instalar mais nada.
    -> Certifique-se que a versão do Python instalada é a 3.13.2 ou superior.

2. Rodando o programa
   -> Abra o terminal e execute o script:
        python GeradorAssembly.py
     

3. Entradas:
    -> Para funcionar adequadamente, todas as operações devem estar entre parênteses com excessão de constantes.
        Exemplos: (4+2); ((4-5) + 3); 222.

4. Saída:
    -> Será gerado no terminal um código Assembly equivalente à expressão matemática digitada.

5. Estrutura do código
    -> O código foi estruturado em três componentes principais:

    - **AnalisadorLexico**: Realiza a análise léxica da expressão identificando tokens como números e operadores.
    - **AnalisadorSintatico**: Realiza a análise sintática construindo a árvore da expressão e validando sua estrutura.
    - **GeradorAssembly**: Converte a árvore sintática em código Assembly que pode ser executado.

6. Classe de teste
    -> Além disso, há uma classe de teste chamada "TesteGerador".
        Ela basicamente vai conter testes a respeito dos casos base cujos códigos em Assembly já são conhecidos para validar o funcionamento. Além disso, também há um teste com uma expressão maior. Ao executar essa classe, ela deve imprimir um "OK" demonstrando que está correto.