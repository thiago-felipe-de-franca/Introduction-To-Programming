import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Quadrado Azul")

# Cores
BLUE = (0, 0, 255)

# Variáveis do quadrado
square_size = 100
square_x = (screen_width - square_size) // 2
square_y = (screen_height - square_size) // 2

# Loop principal
while True:
    # Verifica eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Preenche a tela com a cor branca
    screen.fill((255, 255, 255))

    # Desenha o quadrado azul na tela
    pygame.draw.rect(screen, BLUE, (square_x, square_y, square_size, square_size))

    # Atualiza a tela
    pygame.display.flip()
