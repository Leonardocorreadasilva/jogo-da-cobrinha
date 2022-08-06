from tkinter import Y
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()


'''musicaDeFundo = pygame.mixer.music.load('music.mp3')
musicaDeFundo.set_volume(0.1)
musicaDeFundo.play(-1)'''

barulhoColisao = pygame.mixer.Sound('smw_coin.wav')

largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Cobrinha')
relogio = pygame.time.Clock()
listaCobra = []
ComprimentoInicial = 5

xCobra = int(largura/2)
yCobra = int(altura/2)

velocidade = 10

xControle = velocidade
yControle = 0

xMaca = randint(40, 600)
yMaca = randint(50, 430)
fonte = pygame.font.SysFont('arial', 40, True, True)
pontos = 0
morreu = False

def aumentaCobra(listaCobra):
        for XeY in listaCobra:
                pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

def ReiniciarJogo():
        global pontos, ComprimentoInicial, xCobra, yCobra, listaCabeca, listaCobra, xMaca, yMaca, morreu
        pontos = 0
        ComprimentoInicial = 5
        xCobra = int(largura/2)
        yCobra = int(altura/2)
        listaCobra = []
        listaCabeca = []
        xMaca = randint(40, 600)
        yMaca = randint(50, 430)
        morreu = False

while True:
        relogio.tick(30)
        tela.fill((255,255,255))
        mensagem = f'Pontos: {pontos}'
        textoFormatado = fonte.render(mensagem, False, (0,0,0))
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        exit() 

                if event.type == KEYDOWN:
                        if event.key == K_a:
                                if xControle == velocidade:
                                        pass
                                else:
                                        xControle = -velocidade
                                        yControle = 0

                        if event.key == K_d:
                                if xControle == -velocidade:
                                        pass
                                else:
                                        xControle = velocidade
                                        yControle = 0

                        if event.key == K_w:
                                if yControle == velocidade:
                                        pass
                                else:   
                                        xControle = 0
                                        yControle = -velocidade

                        if event.key == K_s:
                                if yControle == -velocidade:
                                        pass
                                else:
                                        xControle = 0
                                        yControle = velocidade
        xCobra = xCobra + xControle
        yCobra = yCobra + yControle


        cobra = pygame.draw.rect(tela, (0,255,0), (xCobra,yCobra,20,20))
        maca = pygame.draw.rect(tela, (255,0,0), (xMaca,yMaca,20,20))
        if cobra.colliderect(maca):
                xMaca = randint(40, 600)
                yMaca = randint(50, 430)
                barulhoColisao.play()
                pontos = pontos + 1
                ComprimentoInicial = ComprimentoInicial + 1
       
        listaCabeca = []  
        listaCabeca.append(xCobra)
        listaCabeca.append(yCobra)
    
        listaCobra.append(listaCabeca)
        if listaCobra.count(listaCabeca) > 1:
                fonte2 = pygame.font.SysFont('arial', 20, True, True)
                mensagem = 'Morreu playBoy | Aperte R para reiniciar o jogo'
                textoFormatado = fonte2.render(mensagem, True, (0,0,0))
                RetTexto = textoFormatado.get_rect()
                morreu = True
                while morreu:
                        tela.fill((255,255,255))
                        for event in pygame.event.get():
                                if event.type == QUIT:
                                        pygame.quit()
                                        exit()
                                if event.type == KEYDOWN:
                                        if event.key == K_r:
                                                ReiniciarJogo()
                        RetTexto.center = (largura//2, altura // 2)
                        tela.blit(textoFormatado, RetTexto)
                        pygame.display.update()

        if xCobra > largura:
                xCobra = 0
        if xCobra < 0:
                xCobra = largura
        if yCobra < 0:
                yCobra = altura
        if yCobra > altura:
                yCobra = 0

        if len(listaCobra) > ComprimentoInicial:
                del listaCobra[0]

        aumentaCobra(listaCobra) 

        tela.blit(textoFormatado,(425,40))            
        pygame.display.update()