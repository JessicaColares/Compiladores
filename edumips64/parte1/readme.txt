Trabalho 10 - Geração de Código Assembly do EduMIPS64 (parte 1)
Este trabalho tem a ver SOMENTE com a geração de código Assembly do EduMIPS  a partir do código intermediário utilizando a codificação de três endereços.

O que deve ser feito:

1) (7.0 pontos) Receber via linha de comando um arquivo com o código intermediário utilizando a codificação de três endereços. Gerar um outro arquivo com a transformação da entrada no respectivo código Assembly do MIPS que execute no simulador EduMIPS64. No código EduMIPS incluir comentários para cada linha do Código de Três Endereços (como foi mostrado nos exemplos dos slides).

2) (3.0 pontos) Executar o gerador de código EduMIPS (do item anterior) sobre um Código de Três Endereços, que contenha função com mais de quatro argumentos, uma variável global, pelo menos uma variável local, atribuição com expressões aritméticas, if-then-else e while. Inclua comentários indicando cada parte. Incluir os prints de tela.



Exemplo de estudo de caso em C simplificado que precisa ser transformado em Código de Três Endereços.



int global_counter = 0;
void process_data(int a, int b, int c, int d, int e) {
  int local_sum = a + b + c + d + e;
  if (local_sum >= 100) {
    global_counter = global_counter + 1;
  } else {
    global_counter = global_counter - 1;
  }
  while (global_counter < 5) {
    global_counter = global_counter + 2;
  }
}
int main(void) {
  process_data(10, 20, 30, 5, 8);
  printf("global_counter: %d\n", global_counter);
}


OBSERVAÇÕES:

(1) Só será aceito o Assembly do MIPS que execute no simulador EduMIPS64, que é ligeiramente diferente de outros simuladores MIPS;

(2) Este trabalho pode ser feito individual ou em duplas, mas somente uma pessoa deve enviar o trabalho. IMPORTANTE! Para não haver engano, inclua os nomes dos membros da equipe em todos os arquivos;

(3) O gerador de código pode ser feita por um programa Python à parte, mas tem que ser escrito em Python; e

(4) Compacte todos os arquivos usando o ZIP. Coloque os integrantes da equipe como o nome do arquivo.


python geradorEduMIPS64.py test.tac > output.asm