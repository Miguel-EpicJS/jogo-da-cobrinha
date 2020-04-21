import pygame, random#importo as bibliotecas
from pygame.locals import *

def on_grid_random():#defino uma grade para a maça
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):#confiro a colisão da maça com a cobra
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0#direções
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()#inicio o pygame
screen = pygame.display.set_mode((600,600))#inicio a tela
pygame.display.set_caption('Snake')#coloco um nome na tela

snake = [(200, 200), (210, 200), (220,200)]#crio a cobra
snake_skin = pygame.Surface((10,10))#coloco uma skin para ela
snake_skin.fill((255,255,255))#preencho ela com uma cor

apple_pos = on_grid_random()#posição da maça
apple = pygame.Surface((10,10))#maça é criada
apple.fill((255,0,0))#preencho a maça

my_direction = LEFT # defino uma direção padrão

clock = pygame.time.Clock()#variavel do clock

while True:#loop infinito
    clock.tick(10)#FPS do jogo
    for event in pygame.event.get():#evento para sair do jogo
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:#direção
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):#colisão com a maça
        apple_pos = on_grid_random()
        snake.append((0,0))

    for i in range(len(snake) - 1, 0, -1):#movimentação da cobra
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0,0,0))#limpo a tela
    screen.blit(apple, apple_pos)# coloco a maça
    for pos in snake:# coloco a cobra
        screen.blit(snake_skin,pos)

    pygame.display.update()
