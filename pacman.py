import pygame
from config import TAMANHO_CELULA, AMARELO, SPRITE_PACMAN_DIREITA, SPRITE_PACMAN_ESQUERDA, SPRITE_PACMAN_CIMA, SPRITE_PACMAN_BAIXO
from map import NUM_LINHAS, NUM_COLUNAS

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 5
        self.direcao_x = 0
        self.direcao_y = 0
        self.vidas = 3
        self.pontuacao = 0
        self.invencivel = False
        self.tempo_invencivel = 0  # tempo restante da invencibilidade em ms
        self.sprite_atual = SPRITE_PACMAN_DIREITA

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

        if self.direcao_x == 1:
            self.sprite_atual = SPRITE_PACMAN_DIREITA
        elif self.direcao_x == -1:
            self.sprite_atual = SPRITE_PACMAN_ESQUERDA
        elif self.direcao_y == 1:
            self.sprite_atual = SPRITE_PACMAN_BAIXO
        elif self.direcao_y == -1:
            self.sprite_atual = SPRITE_PACMAN_CIMA


    def desenhar(self, tela):
        tela.blit(self.sprite_atual, (self.x, self.y))

    def atualizar_invencibilidade(self, dt):
        if self.invencivel:
            self.tempo_invencivel -= dt
            if self.tempo_invencivel <= 0:
                self.invencivel = False
                self.tempo_invencivel = 0