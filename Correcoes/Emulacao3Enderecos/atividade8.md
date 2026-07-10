## Trabalho 08 - Emulação do Código de Três Endereços

Este trabalho é a construção de um emulador para a Codificação de Três Endereços. O programa deve ler um arquivo de entrada codificado na abordagem de três endereços e deve executar esse código.

A sugestão é que seja gerado uma ​**gramática ANTLR**​, baseado nos slides sobre código de três endereços, e um **Visitor** para percorrer a árvore de parsing e executar cada instrução.

Considere que as instruções serão, somente: atribuição, operações aritméticas (soma, subtração, multiplicação e divisão), operações lógicas (and, or, not) e relacionais (>, >=, <, <= e !=), if, while, definição e chamada de funções (neste momento não precisam ser recursivas) e impressão de uma variável ou constante.

**O que deve ser entregue:**

1) A gramática que gera a codificação de três endereços;
2) O programa em Python que implementa o Visitor;
3) O programa principal em Python que instancia os outros objetos, lê o arquivo de entrada e gera a saída (que pode ser um arquivo ou impresso na tela);
4) Pelo menos cinco casos de teste, desde os mais simples até os mais complexos, explorando as várias facetas deste problema;
5) Junte todos os arquivos e comprima utilizando o compactador ZIP. Coloque o seu nome como nome do arquivo zipado.
