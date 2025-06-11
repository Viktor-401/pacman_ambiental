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
        self.velocidade = 1
        self.direcao_x = 0
        self.direcao_y = 0
        self.sprite_atual = SPRITES_FANTASMAS[cor]

    def mover(self, mapa, pacman, outros_fantasmas):
        dx = pacman.x - self.x
        dy = pacman.y - self.y
        # # Evita aproximação excessiva de outros fantasmas
        # for outro in outros_fantasmas:
        #     if outro is self:
        #         continue
        #     distancia = math.hypot(self.x - outro.x, self.y - outro.y)
        #     if distancia < DISTANCIA_MINIMA:
        #         # Move-se na direção oposta ao outro fantasma
        #         afastar_x = self.x - outro.x
        #         afastar_y = self.y - outro.y
        #         norm = math.hypot(afastar_x, afastar_y)
        #         if norm != 0:
        #             afastar_x /= norm
        #             afastar_y /= norm
        #             tentativa_x = self.x + afastar_x * self.velocidade
        #             tentativa_y = self.y + afastar_y * self.velocidade
        #             if not self.colisao_parede(tentativa_x, tentativa_y, mapa):
        #                 self.x = tentativa_x
        #                 self.y = tentativa_y
        #                 self.direcao_x = int(round(afastar_x))
        #                 self.direcao_y = int(round(afastar_y))
        #                 return
        # Decide qual eixo priorizar baseado na distância absoluta
        if abs(dx) > abs(dy):
            # Tenta mover no eixo X primeiro
            if dx > 0:
                tentativa_x = self.x + self.velocidade
                if not self.colisao_parede(tentativa_x, self.y, mapa):
                    self.x = tentativa_x
                    self.direcao_x = 1
                    self.direcao_y = 0
                    return
            elif dx < 0:
                tentativa_x = self.x - self.velocidade
                if not self.colisao_parede(tentativa_x, self.y, mapa):
                    self.x = tentativa_x
                    self.direcao_x = -1
                    self.direcao_y = 0
                    return
            # Se não conseguiu mover em X, tenta Y
            if dy > 0:
                tentativa_y = self.y + self.velocidade
                if not self.colisao_parede(self.x, tentativa_y, mapa):
                    self.y = tentativa_y
                    self.direcao_y = 1
                    self.direcao_x = 0
                    return
            elif dy < 0:
                tentativa_y = self.y - self.velocidade
                if not self.colisao_parede(self.x, tentativa_y, mapa):
                    self.y = tentativa_y
                    self.direcao_y = -1
                    self.direcao_x = 0
                    return
        else:
            # Tenta mover no eixo Y primeiro
            if dy > 0:
                tentativa_y = self.y + self.velocidade
                if not self.colisao_parede(self.x, tentativa_y, mapa):
                    self.y = tentativa_y
                    self.direcao_y = 1
                    self.direcao_x = 0
                    return
            elif dy < 0:
                tentativa_y = self.y - self.velocidade
                if not self.colisao_parede(self.x, tentativa_y, mapa):
                    self.y = tentativa_y
                    self.direcao_y = -1
                    self.direcao_x = 0
                    return
            # Se não conseguiu mover em Y, tenta X
            if dx > 0:
                tentativa_x = self.x + self.velocidade
                if not self.colisao_parede(tentativa_x, self.y, mapa):
                    self.x = tentativa_x
                    self.direcao_x = 1
                    self.direcao_y = 0
                    return
            elif dx < 0:
                tentativa_x = self.x - self.velocidade
                if not self.colisao_parede(tentativa_x, self.y, mapa):
                    self.x = tentativa_x
                    self.direcao_x = -1
                    self.direcao_y = 0
                    return

        # Se não conseguiu andar em X nem Y, tenta movimentos aleatórios
        self.tenta_mover_aleatoriamente(mapa)

    def colisao_parede(self, x, y, mapa):
                # Dimensões do Pacman (assume quadrado do tamanho da célula)
        tamanho = TAMANHO_CELULA

        # Calcula os quatro cantos após o movimento
        cantos = [
            (x, y),  # canto superior esquerdo
            (x + tamanho - 1, y),  # canto superior direito
            (x, y + tamanho - 1),  # canto inferior esquerdo
            (x + tamanho - 1, y + tamanho - 1)  # canto inferior direito
        ]

        for cx, cy in cantos:
            celula_x = int(cx / TAMANHO_CELULA)
            celula_y = int(cy / TAMANHO_CELULA)
            if not (0 <= celula_x < NUM_COLUNAS and 0 <= celula_y < NUM_LINHAS):
                return True
            if mapa[celula_y][celula_x] == 1:
                return True
        return False

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
