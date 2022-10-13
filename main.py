from tic_tac_toe import *

board = criarBoard()
jogador = 0
ganhador = verificaGanhador(board)

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

humanoPrimeiro = definirPrimeiroJogador()
print('')


if humanoPrimeiro:
    humano, computador = criarJogadores(1)
    exibirBoard(board)

    while not ganhador(board):
        delay()
        movimentoHumano(board, humano)
        delay()
        movimentoIA()
else:
    humano, computador = criarJogadores(0)
    while not ganhador(board):
        delay()
        movimentoIA()
        delay()
        movimentoHumano()
