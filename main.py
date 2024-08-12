import random
from os import system, name

def limpar_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac e Linux
    else:
        _ = system('clear')

# Função que desenha a forca na tela
def display_hangman(tentativas_restantes):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tentativas_restantes]

def game():
    limpar_tela()
    print('\nBem-Vindo ao jogo da forca em Python!')
    print('Adivinhe a palavra abaixo:\n')

    # 1- Definir a lista de palavras possíveis:
    lista_palavras = ['banana', 'uva', 'acerola', 'melao','kiwi']

    # 2- Escolher uma palavra aleatória da lista
    palavra_aleatoria = random.choice(lista_palavras)

    # 3- List comprehension para colocar _ na palavra escolhida
    ocultando = ['_' for _ in palavra_aleatoria]

    # 4- Criar uma lista vazia para armazenar as letras erradas
    letras_erradas = []

    # 5- Definir o número máximo de tentativas permitidas
    MAXIMO_TENTATIVAS = 6  # Reduzi para 6 para alinhar com os estágios da forca

    # 6- Iniciar o loop do jogo
    while MAXIMO_TENTATIVAS > 0:
        print(display_hangman(MAXIMO_TENTATIVAS))
        print(' '.join(ocultando))
        print('Chances restantes:', MAXIMO_TENTATIVAS)
        print('Letras erradas:', ', '.join(letras_erradas))

        tentativa = input('Digite uma letra: ').lower()

        if tentativa in palavra_aleatoria:
            for index, letra in enumerate(palavra_aleatoria):
                if tentativa == letra:
                    ocultando[index] = letra
        else:
            letras_erradas.append(tentativa)
            MAXIMO_TENTATIVAS -= 1

        if '_' not in ocultando:
            print('VOCÊ VENCEU!!! A palavra era:', ''.join(palavra_aleatoria))
            break
    else:
        print(display_hangman(0))
        print('Você perdeu! A palavra era:', ''.join(palavra_aleatoria))

if __name__ == "__main__":
    game()
