import pygame
import sys
from config import *
from map import *
from pacman import Pacman
from fantasma import Fantasma

def desenhar_mapa(tela, mapa):
    for linha_idx, linha in enumerate(mapa):
        for col_idx, celula in enumerate(linha):
            x = col_idx * TAMANHO_CELULA
            y = linha_idx * TAMANHO_CELULA
            if celula == 1: # Parede
                pygame.draw.rect(tela, AZUL, (x, y, TAMANHO_CELULA, TAMANHO_CELULA))
            elif celula == 2: # Bolinha de comida
                pygame.draw.circle(tela, BRANCO, (x + TAMANHO_CELULA // 2, y + TAMANHO_CELULA // 2), TAMANHO_CELULA // 4)
            elif celula == 3: # Bolinha de poder (maior)
                pygame.draw.circle(tela, BRANCO, (x + TAMANHO_CELULA // 2, y + TAMANHO_CELULA // 2), TAMANHO_CELULA // 3)

def verificar_colisoes(pacman, fantasmas, mapa):
    # Colisão Pac-Man com comida
    celula_pacman_x = int(pacman.x / TAMANHO_CELULA)
    celula_pacman_y = int(pacman.y / TAMANHO_CELULA)

    if 0 <= celula_pacman_y < NUM_LINHAS and 0 <= celula_pacman_x < NUM_COLUNAS:
        if mapa[celula_pacman_y][celula_pacman_x] == 2:
            pacman.pontuacao += 10
            mapa[celula_pacman_y][celula_pacman_x] = 0 # Remove a bolinha
        elif mapa[celula_pacman_y][celula_pacman_x] == 3:
            pacman.pontuacao += 50
            # Ativa o modo "Power-Up" (fantasmas ficam azuis, Pac-Man pode comê-los)
            # Isso exigiria mais lógica: timer para o power-up, mudança de estado dos fantasmas.
            mapa[celula_pacman_y][celula_pacman_x] = 0

    # Colisão Pac-Man com fantasma (simplificado: se as caixas de colisão se sobrepõem)
    for fantasma in fantasmas:
        # Usar pygame.Rect para detecção de colisão mais precisa
        rect_pacman = pygame.Rect(pacman.x, pacman.y, TAMANHO_CELULA, TAMANHO_CELULA)
        rect_fantasma = pygame.Rect(fantasma.x, fantasma.y, TAMANHO_CELULA, TAMANHO_CELULA)

        if rect_pacman.colliderect(rect_fantasma):
            if True: # Aqui você verificaria se o Pac-Man está no modo "Power-Up"
                # Se Pac-Man estiver comendo fantasmas, o fantasma volta para a base
                fantasma.x = 10 * TAMANHO_CELULA # Volta para a posição inicial (ou uma "casa" para fantasmas)
                fantasma.y = 7 * TAMANHO_CELULA
                pacman.pontuacao += 200
            else:
                # Se não estiver em power-up, Pac-Man perde uma vida
                pacman.vidas -= 1
                # Resetar posições
                pacman.x = 1 * TAMANHO_CELULA
                pacman.y = 1 * TAMANHO_CELULA
                for f in fantasmas: # Resetar fantasmas também
                    f.x = 10 * TAMANHO_CELULA
                    f.y = 7 * TAMANHO_CELULA

def mostrar_texto(tela, texto, cor, x, y, tamanho_fonte=30):
    fonte = pygame.font.Font(None, tamanho_fonte)
    superficie_texto = fonte.render(texto, True, cor)
    tela.blit(superficie_texto, (x, y))

def dialogo_educacao_ambiental(tela):
    dialogo_texto = [
        "Bem-vindo ao Eco-Pac! Neste jogo, vamos combater os fantasmas da poluição.",
        "Cada bolinha que você come representa uma ação sustentável.",
        "Juntos, podemos cuidar do nosso planeta!",
        "Pressione ESPAÇO para começar!"
    ]
    
    tela.fill(PRETO)
    y_offset = ALTURA_TELA // 3
    for linha in dialogo_texto:
        mostrar_texto(tela, linha, BRANCO, LARGURA_TELA // 2 - len(linha) * 5, y_offset, 25)
        y_offset += 40
    pygame.display.flip()

    esperando_inicio = True
    while esperando_inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    esperando_inicio = False

def menu_start(tela):
    menu_opcoes = ["Iniciar Jogo", "Sair"]
    opcao_selecionada = 0

    while True:
        tela.fill(PRETO)
        mostrar_texto(tela, "PAC-MAN AMBIENTAL", AMARELO, LARGURA_TELA // 2 - 180, ALTURA_TELA // 4, 60)

        y_offset = ALTURA_TELA // 2
        for i, opcao in enumerate(menu_opcoes):
            cor_texto = BRANCO
            if i == opcao_selecionada:
                cor_texto = AMARELO # Destaca a opção selecionada
            mostrar_texto(tela, opcao, cor_texto, LARGURA_TELA // 2 - 70, y_offset, 40)
            y_offset += 60

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Sair"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    opcao_selecionada = (opcao_selecionada - 1) % len(menu_opcoes)
                elif event.key == pygame.K_DOWN:
                    opcao_selecionada = (opcao_selecionada + 1) % len(menu_opcoes)
                elif event.key == pygame.K_RETURN: # Tecla Enter
                    if opcao_selecionada == 0:
                        return "Iniciar Jogo"
                    elif opcao_selecionada == 1:
                        return "Sair"

# Inicialização de Pac-Man e Fantasmas
pacman = Pacman(1 * TAMANHO_CELULA, 1 * TAMANHO_CELULA) # Inicia Pac-Man na primeira célula do caminho

fantasmas = [
    Fantasma(10 * TAMANHO_CELULA, 7 * TAMANHO_CELULA, VERMELHO),
    Fantasma(11 * TAMANHO_CELULA, 7 * TAMANHO_CELULA, LARANJA),
    Fantasma(12 * TAMANHO_CELULA, 7 * TAMANHO_CELULA, ROSA),
    Fantasma(13 * TAMANHO_CELULA, 7 * TAMANHO_CELULA, CIANO),
]


# Chama o menu de start
escolha = menu_start(tela)

# Chama o diálogo ambiental
dialogo_educacao_ambiental(tela)

if escolha == "Sair":
    pygame.quit()
    sys.exit()

# Loop principal do jogo
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacman.direcao_x = -1
                pacman.direcao_y = 0
            elif event.key == pygame.K_RIGHT:
                pacman.direcao_x = 1
                pacman.direcao_y = 0
            elif event.key == pygame.K_UP:
                pacman.direcao_x = 0
                pacman.direcao_y = -1
            elif event.key == pygame.K_DOWN:
                pacman.direcao_x = 0
                pacman.direcao_y = 1
            elif event.key == pygame.K_ESCAPE:
                rodando = False

    # Atualizar estado do jogo
    pacman.mover(MAPA)
    for fantasma in fantasmas:
        fantasma.mover(MAPA, pacman) # Passa o Pac-Man para o fantasma poder persegui-lo
    verificar_colisoes(pacman, fantasmas, MAPA)

    # Desenhar
    tela.fill(PRETO) # Limpa a tela
    desenhar_mapa(tela, MAPA)
    pacman.desenhar(tela)
    for fantasma in fantasmas:
        fantasma.desenhar(tela)

    mostrar_texto(tela, f"Pontuação: {pacman.pontuacao}", BRANCO, 10, ALTURA_TELA - 40)
    mostrar_texto(tela, f"Vidas: {pacman.vidas}", BRANCO, LARGURA_TELA - 100, ALTURA_TELA - 40)

    # Lógica de fim de jogo
    if pacman.vidas <= 0:
        mostrar_texto(tela, "GAME OVER!", VERMELHO, LARGURA_TELA // 2 - 100, ALTURA_TELA // 2 - 30, 50)
        pygame.display.flip()
        pygame.time.wait(3000) # Espera 3 segundos
        rodando = False

    pygame.display.flip() # Atualiza a tela
    clock.tick(FPS) # Controla a taxa de quadros

pygame.quit()
sys.exit()