import pygame
import sys
import os

pygame.init()

# Fenetre
win_width, win_height = 800, 600
win = pygame.display.set_mode((win_width, win_height))

# Fond d'écran
background = pygame.image.load(os.path.join('img.son', 'nouille.png'))
background = pygame.transform.scale(background, (win_width, win_height))

# Bande son
pygame.mixer.music.load("img.son/rpg.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(1)

# Texte
text_content = ('Au cœur de la ville, elle découvrit un restaurant de nouilles réputé, connu pour ses spécialités venues des contrées les plus reculées. Affamée, elle s\'apprêta à déguster son plat quand soudain, un homme mystérieux et robuste, dissimulé sous une capuche, s\'approcha d\'elle. Ses yeux perçants brillaient comme des étoiles dans l\'obscurité. L\'homme mystérieux défia le Petit Chaperon Rouge. Il lui proposa de manger son plat de nouilles en un temps record, sinon c\'était elle qui se ferait dévorer. Il révéla sa véritable identité : un loup à la stature imposante, connu pour ses défis gastronomiques redoutables.')

# Ajuster la taille de la police pour afficher tout le texte sans dépasser de la fenêtre
font_size = 21  #la police
font = pygame.font.Font(None, font_size)

# Nombre de mots à afficher
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
        # Ajouter un effet lumineux en rendant le texte plus clair
        text = font.render(line, True, (min(color[0] + 50, 255), min(color[1] + 50, 255), min(color[2] + 50, 255)))
        text_rect = text.get_rect(center=(rect.centerx, y))
        surface.blit(text, text_rect)
        y += text.get_height()

# Boucle principale
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Afficher le fond d'écran
    win.blit(background, (0, 0))

    # Afficher le texte en bas de la fenêtre
    text_rect = pygame.Rect(50, win_height - 150, win_width - 100, 100)  # Ajuster la position y pour qu'elle soit plus basse
    draw_text(win, text_content, font, (255, 255, 255), text_rect, max_lines=10)

    pygame.display.flip()
    clock.tick(5)  # Limiter la vitesse d'affichage pour contrôler la vitesse du défilement

    # Augmenter le nombre de mots à afficher
    num_words += 2
