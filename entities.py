# entities.py

import pygame
from config import PADDLE_WIDTH, PADDLE_HEIGHT, BALL_SIZE, BALL_SPEED, PADDLE_SPEED, COLORS, WIDTH, HEIGHT

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, up_key, down_key):
        """Déplace le paddle en fonction des touches appuyées."""
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED
        if keys[down_key] and self.rect.bottom < HEIGHT:
            self.rect.y += PADDLE_SPEED

    def draw(self, screen, color):
        """Dessine le paddle à l'écran."""
        pygame.draw.rect(screen, color, self.rect)


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        self.dx = BALL_SPEED
        self.dy = BALL_SPEED

    def move(self):
        """Déplace la balle et gère les collisions avec le mur."""
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Collision avec le haut et le bas
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy = -self.dy

    def reset(self):
        """Réinitialise la position de la balle au centre."""
        self.rect.x = WIDTH // 2 - BALL_SIZE // 2
        self.rect.y = HEIGHT // 2 - BALL_SIZE // 2

    def draw(self, screen):
        """Dessine la balle à l'écran."""
        pygame.draw.rect(screen, COLORS['yellow'], self.rect)
