from config import *

class Fantasma:
    def __init__(self, x, y, cor):
        self.x = x
        self.y = y
        self.cor = cor
        self.velocidade = 3
        self.direcao_x = 0
        self.direcao_y = 0

    def mover(self, mapa, pacman):
        # IA simples: mover aleatoriamente ou em direção ao Pac-Man (mais complexo)
        # Por simplicidade, vamos fazer um movimento aleatório por enquanto
        # Em um jogo completo, você implementaria algoritmos de busca (BFS, A*)
        # para que os fantasmas persigam o Pac-Man de forma inteligente.

        # Exemplo de movimento aleatório básico (apenas para demonstração)
        # Você precisaria de lógica para não colidir com paredes e virar
        # self.x += self.direcao_x * self.velocidade
        # self.y += self.direcao_y * self.velocidade

        # Para um movimento mais inteligente, veja algoritmos de pathfinding.

        # Exemplo de movimentação baseada em célula (simplificado)
        # Precisa de lógica para evitar paredes e mudar de direção
        possiveis_direcoes = []
        if mapa[int(self.y / TAMANHO_CELULA)][int((self.x + self.velocidade) / TAMANHO_CELULA)] != 1:
            possiveis_direcoes.append((1, 0))
        if mapa[int(self.y / TAMANHO_CELULA)][int((self.x - self.velocidade) / TAMANHO_CELULA)] != 1:
            possiveis_direcoes.append((-1, 0))
        if mapa[int((self.y + self.velocidade) / TAMANHO_CELULA)][int(self.x / TAMANHO_CELULA)] != 1:
            possiveis_direcoes.append((0, 1))
        if mapa[int((self.y - self.velocidade) / TAMANHO_CELULA)][int(self.x / TAMANHO_CELULA)] != 1:
            possiveis_direcoes.append((0, -1))

        import random
        if possiveis_direcoes:
            self.direcao_x, self.direcao_y = random.choice(possiveis_direcoes)
            self.x += self.direcao_x * self.velocidade
            self.y += self.direcao_y * self.velocidade
        else:
            # Se não houver direções possíveis, para
            self.direcao_x = 0
            self.direcao_y = 0


    def desenhar(self, tela):
        pygame.draw.circle(tela, self.cor, (int(self.x + TAMANHO_CELULA / 2), int(self.y + TAMANHO_CELULA / 2)), TAMANHO_CELULA // 2 - 2)