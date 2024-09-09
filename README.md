Introdução ao Projeto: Quiz Bíblico Interativo em Python

Bem-vindo ao "Quiz Bíblico Interativo", um projeto em Python que combina programação e conhecimento bíblico para proporcionar uma experiência divertida e educativa. Este projeto utiliza a biblioteca colorama para criar uma interface de quiz visualmente atraente no terminal, oferecendo uma experiência interativa por meio de cores.

O que é o Quiz Bíblico Interativo?
O Quiz Bíblico Interativo é um jogo de perguntas e respostas que testa seu conhecimento sobre a Bíblia. O projeto é estruturado para oferecer duas categorias de perguntas: o Antigo Testamento e o Novo Testamento. O usuário pode escolher a categoria que deseja explorar e responder a uma série de perguntas relacionadas.

Como Funciona?
Inicialização e Configuração:

A biblioteca colorama é utilizada para colorir o texto exibido no terminal, proporcionando uma experiência visual rica. A função init() da biblioteca prepara o ambiente para o uso das cores.
Função exibir_perguntas:

Esta função é responsável por exibir as perguntas e alternativas ao usuário. Ela também lida com a captura da resposta do usuário, verifica se a resposta está correta e atualiza a pontuação conforme as respostas fornecidas.
Função quiz:

A função principal do programa. Ela dá boas-vindas ao usuário e solicita a escolha de uma das duas categorias de perguntas. Dependendo da escolha, um conjunto específico de perguntas é carregado e passado para a função exibir_perguntas.
Resultado e Encerramento:

Após a resposta a todas as perguntas, a pontuação final do usuário é exibida, mostrando quantas perguntas foram respondidas corretamente. O programa então aguarda que o usuário pressione Enter para encerrar.
