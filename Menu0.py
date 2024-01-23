import pygame
import sys
import os
import pygame_gui
from menu1 import menu_1

pygame.init()

# Fenetre
win_width, win_height = 800, 600
win = pygame.display.set_mode((win_width, win_height))

# Ajouter un titre à la fenêtre
pygame.display.set_caption("Le Petit Chaperon Rouge Moderne")

# Manager pour pygame_gui
manager = pygame_gui.UIManager((win_width, win_height))

# Bouton
button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((win_width//2 - 50, win_height//2 - 25), (100, 50)),
                                       text='Commencer ',
                                       manager=manager)

# Fond d'écran
background = pygame.image.load(os.path.join('img.son/foret.png'))
background = pygame.transform.scale(background, (win_width, win_height))

# Bande son
pygame.mixer.music.load("img.son/Jardin japonais.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(1)

# Initialisation de l'horloge
clock = pygame.time.Clock()

# Boucle principale
running = True
while running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        manager.process_events(event)

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button:
                    menu_1()
                    running = False

    manager.update(time_delta)

    # Dessiner le fond d'écran
    win.blit(background, (0, 0))
    
    manager.draw_ui(win)

    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()
sys.exit()