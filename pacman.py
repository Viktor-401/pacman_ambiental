import pygame
from config import TAMANHO_CELULA, AMARELO
from map import NUM_LINHAS, NUM_COLUNAS

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direcao_x = 0
        self.direcao_y = 0
        self.velocidade = 5
        self.pontuacao = 0
        self.vidas = 3

    def mover(self, mapa):
        # Tenta mover na direção atual
        nova_x = self.x + self.direcao_x * self.velocidade
        nova_y = self.y + self.direcao_y * self.velocidade

        # Verifica colisão com paredes (simplificado para células)
        # Mais robusto seria verificar os 4 cantos do Pac-Man
        proxima_celula_x = int(nova_x / TAMANHO_CELULA)
        proxima_celula_y = int(nova_y / TAMANHO_CELULA)

        # Garante que não saia dos limites do mapa
        if 0 <= proxima_celula_y < NUM_LINHAS and 0 <= proxima_celula_x < NUM_COLUNAS:
            if mapa[proxima_celula_y][proxima_celula_x] != 1:  # Se não for parede
                self.x = nova_x
                self.y = nova_y
            else:
                # Se colidir com parede, para de mover nessa direção
                self.direcao_x = 0
                self.direcao_y = 0

    def desenhar(self, tela):
        pygame.draw.circle(tela, AMARELO, (int(self.x + TAMANHO_CELULA / 2), int(self.y + TAMANHO_CELULA / 2)), TAMANHO_CELULA // 2 - 2)