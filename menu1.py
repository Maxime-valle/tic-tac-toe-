import pygame
import sys
import os
from menu2 import menu_2

def menu_1():
    global num_words
    
    pygame.init()
    
    # Fenetre
    win_width, win_height = 800, 600
    win = pygame.display.set_mode((win_width, win_height))

    # Fond d'écran
    background = pygame.image.load(os.path.join('img.son/ville.png'))
    background = pygame.transform.scale(background, (win_width, win_height))

    # Bande son
    pygame.mixer.music.load("img.son/the last u.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(1)

    # Texte
    text_content = ('Il était une fois, dans un monde où les contes de fées se mêlaient à la réalité, une jeune femme intrépide nommée Akai Kōto, surnommée le Petit Chaperon Rouge Moderne. Elle arpentait le monde, parcourant des contrées lointaines à la recherche des saveurs les plus délicieuses. Un jour, alors qu\'elle traversait une forêt mystérieuse connue sous le nom de "Monde Perdu", la nuit tomba rapidement, et le petit chaperon rouge sentit l\'odeur alléchante de nouilles flotter dans l\'air. Curieuse et affamée, elle suivit le parfum délicieux jusqu\'à une clairière où une ville illuminée se dressait au loin. La ville était différente de tout ce qu\'elle avait vu auparavant, car elle était peuplée d\'animaux venus des quatre coins du monde pour explorer ses rues animées. Intriguée, le Petit Chaperon Rouge Moderne s\'aventura dans la cité éclairée....')

    # taille de la police pour afficher tout le texte sans dépasser de la fenêtre
    font_size = 21  
    font = pygame.font.Font(None, font_size)

    # mots à afficher
    num_words = 0

    def draw_text(surface, text, font, color, rect, max_lines):
        global num_words
        words = text.split(' ')
        space_width, _ = font.size(' ')
        
        lines = []
        current_line = []
        current_line_width = 0

        for word in words[:num_words]:
            word_width, word_height = font.size(word)

            if current_line_width + word_width <= rect.width:
                current_line.append(word)
                current_line_width += word_width + space_width
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_line_width = word_width + space_width

        lines.append(' '.join(current_line))

        y = rect.top
        for line in lines[-max_lines:]:
            # Ajouter un effet lumineux +
            text = font.render(line, True, (min(color[0] + 50, 255), min(color[1] + 50, 255), min(color[2] + 50, 255)))
            text_rect = text.get_rect(center=(rect.centerx, y))
            surface.blit(text, text_rect)
            y += text.get_height()

    # Boucle principale
    clock = pygame.time.Clock()
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Vérifier si le bouton est cliqué
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if pygame.Rect(*button_position).collidepoint(mouse_pos):
                    run= False
                    menu_2()
                    
                    

        # Afficher le fond d'écran
        win.blit(background, (0, 0))

        # Afficher le texte en haut de la fenêtre
        text_rect = pygame.Rect(50, 50, win_width - 100, win_height - 100)
        draw_text(win, text_content, font, (255, 255, 255), text_rect, max_lines=10)

        # Dessiner le bouton
        button_color = (50, 50, 50)  
        button_position = (win_width - 100, win_height - 50, 80, 40)  # Position et taille du bouton
        pygame.draw.rect(win, button_color, button_position)

        # Ajouter du texte au bouton
        button_font = pygame.font.Font(None, 20)  
        button_text = button_font.render('Continuer', True, (255, 255, 255))  
        button_text_rect = button_text.get_rect(center=(win_width - 60, win_height - 30))  
        win.blit(button_text, button_text_rect)  

        pygame.display.flip()
        clock.tick(5)  # Limiter la vitesse d'affichage pour contrôler la vitesse du défilement

        # mots à afficher
        num_words += 2