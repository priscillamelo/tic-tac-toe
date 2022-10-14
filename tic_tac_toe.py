import time

class Jogador:
    players = []


def delay():
    time.sleep(0.5)

def criarBoard():  # CRIA O TRABULEIRO DE 3 LINHAS E 3 COLUNAS, COM SEUS RESPECTIVOS VALORES DA POSIÇÃO
    tabuleiro = {
        1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '
    }
    return tabuleiro


def exibirBoard(board):
    print(' ' + board[1] + ' │ ' + board[2] + ' │ ' + board[3] + ' ')
    print('───┼───┼───')
    print(' ' + board[4] + ' │ ' + board[5] + ' │ ' + board[6] + ' ')
    print('───┼───┼───')
    print(' ' + board[7] + ' │ ' + board[8] + ' │ ' + board[9] + ' ')
    print('')


def criarJogadores(valor):
    humano = Jogador("humano", "X")
    computador = Jogador("computador", "O")

    if valor == 0:
        humano.letra = "O"
        computador.letra = "X"

    return humano, computador


def definirPrimeiroJogador():
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
        definirPrimeiroJogador()

def espacoVazio(board, posicao):  # verifica se a posicao escolhida pelo jogador no tabuleiro está vazia
    if board[posicao] == ' ':
        return True
    else:
        return False


def encontraJogadorIA():
    for jogador in Jogador.jogadores:
        if jogador.nome == "computador":
            return jogador


def encontraJogadorHumano():
    for jogador in Jogador.jogadores:
        if jogador.nome == "humano":
            return jogador


def jogarNovamente():
    print("")
    opcao = int(input("Deseja jogar novamente? S/n"))

    if opcao == "S" or opcao == "s":
        print()
        main()
    else:
        exit()


def inserirLetra(board, letra, posicao):  # inserir valor da jogada no tabuleiro
    delay()

    if espacoVazio(board, posicao):
        board[posicao] = letra
        print()
        exibirBoard(board)

        if verificaEmpate(board):
            print("Empate")
            jogarNovamente()
        elif vitoria(board):
            if letra == encontraJogadorIA().letra:
                print("Computador venceu!")
            elif letra == encontraJogadorIA().letra:
                print("Você ganhou!")
            jogarNovamente()
        return
    else:
        print("A posição escolhida já está ocupada!")
        delay()
        posicao = int(input("Escolha uma nova posição: "))
        inserirLetra(board, letra, posicao)
        return


def movimentoHumano(board, humano):
    posicao = int(input('Digite a posição na qual deseja jogar ' + humano.letra + ': '))
    inserirLetra(board, humano.letra, posicao)
    return

def movimentoIA(board, ia):
    melhor_pontuacao = -800
    melhor_movimento = 0

    for key in board.keys():
        if board[key] == ' ':
            board[key] = ia.letter
            pontuacao = minimax(board, 0, False)
            board[key] = ' '
            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                melhor_movimento = key
    print('Jogada do computador:', melhor_movimento)
    inserirLetra(board, ia.letter, melhor_movimento)
    return

def verificaEmpate(board):
    for chave in board.chaves():
        if board[chave] == " ":
            return False
    return True


def checarLinhaVencedora(board, letra=None):
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


def checarColunaVencedora(board, letra=None):
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


def checarDiagonalVencedora(board, letra=None):
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
    if checarLinhaVencedora(board):
        return True
    elif checarColunaVencedora(board):
        return True
    elif checarDiagonalVencedora(board):
        return True
    else:
        return False


def direcaoVencedora(board, jogador):
    if checarLinhaVencedora(board, jogador):
        return True
    elif checarColunaVencedora(board, jogador):
        return True
    elif checarDiagonalVencedora(board, jogador):
        return True
    else:
        return False


def minimax(board, profundidade, valor_maximo):
    ia = encontraJogadorIA()
    humano = encontraJogadorHumano()

    if direcaoVencedora(board, ia.letter):
        return 1
    elif direcaoVencedora(board, humano.letter):
        return -1
    elif verificaEmpate(board):
        return 0

    if valor_maximo:
        melhor_pontuacao = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = ia.letter
                pontuacao = minimax(board, profundidade + 1, False)  # proximo movimento deve minimizar
                board[key] = ' '
                if pontuacao > melhor_pontuacao:
                    melhor_pontuacao = pontuacao
        return melhor_pontuacao

    else:
        melhor_pontuacao = 800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = humano.letter
                pontuacao = minimax(board, profundidade + 1, True)  # proximo movimento deve maximizar
                board[key] = ' '
                if pontuacao < melhor_pontuacao:
                    melhor_pontuacao = pontuacao
        return melhor_pontuacao


def main():
    board = criarBoard()

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

    humano_primeiro = definirPrimeiroJogador()
    print('')

    if humano_primeiro:
        humano, computador = criarJogadores(1)
        exibirBoard(board)

        while not vitoria(board):
            delay()
            movimentoHumano(board, humano)
            delay()
            movimentoIA()
    else:
        humano, computador = criarJogadores(0)
        while not vitoria(board):
            delay()
            movimentoIA()
            delay()
            movimentoHumano()

    if __name__ == '__main__':
        main()
