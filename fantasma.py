from config import *
from map import NUM_LINHAS, NUM_COLUNAS

class Fantasma:
    def __init__(self, x, y, cor):
        self.x = x
        self.y = y
        self.cor = cor
        self.velocidade = 3
        self.direcao_x = 0
        self.direcao_y = 0
        self.sprite_atual = SPRITES_FANTASMAS[cor] # Pega o sprite pela cor

    def mover(self, mapa, pacman):
        dx = pacman.x - self.x
        dy = pacman.y - self.y

        # Tenta mover na direção X primeiro
        if dx > 0: # Pac-Man está à direita
            tentativa_x = self.x + self.velocidade
            celula_alvo_x = int(tentativa_x / TAMANHO_CELULA)
            celula_fantasma_y = int(self.y / TAMANHO_CELULA)
            if 0 <= celula_alvo_x < NUM_COLUNAS and mapa[celula_fantasma_y][celula_alvo_x] != 1:
                self.x = tentativa_x
                self.direcao_x = 1
                self.direcao_y = 0 # Prioriza o movimento horizontal se possível
                return
        elif dx < 0: # Pac-Man está à esquerda
            tentativa_x = self.x - self.velocidade
            celula_alvo_x = int(tentativa_x / TAMANHO_CELULA)
            celula_fantasma_y = int(self.y / TAMANHO_CELULA)
            if 0 <= celula_alvo_x < NUM_COLUNAS and mapa[celula_fantasma_y][celula_alvo_x] != 1:
                self.x = tentativa_x
                self.direcao_x = -1
                self.direcao_y = 0
                return
        
        # Se não conseguiu mover em X, tenta em Y
        if dy > 0: # Pac-Man está para baixo
            tentativa_y = self.y + self.velocidade
            celula_alvo_y = int(tentativa_y / TAMANHO_CELULA)
            celula_fantasma_x = int(self.x / TAMANHO_CELULA)
            if 0 <= celula_alvo_y < NUM_LINHAS and mapa[celula_alvo_y][celula_fantasma_x] != 1:
                self.y = tentativa_y
                self.direcao_y = 1
                self.direcao_x = 0 # Prioriza o movimento vertical
                return
        elif dy < 0: # Pac-Man está para cima
            tentativa_y = self.y - self.velocidade
            celula_alvo_y = int(tentativa_y / TAMANHO_CELULA)
            celula_fantasma_x = int(self.x / TAMANHO_CELULA)
            if 0 <= celula_alvo_y < NUM_LINHAS and mapa[celula_alvo_y][celula_fantasma_x] != 1:
                self.y = tentativa_y
                self.direcao_y = -1
                self.direcao_x = 0
                return

        # Se não conseguiu mover em X nem Y (preso), pode tentar uma direção aleatória
        # ou apenas parar por um momento. Por simplicidade, vamos tentar mover para qualquer direção válida.
        # Isso ainda não evita completamente que ele fique preso, mas é um ponto de partida.
        self.tenta_mover_aleatoriamente(mapa)

    def tenta_mover_aleatoriamente(self, mapa):
        import random
        possiveis_movimentos = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Cima, Baixo, Direita, Esquerda
        random.shuffle(possiveis_movimentos)

        for d_x, d_y in possiveis_movimentos:
            proximo_x = self.x + d_x * self.velocidade
            proximo_y = self.y + d_y * self.velocidade
            
            proxima_celula_x = int(proximo_x / TAMANHO_CELULA)
            proxima_celula_y = int(proximo_y / TAMANHO_CELULA)

            if 0 <= proxima_celula_x < NUM_COLUNAS and \
               0 <= proxima_celula_y < NUM_LINHAS and \
               mapa[proxima_celula_y][proxima_celula_x] != 1: # Se não for parede
                self.x = proximo_x
                self.y = proximo_y
                self.direcao_x = d_x
                self.direcao_y = d_y
                return # Movimento feito

        # Se nenhuma direção aleatória for possível, o fantasma fica parado
        self.direcao_x = 0
        self.direcao_y = 0


    def desenhar(self, tela):
        tela.blit(self.sprite_atual, (self.x, self.y))
