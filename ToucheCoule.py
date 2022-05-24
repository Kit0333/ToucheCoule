import sys
pygame.init()
def surface():
    ecran=pygame.display.set_mode()
    (x,y)=ecran.get_size()
    pygame.display.set_caption("Touché Coulé")
    ecran=pygame.display.set_mode((x,y))

    return (ecran,(x,y))

def plateau(ecran):
    noir=(0,0,0)
    for i in range(10):
        pygame.draw.line(ecran,noir,(i*172,200),(i*172,1080))
        print(i*172)
        pygame.draw.line(ecran,noir,(0,(i*88)+200),(1920,(i*88)+200))
        pygame.display.flip()
    return ecran
def main():
    #initialisation des variables de bases

#-------------------couleurs---------------------

    noir=(0,0,0)
    blanc=(255,255,255)

#-------------------booléens:-----------------------------
    enCours=True
    ecran,test=surface()
    tourJoueur=True
    tourRobot=False

#------------------côté pygame------------------------------

    arial_font = pygame.font.SysFont("arial", 20)
    texteJ1=arial_font.render("C'est le tour du joueur 1",True,noir)
    texteJ2=arial_font.render("C'est le tour du joueur 2",True,noir)

    while enCours:
        ecran.fill(blanc)
        ecran=plateau(ecran)
        ecran.blit(texteJ1,[500,50])
        pygame.display.flip()
        while tourJoueur:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    tourJoueur=False
                    enCours=False
                    pygame.quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        pygame.quit()
                        sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    joueur1PosX, joueur1PosY = pygame.mouse.get_pos()
                    print(joueur1PosX,joueur1PosY)
                    ecran.fill(blanc)
                    ecran.blit(texteJ1, [500, 50])
                    ecran = plateau(ecran)
                    pygame.display.flip()

                    
main()
        
        
