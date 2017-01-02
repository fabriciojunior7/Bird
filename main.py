import pygame, sys, time, random
import bird, chao, ambiente, obstaculos

#Cores
azul_ceu = (102, 255, 255)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

global pontos
pontos = []
global the_best
the_best = 0

def main():
    pygame.init()
    largura = 600
    altura = 400
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("The Bird!")

    #Fontes
    pygame.font.init()
    font = pygame.font.get_default_font()
    font_potuacao = pygame.font.SysFont(font, 25)
    font_best = pygame.font.SysFont(font, 25)

    ponto = 0

    gravidade = 0.25
    num_nuvens = 15
    nuvens = []
    num_tubos = 5
    tubos = []
    tubos_teto = []
    moedas = []
    passando = False

    for i in range(num_nuvens):
        nuvens.append(ambiente.Nuvem())

    for i in range(num_tubos):
        tubos.append(obstaculos.Tubos((i + 6) * 120))

    for t in tubos:
        novo_tubo = obstaculos.Tubos(t.corpo.x)
        novo_tubo.corpo.y = t.corpo.y - 650
        tubos_teto.append(novo_tubo)
        #moeda = pygame.

    relogio = pygame.time.Clock()
    frames = 60

    #Player e Objetos
    player = bird.Bird()
    solo = chao.Chao(largura)
    sol = ambiente.Sol()

    def perdeu():
        restart = False
        global the_best
        if(ponto > the_best): the_best = ponto
        while (not restart):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_RETURN):
                        restart = True
            relogio.tick(frames)
        main()

    f_passados = -419

    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()

            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE):
                    player.pula()

        #Checar
        if(player.corpo.y < -100):
            player.velocidade = 1

        #Rodar
        relogio.tick(frames)
        player.cair(gravidade)
        #Desenha
        tela.fill(azul_ceu)
        sol.desenha(tela)
        for n in nuvens:
            n.desenha(tela)
            n.anda()
            if(n.x < -n.largura):
                n.volta()

        nota_anterior = ponto

        for i in range(len(tubos)):
            y = random.randint(70, 380)
            distancia = random.randint(570, 670)
            tubos[i].desenha(tela)
            tubos[i].anda()
            tubos_teto[i].desenha(tela)
            tubos_teto[i].anda()
            if (tubos[i].corpo.x < -20):
                tubos[i].volta(y)
            if (tubos_teto[i].corpo.x < -20):
                tubos_teto[i].volta(y - distancia)
            if(player.corpo.colliderect(tubos[i].corpo) or player.corpo.colliderect(tubos_teto[i].corpo)):
                perdeu()

            if(player.corpo.colliderect(tubos[i].moeda) and nota_anterior == ponto):
                ponto += 1
                tubos[i].moeda.x = 0


        #Colisoes
        if(player.corpo.colliderect(solo.corpo)):
            perdeu()

        solo.desenha(tela)
        player.desenha(tela)
        pontuacao = font_potuacao.render("%i" % ponto, 1, vermelho)
        best = font_best.render("%i" % the_best, 1, vermelho)
        tela.blit(pontuacao, (0, 0))
        tela.blit(best, (0, 382))
        pygame.display.update()



main()