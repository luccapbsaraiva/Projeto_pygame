import pygame
import random
import sys

pygame.init()

window = pygame.display.set_mode((1250, 600 ))
pygame.display.set_caption('Botões')

font = pygame.font.SysFont(None, 48)
imagem = pygame.image.load("som/voceperdeu.jpg")
imagem = pygame.transform.scale(imagem, (1250, 600))
imagem2= pygame.image.load("som/start.png")
imagem2 = pygame.transform.scale(imagem2, (1250, 600))


vermelho = (100, 0, 0)
verde = (0, 100, 0)
amarelo = (100, 100, 0)
azul = (0, 0, 100)
roxo= (128, 0, 128)
laranja= (150, 80, 0)
a_piscina= (0, 128, 128)
branco = (128, 128, 128)
cor = [vermelho, verde, azul, amarelo, roxo, laranja, a_piscina, branco]

vermelho_claro = (255, 0, 0)
verde_claro =  (0, 255, 0)
amarelo_claro = (255, 255, 0)
azul_claro = (0, 0, 255)
roxo_claro = (255, 0, 255)
laranja_claro = (255, 128, 0)
a_piscina_claro = (0, 255, 255)
branco_claro = (255, 255, 255)
aceso = [vermelho_claro, verde_claro, azul_claro, amarelo_claro, roxo_claro, laranja_claro, a_piscina_claro, branco_claro]

teclas = [pygame.K_q, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_e, pygame.K_d, pygame.K_r, pygame.K_f]

assets = {}
pygame.mixer.music.set_volume(0.4)
assets['pew_sound'] = pygame.mixer.Sound('som\pew.wav')
assets["morreu"] = pygame.mixer.Sound("som/morreu.wav")



botao_verm = pygame.Rect(150, 50, 200, 200)
botao_verde = pygame.Rect(400, 50, 200, 200)
botao_amar = pygame.Rect(150, 300, 200, 200)
botao_azul = pygame.Rect(400, 300, 200, 200)
botao_roxo = pygame.Rect(650, 50, 200, 200)
botao_laranja = pygame.Rect(650, 300, 200, 200)
botao_a_piscina = pygame.Rect(900, 50, 200, 200)
botao_branco = pygame.Rect(900, 300, 200, 200)
clock = pygame.time.Clock()
FPS = 60
vel = 50
game = True

botoes = [botao_verm, botao_verde, botao_azul, botao_amar, botao_roxo, botao_laranja, botao_a_piscina, botao_branco]

seq = []
score = 0
tentativa = []
seq.append(random.randint(0, 7))
text = font.render('os botoes de jogo são: Q W E R A S D F', True, (0, 0, 255))
aguardando = False
inicio = True
while inicio:
    window.blit(imagem2,(0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            inicio = False
pygame.time.wait(2000)
window.fill((0,0,0))
window.blit(text,(200,250))
pygame.display.update()   
pygame.time.wait(3000)
window.fill((0,0,0))
pygame.display.update()   
pygame.time.wait(500)

def pisca(s):
    pygame.draw.rect(window, aceso[s], botoes[s])
    pygame.draw.rect(window, cor[s-1], botoes[s-1])
    pygame.draw.rect(window, cor[s-2], botoes[s-2])
    pygame.draw.rect(window, cor[s-3], botoes[s-3])
    pygame.draw.rect(window, cor[s-4], botoes[s-4])
    pygame.draw.rect(window, cor[s-5], botoes[s-5])
    pygame.draw.rect(window, cor[s-6], botoes[s-6])
    pygame.draw.rect(window, cor[s-7], botoes[s-7])
    pygame.display.update()
    assets['pew_sound'].play()
    pygame.time.wait(500)
    pygame.draw.rect(window, vermelho, botao_verm)
    pygame.draw.rect(window, amarelo, botao_amar)
    pygame.draw.rect(window, verde, botao_verde)
    pygame.draw.rect(window, azul, botao_azul)
    pygame.draw.rect(window, roxo, botao_roxo)
    pygame.draw.rect(window, laranja, botao_laranja)
    pygame.draw.rect(window, a_piscina, botao_a_piscina)
    pygame.draw.rect(window, branco, botao_branco)
    pygame.display.update()
    pygame.time.wait(200)
    
def escolhe_tecla(key):
    if event.key == pygame.K_SPACE:
        aguardando = False
    else:
        if key not in teclas:
            pass
        else:
            tecla = teclas.index(key)
            pisca(tecla)
            tentativa.append(tecla)
    
while game:
    clock.tick(FPS)
    pygame.time.wait(500)
    while aguardando == False: 
        for botao in seq:
            pisca (botao)
        aguardando = True

       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYUP:
            escolhe_tecla (event.key)
            
    for botao in tentativa:
        if seq[tentativa.index(botao)] == botao:
            pass
        else:
            score = 0
            tentativa = []
            seq = []
            seq.append(random.randint(0, 7))
            window.blit(imagem,(0,0))
            assets["morreu"].play()
            pygame.display.update()
            pygame.time.wait(2000)
            aguardando = False
            
    
    if seq == tentativa:
        score += 1
        tentativa = []
        aguardando = False
        seq.append(random.randint(0, 7))
        pygame.time.wait(2000)

       

    window.fill((0, 0, 0))
    pygame.draw.rect(window, vermelho, botao_verm)
    pygame.draw.rect(window, amarelo, botao_amar)
    pygame.draw.rect(window, verde, botao_verde)
    pygame.draw.rect(window, azul, botao_azul)
    pygame.draw.rect(window, roxo, botao_roxo)
    pygame.draw.rect(window, laranja, botao_laranja)
    pygame.draw.rect(window, a_piscina, botao_a_piscina)
    pygame.draw.rect(window, branco, botao_branco)
    font = pygame.font.SysFont(None, 48)
    text_surface = font.render("{:01d}".format(score), True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (50 / 2,  10)
    window.blit(text_surface, text_rect)
    pygame.event.clear()
    pygame.display.update()

pygame.quit()
sys.exit()
