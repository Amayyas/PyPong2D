# game.py

import pygame
import sys
from config import WIDTH, HEIGHT, COLORS, FONT_NAME, FONT_SIZE, PADDLE_WIDTH, PADDLE_HEIGHT
from entities import Paddle, Ball

# Initialisation de Pygame
pygame.init()

# Initialisation de la police
font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)

# Initialisation de l'écran
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyPong2D")

# Initialisation de l'horloge
clock = pygame.time.Clock()


class Game:
    def __init__(self):
        """Initialise les paddles, la balle et les scores."""
        self.left_paddle = Paddle(30, HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.right_paddle = Paddle(WIDTH - 30 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.ball = Ball()
        self.left_score = 0
        self.right_score = 0

    def display_score(self):
        """Affiche le score au centre de l'écran."""
        score_text = font.render(f"Score: {self.left_score} - {self.right_score}", True, COLORS['yellow'])
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    def victory(self, winner):
        """Affiche l'écran de victoire."""
        screen.fill(COLORS['blue'])
        victory_text = font.render(f"{winner} wins!", True, COLORS['yellow'])
        screen.blit(victory_text, (WIDTH // 2 - victory_text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(3000)

    def handle_collisions(self):
        """Vérifie et gère les collisions entre la balle et les paddles."""
        if self.ball.rect.colliderect(self.left_paddle.rect) or self.ball.rect.colliderect(self.right_paddle.rect):
            self.ball.dx = -self.ball.dx

    def update_score(self):
        """Met à jour les scores si la balle sort du terrain."""
        if self.ball.rect.left <= 0:
            self.right_score += 1
            self.ball.reset()
        if self.ball.rect.right >= WIDTH:
            self.left_score += 1
            self.ball.reset()

    def game_loop(self):
        """Boucle principale du jeu."""
        while True:
            screen.fill(COLORS['blue'])

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Mouvement des paddles et de la balle
            self.left_paddle.move(pygame.K_z, pygame.K_s)
            self.right_paddle.move(pygame.K_UP, pygame.K_DOWN)
            self.ball.move()

            # Gestion des collisions
            self.handle_collisions()
            self.update_score()

            # Vérifier si un joueur a gagné
            if self.left_score >= 3:
                self.victory("Left")
                break
            if self.right_score >= 3:
                self.victory("Right")
                break

            # Dessiner les éléments du jeu
            self.left_paddle.draw(screen, COLORS['green'])
            self.right_paddle.draw(screen, COLORS['purple'])
            self.ball.draw(screen)
            self.display_score()

            # Mise à jour de l'affichage
            pygame.display.flip()
            clock.tick(60)
