# Projeto Python análise COVID-19
[![GitHub license](https://img.shields.io/github/license/WellingtonOliveira95/questionario_covid)](https://github.com/WellingtonOliveira95/questionario_covid/blob/master/LICENSE)

## Sobre o projeto:
Neste projeto utilizei como linguagem o Python, nele faço uma requisição no viacep.com.br para consumir a API e gerar um dado para localizar o usuário em caso de necessidade de assistência médica!
O usuário da entrada em seu nome e CEP onde reservo estas variáveis.

As questões me embasei em sites e pesquisas contendo alguns dos principais sintomas para COVID-19, onde acrescento 1 para respostas positivas a pergunta de sintoma e 2 para negativas.

No final das questões verifico o valor final da variável receptora desta soma de respostas positivas e com uma análise de quantidade de respostas retorno ao usuário qual a possibilidade de estar resfriado, gripado ou com COVID em uma escala de 1 a 6 (quantidade de perguntas).
Caso retorne grandes chances de estar infectado ou então com gripe utilizo o **.format()** e uso os dados da API para informar que ele deve procurar um médico/assistência na cidade/bairro que reside.

## Autor:
Wellington Oliveira.
Linkedin: https://www.linkedin.com/in/wellingtonsoliveira/
