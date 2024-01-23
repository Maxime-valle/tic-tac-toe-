import pygame
import sys
import os 

def tic_tac_toe():

    pygame.init()

    # la fenêtre
    taille_case = 100
    marge = 15
    taille_grille = 3
    taille_fenetre = taille_case * taille_grille + marge * (taille_grille + 1)
    fenetre = pygame.display.set_mode((taille_fenetre, taille_fenetre))

    # Bande son
    pygame.mixer.music.load("img.son/SuperS.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(1)

    # Définir les dimensions de la fenêtre
    win_width = taille_fenetre
    win_height = taille_fenetre

    #fond d'écran
    background = pygame.image.load(os.path.join('img.son/ville.png'))
    background = pygame.transform.scale(background, (win_width, win_height))

    # Configuration des couleurs
    COULEUR_FOND = (28, 170, 156)
    LIGNE_COULEUR = (23, 145, 135)
    CROIX_COULEUR = (66, 66, 66)
    ROND_COULEUR = (239, 231, 200)

    # Configuration du jeu
    grille = [[None, None, None] for _ in range(3)]
    joueur = "X"

    def dessiner_grille():
        for x in range(1, taille_grille):
            pygame.draw.line(fenetre, LIGNE_COULEUR, (0, taille_case * x + marge * x), (taille_fenetre, taille_case * x + marge * x), marge)
            pygame.draw.line(fenetre, LIGNE_COULEUR, (taille_case * x + marge * x, 0), (taille_case * x + marge * x, taille_fenetre), marge)
        pygame.display.flip()

    def dessiner_symboles():
        for y in range(taille_grille):
            for x in range(taille_grille):
                centre_x = taille_case * x + taille_case // 2 + marge * (x + 1)
                centre_y = taille_case * y + taille_case // 2 + marge * (y + 1)
                if grille[y][x] == "X":
                    pygame.draw.line(fenetre, CROIX_COULEUR, (centre_x - 20, centre_y - 20), (centre_x + 20, centre_y + 20), marge)
                    pygame.draw.line(fenetre, CROIX_COULEUR, (centre_x + 20, centre_y - 20), (centre_x - 20, centre_y + 20), marge)
                elif grille[y][x] == "O":
                    pygame.draw.circle(fenetre, ROND_COULEUR, (centre_x, centre_y), 30, marge)
        pygame.display.flip()

    def verifier_victoire(joueur):
        #  les lignes
        for y in range(taille_grille):
            if all([case == joueur for case in grille[y]]):
                return True
        #  les colonnes
        for x in range(taille_grille):
            if all([grille[y][x] == joueur for y in range(taille_grille)]):
                return True
        #  les diagonales
        if all([grille[i][i] == joueur for i in range(taille_grille)]) or all([grille[i][taille_grille - i - 1] == joueur for i in range(taille_grille)]):
            return True
        return False

    # Boucle principale
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                grille_y = y // (taille_case + marge)
                grille_x = x // (taille_case + marge)
                if grille[grille_y][grille_x] is None:
                    grille[grille_y][grille_x] = joueur
                    if verifier_victoire(joueur):
                        font = pygame.font.Font(None, 72)
                        texte = font.render(f"Le joueur {joueur} a gagné !", True, (255, 255, 255))
                        fenetre.blit(texte, (taille_fenetre // 2 - texte.get_width() // 2, taille_fenetre // 2 - texte.get_height() // 2))
                        pygame.display.flip()
                        pygame.time.wait(3000)
                        # Réinitialiser la grille et le joueur
                        grille = [[None, None, None] for _ in range(3)]
                        joueur = "X"
                    else:
                        joueur = "O" if joueur == "X" else "X"
                    fenetre.fill(COULEUR_FOND)
                    dessiner_grille()
                    dessiner_symboles()
                    pygame.display.flip()
