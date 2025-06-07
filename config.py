import pygame

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