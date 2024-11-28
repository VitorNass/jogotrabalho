import pygame
import random
pygame.init()

x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('Meu jogo em python')

bg = pygame.image.load('asset/MenuBg.png').convert_alpha()
bg = pygame.transform.scale(bg, (x,y))

alien = pygame.image.load('asset/Player1.png').convert_alpha()
alien = pygame.transform.scale(alien, (59,29))

playerImg = pygame.image.load('asset/Enemy1.png').convert_alpha()
playerImg = pygame.transform.scale(playerImg, (86,39)) #conversão do tamanho da nave
playerImg = pygame.transform.rotate(playerImg, 360)

missil = pygame.image.load('asset/Enemy1Shot.png').convert_alpha()
missil = pygame.transform.scale(missil, (86,39)) #conversão do tamanho da nave
missil= pygame.transform.rotate(missil, 360)

#controle de posições GERAL
pos_alien_x= 500
pos_alien_y= 360

pos_player_x= 200
pos_player_y= 300

vel_missil_x = 0
pos_missil_x = 200
pos_missil_y = 300


triggered = False
rodando = True

#funções
def respawn():
    x = 1350
    y = random.randint(1,640)
    return [x,y]
def respawn_missil():
    triggered = False
    respawn_missil_x = pos_player_x
    respawn_missil_y = pos_player_y
    vel_missil_x = 0
    return [respawn_missil_x, respawn_missil_y, triggered, vel_missil_x]

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg, (0,0))
    rel_x= x % bg.get_rect().width
    screen.blit(bg,(rel_x - bg.get_rect().width,0))#cria backgroud
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))

    # controla velocidade de movimento da tela
    x-=2
    pos_alien_x -=1
    pos_missil_x += vel_missil_x

    #criar imagens
    screen.blit(alien,(pos_alien_x, pos_alien_y))
    screen.blit(missil, (pos_missil_x, pos_missil_y))
    screen.blit(playerImg, (pos_player_x, pos_player_y))
    pygame.display.update()

    #teclas
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -=1
        if not triggered:
            pos_missil_y -=1

    if tecla[pygame.K_DOWN] and pos_player_y < 665:
        pos_player_y +=1
        if not triggered:
            pos_missil_y +=1

    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_missil_x = 5
    #respawn
    if pos_alien_x == 50:
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]
    if pos_missil_x == 1300:
        pos_missil_x, pos_missil_y, triggered, vel_missil_x = respawn_missil()


