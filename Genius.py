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
cores = [vermelho, verde, azul, amarelo, roxo, laranja, a_piscina, branco]
vermelho_claro = (255, 0, 0)



assets = {}
pygame.mixer.music.set_volume(0.4)
assets['pew_sound'] = pygame.mixer.Sound('som\pew.wav')



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

botoes = [botao_verm, botao_verde, botao_azul, botao_amar]
botoes_novos = [botao_roxo, botao_laranja, botao_a_piscina, botao_branco]  #colocar na lista botoes qnd eles puderem ser usados
seq = []
score = 0
tentativa = []
seq.append(random.choice(botoes))
aguardando = False
inicio = True
while inicio:
    window.blit(imagem2,(0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            inicio = False
pygame.time.wait(2000)            
while game:
    clock.tick(FPS)
    pygame.time.wait(500)
    while aguardando == False: 
        for botao in seq:
            if botao == botao_verm:
                vermelho = vermelho_claro
                pygame.draw.rect(window, vermelho, botao_verm)
                pygame.draw.rect(window, amarelo, botao_amar)
                pygame.draw.rect(window, verde, botao_verde)
                pygame.draw.rect(window, azul, botao_azul)
                pygame.draw.rect(window, roxo, botao_roxo)
                pygame.draw.rect(window, laranja, botao_laranja)
                pygame.draw.rect(window, a_piscina, botao_a_piscina)
                pygame.draw.rect(window, branco, botao_branco)
                pygame.display.update()
                assets['pew_sound'].play()
                pygame.time.wait(500)
                vermelho = (100, 0, 0)
                pygame.draw.rect(window, vermelho, botao_verm)
                pygame.draw.rect(window, amarelo, botao_amar)
                pygame.draw.rect(window, verde, botao_verde)
                pygame.draw.rect(window, azul, botao_azul)
                pygame.draw.rect(window, roxo, botao_roxo)
                pygame.draw.rect(window, laranja, botao_laranja)
                pygame.draw.rect(window, a_piscina, botao_a_piscina)
                pygame.draw.rect(window, branco, botao_branco)
                pygame.display.update()
                pygame.time.wait(500)
            elif botao == botao_verde:
                verde = (0, 255, 0)
                pygame.draw.rect(window, verde, botao_verde)
                pygame.draw.rect(window, vermelho, botao_verm)
                pygame.draw.rect(window, amarelo, botao_amar)
                pygame.draw.rect(window, verde, botao_verde)
                pygame.draw.rect(window, azul, botao_azul)
                pygame.draw.rect(window, roxo, botao_roxo)
                pygame.draw.rect(window, laranja, botao_laranja)
                pygame.draw.rect(window, a_piscina, botao_a_piscina)
                pygame.draw.rect(window, branco, botao_branco)
                pygame.display.update()
                assets['pew_sound'].play()
                pygame.time.wait(500)
                verde = (0, 100, 0)
                pygame.draw.rect(window, verde, botao_verde)
                pygame.draw.rect(window, vermelho, botao_verm)
                pygame.draw.rect(window, amarelo, botao_amar)
                pygame.draw.rect(window, verde, botao_verde)
                pygame.draw.rect(window, azul, botao_azul)
                pygame.draw.rect(window, roxo, botao_roxo)
                pygame.draw.rect(window, laranja, botao_laranja)
                pygame.draw.rect(window, a_piscina, botao_a_piscina)
                pygame.draw.rect(window, branco, botao_branco)
                pygame.display.update()
                pygame.time.wait(500)
            elif botao == botao_amar:
                amarelo = (255, 255, 0)
                pygame.draw.rect(window, amarelo, botao_amar)
                pygame.draw.rect(window, vermelho, botao_verm)
                pygame.draw.rect(window, amarelo, botao_amar)
                pygame.draw.rect(window, verde, botao_verde)
                pygame.draw.rect(window, azul, botao_azul)
                pygame.draw.rect(window, roxo, botao_roxo)
                pygame.draw.rect(window, laranja, botao_laranja)
                pygame.draw.rect(window, a_piscina, botao_a_piscina)
                pygame.draw.rect(window, branco, botao_branco)
                pygame.display.update()
                assets['pew_sound'].play()
                pygame.time.wait(500)
                amarelo = (100, 100, 0)
                pygame.draw.rect(window, amarelo, botao_amar)
                pygame.draw.rect(window, vermelho, botao_verm)
                pygame.draw.rect(window, amarelo, botao_amar)
                pygame.draw.rect(window, verde, botao_verde)
                pygame.draw.rect(window, azul, botao_azul)
                pygame.draw.rect(window, roxo, botao_roxo)
                pygame.draw.rect(window, laranja, botao_laranja)
                pygame.draw.rect(window, a_piscina, botao_a_piscina)
                pygame.draw.rect(window, branco, botao_branco)
                pygame.display.update()
                pygame.time.wait(500)
            elif botao == botao_azul:
                azul = (0, 0, 255)
                pygame.draw.rect(window, azul, botao_azul)
                pygame.draw.rect(window, vermelho, botao_verm)
                pygame.draw.rect(window, amarelo, botao_amar)
                pygame.draw.rect(window, verde, botao_verde)
                pygame.draw.rect(window, azul, botao_azul)
                pygame.draw.rect(window, roxo, botao_roxo)
                pygame.draw.rect(window, laranja, botao_laranja)
                pygame.draw.rect(window, a_piscina, botao_a_piscina)
                pygame.draw.rect(window, branco, botao_branco)
                pygame.display.update()
                assets['pew_sound'].play()
                pygame.time.wait(500)
                azul = (0, 0, 100)
                pygame.draw.rect(window, azul, botao_azul)
                pygame.draw.rect(window, vermelho, botao_verm)
                pygame.draw.rect(window, amarelo, botao_amar)
                pygame.draw.rect(window, verde, botao_verde)
                pygame.draw.rect(window, azul, botao_azul)
                pygame.draw.rect(window, roxo, botao_roxo)
                pygame.draw.rect(window, laranja, botao_laranja)
                pygame.draw.rect(window, a_piscina, botao_a_piscina)
                pygame.draw.rect(window, branco, botao_branco)
                pygame.display.update()
                pygame.time.wait(500)
            
            
        aguardando = True

       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                botao_escolhido = botao_verm
                vermelho = vermelho_claro
                pygame.draw.rect(window, vermelho, botao_verm)
                pygame.display.update()
                assets['pew_sound'].play()
                pygame.time.wait(500)
                vermelho = (100, 0, 0)
                pygame.draw.rect(window, vermelho, botao_verm)
                pygame.display.update()
                tentativa.append(botao_verm)

            elif event.key == pygame.K_a:
                botao_escolhido = botao_amar
                amarelo = (255, 255, 0)
                pygame.draw.rect(window, amarelo, botao_amar)
                pygame.display.update()
                assets['pew_sound'].play()
                pygame.time.wait(500)
                amarelo = (100, 100, 0)
                pygame.draw.rect(window, amarelo, botao_amar)
                pygame.display.update()
                tentativa.append(botao_amar)

            elif event.key == pygame.K_w:
                botao_escolhido = botao_verde
                verde = (0, 255, 0)
                pygame.draw.rect(window, verde, botao_verde)
                pygame.display.update()
                assets['pew_sound'].play()
                pygame.time.wait(500)
                verde = (0, 100, 0)
                pygame.draw.rect(window, verde, botao_verde)
                pygame.display.update()
                tentativa.append(botao_verde)

            elif event.key == pygame.K_s:
                botao_escolhido = botao_azul
                azul = (0, 0, 255)
                pygame.draw.rect(window, azul, botao_azul)
                pygame.display.update()
                assets['pew_sound'].play()
                pygame.time.wait(500)
                azul = (0, 0, 100)
                pygame.draw.rect(window, azul, botao_azul)
                pygame.display.update()
                tentativa.append(botao_azul)
            elif event.key == pygame.K_SPACE:
                aguardando = False
    for botao in tentativa:
        if seq[tentativa.index(botao)] == botao:
            pass
        else:
            score = 0
            tentativa = []
            seq = []
            seq.append(random.choice(botoes))
            window.blit(imagem,(0,0))
            pygame.display.update()
            pygame.time.wait(2000)
            aguardando = False
            

    
    if seq == tentativa:
        score += 1
        tentativa = []
        aguardando = False
        seq.append(random.choice(botoes))
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
