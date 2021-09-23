#EQUIPE:
#ALICE LONGMAN
#LUCCA SARAIVA
#PEDRO VON DANNECKER

import pygame
import random
import sys

class c_game:
    def __init__(self):
        self.colors = {"vermelho" : (100, 0, 0), "verde" : (0, 100, 0), "amarelo" : (100, 100, 0), "azul" : (0, 0, 100), "roxo" : (128, 0, 128), "laranja" : (150, 80, 0), "azul piscina" : (0, 128, 128), "branco" : (128, 128, 128),
            "vermelho claro" : (255, 0, 0), "verde claro" : (0, 255, 0), "azul claro" : (0, 0, 255), "amarelo claro" : (255, 255, 0), "roxo claro" : (255, 0, 255), "laranja claro" : (255, 128, 0), "azul piscina claro" : (0, 255, 255), "branco claro" : (255, 255, 255)}
        self.buttons = {"vermelho" : pygame.Rect(150, 50, 200, 200), "verde" : pygame.Rect(400, 50, 200, 200), "amarelo" : pygame.Rect(150, 300, 200, 200), "azul" : pygame.Rect(400, 300, 200, 200), "roxo" : pygame.Rect(650, 50, 200, 200),
            "laranja" : pygame.Rect(650, 300, 200, 200), "azul piscina" : pygame.Rect(900, 50, 200, 200), "branco" : pygame.Rect(900, 300, 200, 200)}
        self.keys = [pygame.K_q, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_e, pygame.K_d, pygame.K_r, pygame.K_f]
        self.states = {"start" : 0, "transition" : 1, "in game" : 2, "loss" : 3}

    def initialize(self):
        self.window = pygame.display.set_mode((1250, 600))
        self.rules = {"framerate" : 100}

        pygame.display.set_caption('Botões')

        pygame.mixer.music.set_volume(0.4)
        self.initialize_assets()

        self.clock = pygame.time.Clock()
        self.score = 0
        self.sequence = [random.randint(0, 7)]

        self.attempt = []

        self.state = self.states["start"]
        self.waiting = False

    def initialize_assets(self):
        self.font = pygame.font.SysFont(None, 48)

        self.sprite = {"start" : pygame.transform.scale(pygame.image.load("som/start.png"), (1250, 500)), "loss" : pygame.transform.scale(pygame.image.load("som/voceperdeu.jpg"), (1250, 600))}
        self.audio = {"pew_sound" : pygame.mixer.Sound('som\pew.wav'), "morreu" : pygame.mixer.Sound("som/morreu.wav")}

    def frame_think(self):
        self.clock.tick(self.rules["framerate"])
        pygame.time.wait(3)

        if not self.waiting:
            for button in self.sequence:
                self.blink(button)
            self.waiting = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.waiting = False
                    self.attempt = []
                else:
                    self.key_select(event.key)

        for button in self.attempt:
            if button in self.attempt and self.sequence[self.attempt.index(button)] == button:
                pass
            else:
                self.score = 0
                self.attempt = []
                self.sequence = [random.randint(0, 7)]
                self.window.blit(self.sprite["loss"],(0,0))
                self.audio["morreu"].play()
                pygame.display.update()
                pygame.time.wait(2000)
                self.waiting = False
            
    
        if self.sequence == self.attempt:
            self.score += 1
            self.attempt = []
            self.waiting = False
            self.sequence.append(random.randint(0, 7))
            pygame.time.wait(2000)

        return True
    
    def frame_render(self):
        self.window.fill((0, 0, 0))
        for color in list(self.colors.keys())[:8]:
            pygame.draw.rect(self.window, self.colors[color], self.buttons[color])
            
        self.font = pygame.font.SysFont(None, 48)
        text_surface = self.font.render("{:01d}".format(self.score), True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (50 / 2,  10)
        self.window.blit(text_surface, text_rect)

        pygame.event.clear()
        pygame.display.update()

    def handle_scene(self):
        while True:
            if self.state == self.states["start"]:
                
                if not self.scene_start():
                    self.state = self.states["transition"]

            elif self.state == self.states["transition"]:
                
                self.scene_transition()
                self.state = self.states["in game"]

            elif self.state == self.states["in game"]:
                if not self.scene_in_game():
                    break

    def scene_in_game(self):
        if self.frame_think():
            self.frame_render()
            return True

        return False

    def scene_start(self):
        self.window.blit(self.sprite["start"], (0,0))
        self.window.blit(self.font.render("Clique em qualquer tecla para começar o jogo", True, (255, 255, 255)), (0, 550))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                return False

        return True

    def scene_transition(self):
        pygame.time.wait(2000)
        self.window.fill((0,0,0))
        self.window.blit(self.font.render("BEM VINDO AO GENIUS!", True, (128, 128, 128)), (500, 50))
        self.window.blit(self.font.render('os botões de jogo são:', True, (0, 0, 255)), (150, 150))

        print(self.colors)

        letters = ['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F']
        x, y = 200, 250
        for index, letter in enumerate(letters):
            # cores claras, logo indice da primeira cor clara + index
            x += 50
            if x > 350:
                x = 200
            
            if index == 4:
                y += 50

            print(f'8 + {index} = {8 + index}; total size: {len(list(self.colors.values()))}')
            self.window.blit(self.font.render(letter, True, list(self.colors.values())[8 - index]), (x, y))

        self.window.blit(self.font.render("Com as teclas de jogo, reproduza a sequência apresentada", True, (128, 128, 128)), (150, 400))
        self.window.blit(self.font.render("Caso precise rever a sequência tecle SPACE", True, (128, 128, 128)), (150, 450))
        self.window.blit(self.font.render("Se você errar a sequência perde o jogo", True, (128, 128, 128)), (150, 500))
        
        pygame.display.update()   
        pygame.time.wait(8000)
        
        self.window.fill((0, 0, 0))
        
        pygame.display.update()   
        pygame.time.wait(500)

    def key_select(self, key):
        if key not in self.keys:
            pass

        else:
            tecla = self.keys.index(key)
            self.blink(tecla)
            self.attempt.append(tecla)

    def blink(self, s):
        pygame.draw.rect(self.window, list(self.colors.values())[s + 8], list(self.buttons.values())[s])

        for idx in range(1, 8):
            pygame.draw.rect(self.window, list(self.colors.values())[s-1], list(self.buttons.values())[s-1])

        pygame.display.update()
        self.audio['pew_sound'].play()

        pygame.time.wait(500)
        for key in list(self.colors.keys())[:8]:
            pygame.draw.rect(self.window, self.colors[key], self.buttons[key])

        pygame.display.update()
        pygame.time.wait(200)
    
pygame.init()

game_instance = c_game()
game_instance.initialize()
game_instance.handle_scene()

pygame.quit()
sys.exit()
