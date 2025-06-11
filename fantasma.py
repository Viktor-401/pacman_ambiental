from config import *
from map import NUM_LINHAS, NUM_COLUNAS
import math
import random

DISTANCIA_MINIMA = TAMANHO_CELULA * 2  # distância mínima entre fantasmas

class Fantasma:
    def __init__(self, x, y, cor):
        self.x = x
        self.y = y
        self.cor = cor
        self.velocidade = 3
        self.direcao_x = 0
        self.direcao_y = 0
        self.sprite_atual = SPRITES_FANTASMAS[cor]

    def mover(self, mapa, pacman, outros_fantasmas):
        # Primeiro, calcula vetor para fugir de fantasmas próximos
        afastar_x, afastar_y = 0, 0
        for f in outros_fantasmas:
            if f is self:
                continue
            dist = math.hypot(self.x - f.x, self.y - f.y)
            if dist < DISTANCIA_MINIMA and dist > 0:
                # vetor de afastamento (normalizado e inverso da direção)
                afastar_x += (self.x - f.x) / dist
                afastar_y += (self.y - f.y) / dist
        
        # Se está perto de algum fantasma, tenta se afastar
        if afastar_x != 0 or afastar_y != 0:
            norm = math.hypot(afastar_x, afastar_y)
            afastar_x /= norm
            afastar_y /= norm

            tentativa_x = self.x + afastar_x * self.velocidade
            tentativa_y = self.y + afastar_y * self.velocidade

            if not self.colisao_parede(tentativa_x, tentativa_y, mapa):
                self.x = tentativa_x
                self.y = tentativa_y
                self.direcao_x = afastar_x
                self.direcao_y = afastar_y
                return

        # Se não precisa fugir, move normalmente em direção ao Pac-Man
        dx = pacman.x - self.x
        dy = pacman.y - self.y

        # Prioriza X
        if dx > 0:
            tentativa_x = self.x + self.velocidade
            celula_alvo_x = int(tentativa_x / TAMANHO_CELULA)
            celula_fantasma_y = int(self.y / TAMANHO_CELULA)
            if 0 <= celula_alvo_x < NUM_COLUNAS and mapa[celula_fantasma_y][celula_alvo_x] != 1:
                self.x = tentativa_x
                self.direcao_x = 1
                self.direcao_y = 0
                return
        elif dx < 0:
            tentativa_x = self.x - self.velocidade
            celula_alvo_x = int(tentativa_x / TAMANHO_CELULA)
            celula_fantasma_y = int(self.y / TAMANHO_CELULA)
            if 0 <= celula_alvo_x < NUM_COLUNAS and mapa[celula_fantasma_y][celula_alvo_x] != 1:
                self.x = tentativa_x
                self.direcao_x = -1
                self.direcao_y = 0
                return

        # Depois Y
        if dy > 0:
            tentativa_y = self.y + self.velocidade
            celula_alvo_y = int(tentativa_y / TAMANHO_CELULA)
            celula_fantasma_x = int(self.x / TAMANHO_CELULA)
            if 0 <= celula_alvo_y < NUM_LINHAS and mapa[celula_alvo_y][celula_fantasma_x] != 1:
                self.y = tentativa_y
                self.direcao_y = 1
                self.direcao_x = 0
                return
        elif dy < 0:
            tentativa_y = self.y - self.velocidade
            celula_alvo_y = int(tentativa_y / TAMANHO_CELULA)
            celula_fantasma_x = int(self.x / TAMANHO_CELULA)
            if 0 <= celula_alvo_y < NUM_LINHAS and mapa[celula_alvo_y][celula_fantasma_x] != 1:
                self.y = tentativa_y
                self.direcao_y = -1
                self.direcao_x = 0
                return

        # Se não conseguiu andar em X nem Y, tenta movimentos aleatórios
        self.tenta_mover_aleatoriamente(mapa)

    def colisao_parede(self, x, y, mapa):
        cel_x = int(x / TAMANHO_CELULA)
        cel_y = int(y / TAMANHO_CELULA)
        if cel_y < 0 or cel_y >= NUM_LINHAS or cel_x < 0 or cel_x >= NUM_COLUNAS:
            return True
        return mapa[cel_y][cel_x] == 1

    def tenta_mover_aleatoriamente(self, mapa):
        possiveis_movimentos = [(0,1),(0,-1),(1,0),(-1,0)]
        random.shuffle(possiveis_movimentos)
        for d_x, d_y in possiveis_movimentos:
            proximo_x = self.x + d_x * self.velocidade
            proximo_y = self.y + d_y * self.velocidade
            if not self.colisao_parede(proximo_x, proximo_y, mapa):
                self.x = proximo_x
                self.y = proximo_y
                self.direcao_x = d_x
                self.direcao_y = d_y
                return
        self.direcao_x = 0
        self.direcao_y = 0

    def desenhar(self, tela):
        tela.blit(self.sprite_atual, (self.x, self.y))
