import time


class Jogador:
    jogadores = []

    def __init__(self, name='', letter=''):
        self.nome = name
        self.letra = letter
        Jogador.jogadores.append(self)


def delay():
    time.sleep(0.5)


def cria_board():  # CRIA O TABULEIRO DE 3 LINHAS E 3 COLUNAS, COM SEUS RESPECTIVOS VALORES DA POSIÇÃO
    tabuleiro = {
        1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '
    }
    return tabuleiro


def exibe_board(board):
    print(' ' + board[1] + ' │ ' + board[2] + ' │ ' + board[3] + ' ')
    print('───┼───┼───')
    print(' ' + board[4] + ' │ ' + board[5] + ' │ ' + board[6] + ' ')
    print('───┼───┼───')
    print(' ' + board[7] + ' │ ' + board[8] + ' │ ' + board[9] + ' ')
    print('')


def cria_jogadores(valor):
    humano = Jogador('humano', 'X')
    computador = Jogador('computador', 'O')

    if valor == 0:
        humano.letra = 'O'
        computador.letra = 'X'

    return humano, computador


def definir_primeiro_jogador():
    delay()
    opcao = int(input("Digite 1 para jogar primeiro, ou 0 para o computador iniciar:"))
    if opcao == 1:
        print("Você é o primeiro a jogar!")
        return True
    elif opcao == 0:
        print("O computador inicializa o jogo!")
        return False
    else:
        print("Opção inválida! Digite novamente")
        definir_primeiro_jogador()


def espaco_vazio(board, posicao):  # verifica se a posicao escolhida pelo jogador no tabuleiro está vazia
    if board[posicao] == ' ':
        return True
    else:
        return False


def encontra_jogador_ia():
    for jogador in Jogador.jogadores:
        if jogador.nome == "computador":
            return jogador


def encontra_jogador_humano():
    for jogador in Jogador.jogadores:
        if jogador.nome == "humano":
            return jogador


def jogar_novamente():
    print("")
    opcao = input("Deseja jogar novamente? S/n")

    if opcao == "S" or opcao == "s":
        print()
        main()
    else:
        exit()


def inserir_letra(board, letra, posicao):  # inserir valor da jogada no tabuleiro
    delay()

    if espaco_vazio(board, posicao):
        board[posicao] = letra
        print()
        exibe_board(board)

        if verifica_empate(board):
            print("Empate")
            jogar_novamente()
        elif vitoria(board):
            if letra == encontra_jogador_ia().letra:
                print("Computador venceu!")
            elif letra == encontra_jogador_humano().letra:
                print("Você ganhou!")
            jogar_novamente()
        return

    else:
        print("A posição escolhida já está ocupada!")
        delay()
        posicao = int(input("Escolha uma nova posição: "))
        inserir_letra(board, letra, posicao)
        return


def movimento_humano(board, humano):
    posicao = int(input('Digite a posição na qual deseja jogar ' + humano.letra + ': '))
    inserir_letra(board, humano.letra, posicao)
    return


def movimento_ia(board, ia):
    melhor_pontuacao = -800
    melhor_movimento = 0

    for key in board.keys():
        if board[key] == ' ':
            board[key] = ia.letra
            pontuacao = minimax(board, 0, False)
            board[key] = ' '
            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                melhor_movimento = key
    print('Jogada do computador:', melhor_movimento)
    inserir_letra(board, ia.letra, melhor_movimento)
    return


def verifica_empate(board):
    for chave in board.keys():
        if board[chave] == " ":
            return False
    return True


def checar_linha_vencedora(board, letra=None):
    if letra is None:
        if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
            return True
        elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
            return True
        elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
            return True
        else:
            return False
    else:
        if board[1] == board[2] and board[1] == board[3] and board[1] == letra:
            return True
        elif board[4] == board[5] and board[4] == board[6] and board[4] == letra:
            return True
        elif board[7] == board[8] and board[7] == board[9] and board[7] == letra:
            return True
        else:
            return False


def checar_coluna_vencedora(board, letra=None):
    if letra is None:
        if board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
            return True
        elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
            return True
        elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
            return True
        else:
            return False
    else:
        if board[1] == board[4] and board[1] == board[7] and board[1] == letra:
            return True
        elif board[2] == board[5] and board[2] == board[8] and board[2] == letra:
            return True
        elif board[3] == board[6] and board[3] == board[9] and board[3] == letra:
            return True
        else:
            return False


def checar_diagonal_vencedora(board, letra=None):
    if letra is None:
        if board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
            return True
        elif board[7] == board[5] and board[7] == board[3] and board[7] != ' ':
            return True
        else:
            return False
    else:
        if board[1] == board[5] and board[1] == board[9] and board[1] == letra:
            return True
        elif board[7] == board[5] and board[7] == board[3] and board[7] == letra:
            return True
        else:
            return False


def vitoria(board):
    if checar_linha_vencedora(board):
        return True
    elif checar_coluna_vencedora(board):
        return True
    elif checar_diagonal_vencedora(board):
        return True
    else:
        return False


def direcao_vencedora(board, jogador):
    if checar_linha_vencedora(board, jogador):
        return True
    elif checar_coluna_vencedora(board, jogador):
        return True
    elif checar_diagonal_vencedora(board, jogador):
        return True
    else:
        return False


def minimax(board, profundidade, valor_maximo):
    ia = encontra_jogador_ia()
    humano = encontra_jogador_humano()

    if direcao_vencedora(board, ia.letra):
        return 1
    elif direcao_vencedora(board, humano.letra):
        return -1
    elif verifica_empate(board):
        return 0

    if valor_maximo:
        melhor_pontuacao = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = ia.letra
                pontuacao = minimax(board, profundidade + 1, False)  # proximo movimento deve minimizar
                board[key] = ' '
                if pontuacao > melhor_pontuacao:
                    melhor_pontuacao = pontuacao
        return melhor_pontuacao

    else:
        melhor_pontuacao = 800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = humano.letra
                pontuacao = minimax(board, profundidade + 1, True)  # proximo movimento deve maximizar
                board[key] = ' '
                if pontuacao < melhor_pontuacao:
                    melhor_pontuacao = pontuacao
        return melhor_pontuacao


def main():
    board = cria_board()

    print('##################################################')
    print('#                 Jogo da Velha                  #')
    print('##################################################')
    print('')
    print('Digite o número referente a posição na qual você deseja jogar, ')
    print('seguindo o mapa abaixo:')
    print('')

    delay()

    print(' 1 │ 2 │ 3 ')
    print('───┼───┼───')
    print(' 4 │ 5 │ 6 ')
    print('───┼───┼───')
    print(' 7 │ 8 │ 9 ')
    print('')

    humano_primeiro = definir_primeiro_jogador()
    print('')

    if humano_primeiro:
        humano, computador = cria_jogadores(1)
        exibe_board(board)
        while not vitoria(board):
            delay()
            movimento_humano(board, humano)
            delay()
            movimento_ia(board, computador)
    else:
        humano, computador = cria_jogadores(0)
        while not vitoria(board):
            delay()
            movimento_ia(board, computador)
            delay()
            movimento_humano(board, humano)


if __name__ == '__main__':
    main()
