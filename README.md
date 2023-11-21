# Termos de Bronze TrabalhoG2.SIS2 

*O trabalho do jogo "Termo" foi feito por:**Roberto Waide e Arthur Santiago Pereira de Sena***

*A segunda proposta dada para o trabalho avaliativo do professor* ***Jardel Felipe Knirsch*** *involve entre pares programarem uma simulação do jogo https://term.ooo revisando a materia de exceptions e manipulação de arquivo*

# O programa desta vez esta dividido entre as etapas de Manipulação dos Arquivos e o jogo em si

(Portanto alguns defs foram incluidos em relação a formatação de prints coloridos)
(Vale resaltar que o codigo tem comentarios em si para a explicação de cada parte)

-"**Manipulação de Arquivos**": O codigo começã com 3 variaveis denominadas de "counter" onde sera armazenado o contador de tentavivas do jogador, "words" onde sera selecionada uma palavra para a partida e "black_list" que é usado para escrever no arquivo "black_file.txt" quais palavras já foram escolhidas. Se a variavel "words" for retornada vazia ele cancela a rodada e limpa o arquivo de "black_file.txt"

Se a variavel "words" retornar com uma palavra ela passara para uma lista de words_spell, ela escreve a palavra escolhida para o arquivo "black_file.txt" e separa a palavra e pede o input do jogador. 

O jogador pode pedir as regras do jogo digitando um "?" as regras do jogo serão mostradas para o jogador com um print. Caso o jogador escrever algo que não seja uma letra do alfabeto ou palavras de mais de 5 letras sera puxado o seu respectivo exception.

O codigo irá ver a resposta do jogador e adicionará a uma lista de sugestões para depois poder ser analisado e potencialmente ser adicionado a lista de palavras possiveis no jogo. Além disso, a resposta do jogador pasará por uma confirmação usando o word_spell para checar se cada letra está em seu devido lugar, se estiver ela vira-ra verde, se ela estiver apenas na palavra mas em um lugar errado ela vira-ra amarela e se não estiver ela sera denominada pela cor preta.

O jogo irá terminará assim que o jogador conseguir acertar a palavra antes de cinco tentativas ou falhar tentando.

