Trabalho 07 - Representação Intermediária
Este trabalho tem a ver com a representação intermediária baseado no "código de três endereços"  para a linguagem MiniC. Este trabalho pode ser feito individual ou em duplas.

O que deve ser feito:

1. Receber via linha de comando um arquivo com o código de entrada na linguagem MiniC e gerar um outro arquivo com a transformação desse arquivo de entrada no respectivo código intermediário de três endereços.

2. A solução deve estar integrada com o analisador semântico, ou seja, só gerar a representação intermediária se o código de entrada não possuir nenhum erro léxico, sintático ou semântico.

3. Sugestão: utilize o padrão de projeto VISITOR.

O que deve ser entregue:

O arquivo com a gramática utilizada, o Visitor, o programa Python principal e pelo menos cinco arquivos de entrada utilizados como caso de testes. Compacte todos os arquivos usando o ZIP. Coloque os integrantes da equipe como o nome do arquivo.

OBSERVAÇÕES:

(1) Considere que a gramática do MiniC inclui também o tipo char;

(2) Como este trabalho pode ser feito individual ou em duplas, somente uma pessoa deve enviar o trabalho. Para não haver engano, inclua os nomes dos membros da equipe em todos os arquivos.



Executar o arquivo
python main.py input.c