import os
import random
import time

# Função para limpar a tela (compatível com Linux e Windows)
def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

# Função para mostrar o tabuleiro com uma interface estilizada
def mostrar_tabuleiro(tabuleiro):
    limpar_tela()
    print("\n  JOGO DA VELHA - Contra IA")
    print("┌───┬───┬───┐")
    for i in range(3):
        print(f"│ {tabuleiro[i][0]} │ {tabuleiro[i][1]} │ {tabuleiro[i][2]} │")
        if i < 2:
            print("├───┼───┼───┤")
    print("└───┴───┴───┘")

# Verifica se há vitória ou empate
def verificar_vitoria(tabuleiro, jogador):
    return (
        any(all(cell == jogador for cell in row) for row in tabuleiro) or
        any(all(row[i] == jogador for row in tabuleiro) for i in range(3)) or
        all(tabuleiro[i][i] == jogador for i in range(3)) or
        all(tabuleiro[i][2 - i] == jogador for i in range(3))
    )

# Verifica se o tabuleiro está cheio (empate)
def verificar_empate(tabuleiro):
    return all(cell in ('X', 'O') for row in tabuleiro for cell in row)

# IA com algoritmo de minimax básico
def melhor_movimento(tabuleiro):
    for jogador in ['O', 'X']:
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] not in ('X', 'O'):
                    tabuleiro[i][j] = jogador
                    if verificar_vitoria(tabuleiro, jogador):
                        return i, j
                    tabuleiro[i][j] = str(i * 3 + j + 1)

    movimentos_disponiveis = [(i, j) for i in range(3) for j in range(3) if tabuleiro[i][j] not in ('X', 'O')]
    return random.choice(movimentos_disponiveis)

# Função principal do jogo
def jogar():
    tabuleiro = [[str(i * 3 + j + 1) for j in range(3)] for i in range(3)]
    jogador = 'X'
    ia = 'O'

    mostrar_tabuleiro(tabuleiro)

    while True:
        # Jogador faz o movimento
        try:
            movimento = int(input("Escolha uma posição (1-9): ")) - 1
            linha, coluna = movimento // 3, movimento % 3
            if tabuleiro[linha][coluna] in ('X', 'O'):
                print("Posição já ocupada! Tente novamente.")
                time.sleep(1)
                continue
        except (ValueError, IndexError):
            print("Entrada inválida! Escolha um número entre 1 e 9.")
            time.sleep(1)
            continue

        tabuleiro[linha][coluna] = jogador
        mostrar_tabuleiro(tabuleiro)

        # Verifica se o jogador venceu
        if verificar_vitoria(tabuleiro, jogador):
            print("Parabéns! Você venceu!")
            break

        # Verifica empate
        if verificar_empate(tabuleiro):
            print("Empate!")
            break

        # Movimento da IA
        print("IA está pensando...")
        time.sleep(1)
        linha, coluna = melhor_movimento(tabuleiro)
        tabuleiro[linha][coluna] = ia
        mostrar_tabuleiro(tabuleiro)

        # Verifica se a IA venceu
        if verificar_vitoria(tabuleiro, ia):
            print("A IA venceu! Boa sorte na próxima!")
            break

        # Verifica empate
        if verificar_empate(tabuleiro):
            print("Empate!")
            break

# Inicia o jogo
if __name__ == "__main__":
    jogar()
