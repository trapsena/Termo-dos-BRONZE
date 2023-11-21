import random
import os

def print_colored(message,code): # adiciona para lista com cor
    present.append(f"\033[{code}m {message}\033[00m") 
def warning(message,code): # mensagem de aviso com cor
    print(f"\033[{code}m {message}\033[00m")
def warning2(message,code): # mensagem de aviso com cor com junção de linha
    print(f"\033[{code}m {message}\033[00m",end="")



while True:
    counter = 0 # Contador de tentativas
    words=[] # palavras a serem sorteasdas ## Ambas listas são temporarias e
    black_list = [] # palavras já usadas   ## são reiniciadas toda nova partida

    with open("black_file.txt", "r") as file:
        for line in file:
            black_list.append(line) # guarda palavras já usadas para não repetir
    
    with open("words.txt", "r") as file:
        for line in file:
            if line not in black_list: #passsa apena palavras novas
                words.append(line) # adiciona a leva de palavras
              

    if words == []:
        with open("black_file.txt", "w") as file:
            file.write("") # limpa a black_list caso todas palavras tenham sido usadas
    else:
        word_game = random.choice(words) # sorteia a palavra da vez

        word_spell = []
        for i in word_game:
            if i != "\n":
                word_spell.append(i.upper()) # separa a palavra por letras

        print("\nDigite ? para ver as regras!")

        while True:
            while True:
                player_choise = []
                try:
                    player_w = input(f"\nDigite uma palavra: ").upper()
                    if player_w == "-----":
                        counter = 6
                    elif player_w == "?": # regras
                        print("\nDescubra a palavra certa em 6 tentativas. Depois de cada tentaviva,\nas letras mostram o quão perto da resposta\n\nA",end ="")
                        warning2("letra verde ",92)
                        print("faz parte da palavra e está na posição certa.\n\nA", end="")
                        warning2("letra amarela ",93)
                        print("faz parte da palvra mas em outra posição.\n\nA", end="")
                        warning2("letra preta ",2)
                        print("não faz parte da palavra.\n\nOs aventos não são preenchidos.\nAs palavra pode possuir letras repetidas.")
                    elif player_w.isalpha() == False: # bloqueia caracteres diferentes de letras
                        raise BaseException("\nUse apenas letras")
                    elif len(player_w) != 5: # bloquia palavras com menos ou mais de 5 letras
                        raise BaseException('\nUse uma palavra com apenas 5 letras >w<" ')
                    break 
                except BaseException as error:
                    warning(error,91)
            if player_w != "?": # Se for a explicação o codigo n roda e apenas da print na explicação
                for i in player_w:
                    player_choise.append(i) # soletra a palavra do jogador

                if (f"{player_w.lower()}\n") not in words and (f"{player_w.lower()}\n") not in black_list:
                    with open("sugestions.txt", "a") as file: # sugestão de palavras
                        file.write(f"{player_w.lower()}\n")
                    
                present = [] #coloração da palavra escrita pelo jogador
                for u in range(5):
                    if player_choise[u] == word_spell[u]: 
                        print_colored(player_choise[u], 92) # verde - quando a letra está certa
                    elif player_choise[u] in word_spell:
                        print_colored(player_choise[u], 93) # amarelo - quando tem a letra mas posição errada
                    else:
                        print_colored(player_choise[u], 2) # preto - quando não tem a letra


                present = "  | ".join(present)  # formatação para apresentar
                print(f"\n{present}")

                if player_choise == word_spell: # sistema de vitoria - quando a palavra do jogador e a escolhida são iguais ativa a condição
                    warning("\nYou WIN!!",92)
                    input("\nDigite enter para um novo jogo.")
                    with open("black_file.txt", "a") as file:
                        file.write(word_game)  # exclui a palvra escolhida da proxima vez
                    os.system('cls')
                    break
                elif counter == 5: # caso o contador de a tntativa limite, o jogo acaba em derrota (e puxa o seu elo para baixo)
                    warning("\nYou LOSE.",91)
                    print(f"\n{word_spell}")
                    input("\nDigite enter para um novo jogo. ")    
                    os.system('cls')
                    break
                counter += 1
        
















# BRONZE TAMBEM É GENTE
