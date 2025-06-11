import pygame
from config import TAMANHO_CELULA, AMARELO, SPRITE_PACMAN_DIREITA, SPRITE_PACMAN_ESQUERDA, SPRITE_PACMAN_CIMA, SPRITE_PACMAN_BAIXO
from map import NUM_LINHAS, NUM_COLUNAS

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 2
        self.direcao_x = 0
        self.direcao_y = 0
        self.vidas = 3
        self.pontuacao = 0
        self.invencivel = False
        self.tempo_invencivel = 0  # tempo restante da invencibilidade em ms
        self.sprite_atual = SPRITE_PACMAN_DIREITA

    def mover(self, mapa):
        # Calcula a nova posição pretendida
        nova_x = self.x + self.direcao_x * self.velocidade
        nova_y = self.y + self.direcao_y * self.velocidade

        # Dimensões do Pacman (assume quadrado do tamanho da célula)
        tamanho = 14

        # Calcula os quatro cantos após o movimento
        cantos = [
            (nova_x, nova_y),  # canto superior esquerdo
            (nova_x + tamanho - 1, nova_y),  # canto superior direito
            (nova_x, nova_y + tamanho - 1),  # canto inferior esquerdo
            (nova_x + tamanho - 1, nova_y + tamanho - 1)  # canto inferior direito
        ]

        pode_mover = True
        for cx, cy in cantos:
            celula_x = int(cx / TAMANHO_CELULA)
            celula_y = int(cy / TAMANHO_CELULA)
            if not (0 <= celula_x < NUM_COLUNAS and 0 <= celula_y < NUM_LINHAS):
                pode_mover = False
                break
            if mapa[celula_y][celula_x] == 1:
                pode_mover = False
                break

        if pode_mover:
            self.x = nova_x
            self.y = nova_y

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