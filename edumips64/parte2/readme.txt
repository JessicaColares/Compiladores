Trabalho 11 - Geração de Código Assembly do EduMIPS64 (parte 2)
Este trabalho é a continuação da geração de código Assembly do EduMIPS  a partir do código intermediário utilizando a codificação de três endereços.

O que deve ser feito:

Integrar a transformação para o código Assembly do MIPS com os analisadores léxico, sintático, semântico e gerador do código intermediário. Ou seja, a entrada será o código do MiniC e deve gerar como saída o código Assembly do EduMIPS. Obviamente que só deve gerar os códigos intermediário e assembly se o código de entrada do MiniC não possuir nenhum erro léxico, sintático ou semântico. Gere um "script" que integre todas as chamadas de todos os programas.

OBSERVAÇÕES:

(1) Considere que a gramática do MiniC inclui somente o tipo "int" e o tipo "char";

(2) Vamos considerar chamadas de função simples ou aninhadas, recursivas ou não, com a possibilidade de ter mais de quatro parâmetros;

(3) Você pode ajustar qualquer parte do compilador que se fizer necessário;

(4) Só será aceito o Assembly do MIPS que execute no simulador EduMIPS64, que é ligeiramente diferente de outros simuladores MIPS;

(5) Este trabalho pode ser feito individual ou em duplas, mas somente uma pessoa deve enviar o trabalho. Para não haver engano, inclua os nomes dos membros da equipe em todos os arquivos; e

(6) Compacte todos os arquivos usando o ZIP. Coloque os integrantes da equipe no nome do arquivo.