import time
import main

class Jogador:
    jogadores = []
    def __int__(self, nome="", letra=""):


def criarBoard():
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


def verificaEspaço(board):
    for chave in board.chaves():
        if board[chave] == " ":
            return False

    return True


def jogarNovamente():
    print("")
    opcao = int(input("Deseja Jogar novamente? S/n"))

    if opcao == "S" or opcao == "s":
        print()
        main
    else:
        exit()


def inserirLetra(board, letra, posicao): # inserir valor da jogada no tabuleiro
    delay()

    if espacoVazio(board, posicao):
        board[posicao] = letra
        print()
        exibirBoard(board)

        if verificaEspaço(board):
            print("Empate")
            jogarNovamente()



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


def criarJogadores(valor):
    humano = Jogador("humano", "X")
    computador = Jogador("computador", "O")

    if valor == 0:
        humano.letra = "O"
        computador.letra = "X"

    return humano, computador















def movimentoHumano(board, humano):
    posicao = int(input("Digite a sua posição para jogar" + humano.letra + ": "))


def movimentoIA():
    pass


def espacoVazio(board, posicao):  # verifica se a posicao escolhida pelo jogador no tabuleiro está vazia
    if board[posicao] == ' ':
        return True
    else:
        return False


def getInputInvalido(board, mensagem):
    try:
        number = int(input(mensagem))
        espacoVazio(board, number)

        print("Sucesso", number)
    except:
        print("Número inválido!")
        getInputInvalido(mensagem)


def verificaMovimento():
    pass


def fazMovimento():
    pass


def verificaGanhador(tabuleiro):
    return


def delay():
    time.sleep(0.5)
