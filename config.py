import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Dimensões da tela
LARGURA_TELA = 800
ALTURA_TELA = 600
TAMANHO_CELULA = 20  # Tamanho de cada "quadradinho" no mapa

# Cores
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
LARANJA = (255, 165, 0)
ROSA = (255, 192, 203)
CIANO = (0, 255, 255)

# Configuração da tela
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Pac-Man em Pygame")

# Clock para controlar a taxa de quadros
clock = pygame.time.Clock()
FPS = 30

# Carrega as imagens dos sprites
try:
    SPRITE_PACMAN_DIREITA = pygame.image.load('assets/pacman_right.png').convert_alpha()
    SPRITE_PACMAN_ESQUERDA = pygame.image.load('assets/pacman_left.png').convert_alpha()
    SPRITE_PACMAN_CIMA = pygame.image.load('assets/pacman_up.png').convert_alpha()
    SPRITE_PACMAN_BAIXO = pygame.image.load('assets/pacman_down.png').convert_alpha()
    SPRITE_FANTASMA_VERMELHO = pygame.image.load('assets/ghost_red.png').convert_alpha()
    SPRITE_FANTASMA_LARANJA = pygame.image.load('assets/ghost_orange.png').convert_alpha()
    SPRITE_FANTASMA_ROSA = pygame.image.load('assets/ghost_pink.png').convert_alpha()
    SPRITE_FANTASMA_CIANO = pygame.image.load('assets/ghost_cyan.png').convert_alpha()
except pygame.error as e:
    print(f"Erro ao carregar sprite: {e}")
    print("Certifique-se de que as imagens estão na pasta 'assets'.")
    sys.exit()

# Redimensionar os sprites para o TAMANHO_CELULA
SPRITE_PACMAN_DIREITA = pygame.transform.scale(SPRITE_PACMAN_DIREITA, (TAMANHO_CELULA, TAMANHO_CELULA))
SPRITE_PACMAN_ESQUERDA = pygame.transform.scale(SPRITE_PACMAN_ESQUERDA, (TAMANHO_CELULA, TAMANHO_CELULA))
SPRITE_PACMAN_CIMA = pygame.transform.scale(SPRITE_PACMAN_CIMA, (TAMANHO_CELULA, TAMANHO_CELULA))
SPRITE_PACMAN_BAIXO = pygame.transform.scale(SPRITE_PACMAN_BAIXO, (TAMANHO_CELULA, TAMANHO_CELULA))
SPRITE_FANTASMA_VERMELHO = pygame.transform.scale(SPRITE_FANTASMA_VERMELHO, (TAMANHO_CELULA, TAMANHO_CELULA))
SPRITE_FANTASMA_LARANJA = pygame.transform.scale(SPRITE_FANTASMA_LARANJA, (TAMANHO_CELULA, TAMANHO_CELULA))
SPRITE_FANTASMA_ROSA = pygame.transform.scale(SPRITE_FANTASMA_ROSA, (TAMANHO_CELULA, TAMANHO_CELULA))
SPRITE_FANTASMA_CIANO = pygame.transform.scale(SPRITE_FANTASMA_CIANO, (TAMANHO_CELULA, TAMANHO_CELULA))

# Mapear cores dos fantasmas para seus sprites
SPRITES_FANTASMAS = {
    VERMELHO: SPRITE_FANTASMA_VERMELHO,
    LARANJA: SPRITE_FANTASMA_LARANJA,
    ROSA: SPRITE_FANTASMA_ROSA,
    CIANO: SPRITE_FANTASMA_CIANO,
}
