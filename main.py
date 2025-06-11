import sys, io, os
buffer = io.StringIO()
sys.stdout = sys.stderr = buffer

import pygame
from config import *
from map import *
from pacman import Pacman
from fantasma import Fantasma

def desenhar_mapa(tela, mapa):
    for linha_idx, linha in enumerate(mapa):
        for col_idx, celula in enumerate(linha):
            x = col_idx * TAMANHO_CELULA
            y = linha_idx * TAMANHO_CELULA
            if celula == 1:  # Parede
                pygame.draw.rect(tela, VERDE_ESCURO, (x, y, TAMANHO_CELULA, TAMANHO_CELULA))
            elif celula == 2:  # Bolinha de comida
                pygame.draw.rect(tela, LARANJA, (x, y, TAMANHO_CELULA, TAMANHO_CELULA))
                pygame.draw.circle(tela, BRANCO, (x + TAMANHO_CELULA // 2, y + TAMANHO_CELULA // 2), TAMANHO_CELULA // 4)
            elif celula == 3:  # Bolinha de poder (maior)
                pygame.draw.circle(tela, BRANCO, (x + TAMANHO_CELULA // 2, y + TAMANHO_CELULA // 2), TAMANHO_CELULA // 3)
            elif celula == 0:  # Espaço vazio
                pygame.draw.rect(tela, LARANJA, (x, y, TAMANHO_CELULA, TAMANHO_CELULA))

def verificar_colisoes(pacman, fantasmas, mapa):
    # Colisão Pac-Man com comida
    celula_pacman_x = int(pacman.x / TAMANHO_CELULA)
    celula_pacman_y = int(pacman.y / TAMANHO_CELULA)

    if 0 <= celula_pacman_y < NUM_LINHAS and 0 <= celula_pacman_x < NUM_COLUNAS:
        if mapa[celula_pacman_y][celula_pacman_x] == 2:
            pacman.pontuacao += 10
            mapa[celula_pacman_y][celula_pacman_x] = 0  # Remove a bolinha
        elif mapa[celula_pacman_y][celula_pacman_x] == 3:
            pacman.pontuacao += 50
            mapa[celula_pacman_y][celula_pacman_x] = 0

    # Colisão Pac-Man com fantasma
    rect_pacman = pygame.Rect(pacman.x, pacman.y, TAMANHO_CELULA, TAMANHO_CELULA)
    for fantasma in fantasmas:
        rect_fantasma = pygame.Rect(fantasma.x, fantasma.y, TAMANHO_CELULA, TAMANHO_CELULA)
        if rect_pacman.colliderect(rect_fantasma):
            if not pacman.invencivel:
                pacman.vidas -= 1
                pacman.invencivel = True
                pacman.tempo_invencivel = 2000  # 2 segundos invencível
                # Resetar posições
                pacman.x = 1 * TAMANHO_CELULA
                pacman.y = 1 * TAMANHO_CELULA

def mostrar_texto(tela, texto, cor, x, y, tamanho_fonte=30):
    fonte = pygame.font.Font(None, tamanho_fonte)
    superficie_texto = fonte.render(texto, True, cor)
    tela.blit(superficie_texto, (x, y))

def dialogo_educacao_ambiental(tela):
    dialogo_texto = [
        "Bem-vindo ao Eco-Pac! Neste jogo, vamos combater os fantasmas da poluição:",
        "As industrias poluentes, o desmatamento e as queimadas, na busca pelo maior acumulo de capital.",
        "Cada bolinha que você come representa uma ação sustentável e menos poder para os fantasmas.",
        "Juntos, podemos cuidar do nosso planeta!",
        "Pressione Enter para começar!"
    ]

    tela.fill(VERDE_ESCURO)
    y_offset = ALTURA_TELA // 3
    for linha in dialogo_texto:
        mostrar_texto(tela, linha, BRANCO, LARGURA_TELA // 2 - len(linha) * 5, y_offset, 25)
        y_offset += 40

    imagens = [
        SPRITE_FANTASMA_VERMELHO,
        SPRITE_FANTASMA_LARANJA, SPRITE_FANTASMA_ROSA, SPRITE_FANTASMA_CIANO]
    
    imagem = pygame.transform.scale(SPRITE_PACMAN_BAIXO, (64, 64))
    tela.blit(imagem, (LARGURA_TELA // 2 - 250, ALTURA_TELA // 6))
    

    for i, sprite in enumerate(imagens):
        imagem = pygame.transform.scale(sprite, (64, 64))
        tela.blit(imagem, (LARGURA_TELA // 2 - 30 + (i * 70), ALTURA_TELA // 6))

    pygame.display.flip()

    esperando_inicio = True
    while esperando_inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    esperando_inicio = False

def menu_start(tela):
    menu_opcoes = ["Iniciar Jogo", "Sair"]
    opcao_selecionada = 0

    while True:
        tela.fill(VERDE_ESCURO)
        mostrar_texto(tela, "PAC-MAN AMBIENTAL", AMARELO, LARGURA_TELA // 2 - 180, ALTURA_TELA // 4, 60)

        y_offset = ALTURA_TELA // 2
        for i, opcao in enumerate(menu_opcoes):
            cor_texto = BRANCO
            if i == opcao_selecionada:
                cor_texto = AMARELO
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
                elif event.key == pygame.K_RETURN:
                    if opcao_selecionada == 0:
                        return "Iniciar Jogo"
                    elif opcao_selecionada == 1:
                        return "Sair"

# Inicialização do Pygame e da tela
pygame.init()
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Eco-Pac")
clock = pygame.time.Clock()

# Inicialização de Pac-Man e Fantasmas
pacman = Pacman(1 * TAMANHO_CELULA, 1 * TAMANHO_CELULA)

fantasmas = [
    Fantasma(10 * TAMANHO_CELULA, 7 * TAMANHO_CELULA, VERMELHO),
    Fantasma(1 * TAMANHO_CELULA, (NUM_LINHAS-2) * TAMANHO_CELULA, LARANJA),
    Fantasma((NUM_COLUNAS-2) * TAMANHO_CELULA, (NUM_LINHAS-2) * TAMANHO_CELULA, ROSA),
    Fantasma((NUM_LINHAS-2) * TAMANHO_CELULA, 1 * TAMANHO_CELULA, CIANO),
]

# Chama o menu de start
escolha = menu_start(tela)

# Chama o diálogo ambiental
dialogo_educacao_ambiental(tela)

if escolha == "Sair":
    pygame.quit()
    sys.exit()

rodando = True
while rodando:
    dt = clock.tick(FPS)  # tempo desde último frame (ms)

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

    pacman.mover(MAPA)
    for fantasma in fantasmas:
        fantasma.mover(MAPA, pacman, fantasmas)

    verificar_colisoes(pacman, fantasmas, MAPA)
    pacman.atualizar_invencibilidade(dt)

    # Desenhar tudo
    tela.fill(BRANCO)
    desenhar_mapa(tela, MAPA)
    pacman.desenhar(tela)
    for fantasma in fantasmas:
        fantasma.desenhar(tela)

    mostrar_texto(tela, f"Pontuação: {pacman.pontuacao}", PRETO, 10, ALTURA_TELA - 40)
    mostrar_texto(tela, f"Vidas: {pacman.vidas}", PRETO, LARGURA_TELA - 100, ALTURA_TELA - 40)

    if pacman.vidas <= 0:
        mostrar_texto(tela, "GAME OVER!", VERMELHO, LARGURA_TELA // 2 - 100, ALTURA_TELA // 2 - 30, 50)
        pygame.display.flip()
        pygame.time.wait(3000)
        rodando = False

    pygame.display.flip()

pygame.quit()
sys.exit()
