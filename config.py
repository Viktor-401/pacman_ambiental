import pygame
import sys, os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        nase_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Inicialização do Pygame
pygame.init()

# Dimensões da tela
LARGURA_TELA = 1080
ALTURA_TELA = 720
TAMANHO_CELULA = 20  # Tamanho de cada "quadradinho" no mapa

# Cores
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERDE_ESCURO = (0, 120, 0)
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
    SPRITE_PACMAN_DIREITA = pygame.image.load(resource_path('assets/heroi.png')).convert_alpha()
    SPRITE_PACMAN_ESQUERDA = pygame.image.load(resource_path('assets/heroi.png')).convert_alpha()
    SPRITE_PACMAN_CIMA = pygame.image.load(resource_path('assets/heroi.png')).convert_alpha()
    SPRITE_PACMAN_BAIXO = pygame.image.load(resource_path('assets/heroi.png')).convert_alpha()
    SPRITE_FANTASMA_VERMELHO = pygame.image.load(resource_path('assets/capitalismo.png')).convert_alpha()
    SPRITE_FANTASMA_LARANJA = pygame.image.load(resource_path('assets/fabrica.png')).convert_alpha()
    SPRITE_FANTASMA_ROSA = pygame.image.load(resource_path('assets/desmatamento.png')).convert_alpha()
    SPRITE_FANTASMA_CIANO = pygame.image.load(resource_path('assets/queimada.png')).convert_alpha()
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
