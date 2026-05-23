import pygame
import random
import sys
import datetime

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Misleading TV Show")

clock = pygame.time.Clock()

def load_img(path):
    img = pygame.image.load(path).convert()
    return pygame.transform.scale(img, (WIDTH, HEIGHT))

background = load_img("ressource/GUI/menu.png")

home_0 = load_img("ressource/GUI/home.png")
home_1 = load_img("ressource/GUI/home_1.png")
home_2 = load_img("ressource/GUI/home_2.png")
home_3 = load_img("ressource/GUI/home_3.png")
home_4 = load_img("ressource/GUI/home_4.png")
home_5 = load_img("ressource/GUI/home_5.png")
home_6 = load_img("ressource/GUI/home_6.png")
home_7 = load_img("ressource/GUI/home_7.png")
home_end = load_img("ressource/GUI/home_end.png")

font = pygame.font.SysFont("Arial", 45, bold=True)
dialog_font = pygame.font.SysFont("Arial", 38)
menu_font = pygame.font.SysFont("Arial", 80, bold=True)
end_font = pygame.font.SysFont("Arial", 120, bold=True)

start_text = menu_font.render("START", True, (255, 255, 255))
start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

def draw_dialog_dual(tv_text=None, char_text=None, alien_text=None):

    if tv_text:
        rect_tv = pygame.Rect(50, HEIGHT - 300, WIDTH - 100, 120)
        pygame.draw.rect(screen, (0, 0, 0), rect_tv)
        pygame.draw.rect(screen, (200, 40, 40), rect_tv, 4)

        for i, line in enumerate(tv_text.split("\n")):
            txt = dialog_font.render(line, True, (255, 255, 255))
            screen.blit(txt, (rect_tv.x + 20, rect_tv.y + 20 + i * 40))


    if char_text:
        rect_char = pygame.Rect(50, HEIGHT - 170, WIDTH - 100, 120)
        pygame.draw.rect(screen, (0, 0, 0), rect_char)
        pygame.draw.rect(screen, (40, 120, 255), rect_char, 4)

        for i, line in enumerate(char_text.split("\n")):
            txt = dialog_font.render(line, True, (255, 255, 255))
            screen.blit(txt, (rect_char.x + 20, rect_char.y + 20 + i * 40))

    if alien_text:
        rect_alien = pygame.Rect(50, HEIGHT - 170, WIDTH - 100, 120)
        pygame.draw.rect(screen, (0, 0, 0), rect_alien)
        pygame.draw.rect(screen, (180, 0, 180), rect_alien, 4)

        for i, line in enumerate(alien_text.split("\n")):
            txt = dialog_font.render(line, True, (255, 255, 255))
            screen.blit(txt, (rect_alien.x + 20, rect_alien.y + 20 + i * 40))


def draw_choice(text, y):
    rect = pygame.Rect(WIDTH - 420, y, 350, 70)
    pygame.draw.rect(screen, (20, 20, 20), rect)
    pygame.draw.rect(screen, (255, 255, 255), rect, 3)

    txt = font.render(text, True, (255, 255, 255))
    txt_rect = txt.get_rect(center=rect.center)
    screen.blit(txt, txt_rect)

    return rect


def draw_glitch(surface):
    for _ in range(2):
        y = random.randint(0, HEIGHT)
        h = random.randint(20, 60)
        alpha = random.randint(40, 90)
        band = pygame.Surface((WIDTH, h))
        band.set_alpha(alpha)
        shade = random.randint(10, 40)
        band.fill((shade, shade, shade))
        surface.blit(band, (0, y))

    if random.random() < 0.12:
        slice_height = random.randint(30, 120)
        y = random.randint(0, HEIGHT - slice_height)
        offset = random.randint(-40, 40)
        slice_surface = surface.subsurface((0, y, WIDTH, slice_height)).copy()
        surface.blit(slice_surface, (offset, y))

    for _ in range(120):
        x = random.randint(0, WIDTH - 1)
        y = random.randint(0, HEIGHT - 1)
        shade = random.randint(20, 60)
        surface.set_at((x, y), (shade, shade, shade))

def global_keys():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if keys[pygame.K_r]:
        menu()


def menu():
    while True:
        screen.blit(background, (0, 0))

        if random.random() < 0.35:
            draw_glitch(screen)

        screen.blit(start_text, start_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    return scene_allumer()

        pygame.display.flip()
        clock.tick(60)


def scene_allumer():
    while True:
        screen.blit(home_0, (0, 0))

        choice = draw_choice("Allumer la TV", HEIGHT//2)

        global_keys()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if choice.collidepoint(event.pos):
                    return scene_choix_emission()

        pygame.display.flip()
        clock.tick(60)

def scene_choix_emission():
    while True:
        screen.blit(home_1, (0, 0))

        c1 = draw_choice("Information", HEIGHT//2)
        c2 = draw_choice("Family Show", HEIGHT//2 + 120)

        global_keys()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if c1.collidepoint(event.pos):
                    return scene_information()

                if c2.collidepoint(event.pos):
                    return scene_family()

        pygame.display.flip()
        clock.tick(60)

def scene_information():
    while True:
        screen.blit(home_2, (0, 0))

        draw_dialog_dual(
            tv_text="Bienvenue dans les informations.\nUne adolescente de 14 ans s'est suicidée.",
            char_text=None
        )

        meteo = draw_choice("Météo", HEIGHT - 250)

        global_keys()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if meteo.collidepoint(event.pos):
                    return scene_meteo()

        pygame.display.flip()
        clock.tick(60)

def scene_family():
    while True:
        screen.blit(home_3, (0, 0))

        draw_dialog_dual(
            tv_text=None,
            char_text="Oh non, pas de pub...\nJe reviendrai plus tard."
        )

        meteo = draw_choice("Météo", HEIGHT - 250)

        global_keys()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if meteo.collidepoint(event.pos):
                    return scene_meteo()

        pygame.display.flip()
        clock.tick(60)

def scene_meteo():
    start = datetime.date.today()
    end = start + datetime.timedelta(days=3)

    while True:
        screen.blit(home_4, (0, 0))

        draw_dialog_dual(
            tv_text=f"Nous aurons de la neige dans toute la France\n"
                    f"du {start.strftime('%d/%m/%Y')} au {end.strftime('%d/%m/%Y')}.",
            char_text="De la neige au printemps... c'est quoi la suite ?\nDu soleil en hiver haha."
        )

        c1 = draw_choice("Family Show", HEIGHT - 350)
        c2 = draw_choice("Télé-réalité", HEIGHT - 250)

        global_keys()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if c1.collidepoint(event.pos) or c2.collidepoint(event.pos):
                    return scene_enlevement()

        pygame.display.flip()
        clock.tick(60)

def scene_enlevement():
    while True:
        screen.blit(home_6, (0, 0))

        draw_dialog_dual(
            tv_text=None,
            char_text="Encore un enlèvement !\nPfff... ils inondent nos écrans."
        )

        c1 = draw_choice("Documentaire", HEIGHT - 350)
        c2 = draw_choice("Informations", HEIGHT - 250)

        global_keys()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if c1.collidepoint(event.pos) or c2.collidepoint(event.pos):
                    return scene_documentaire()

        pygame.display.flip()
        clock.tick(60)

def scene_documentaire():
    while True:
        screen.blit(home_7, (0, 0))

        draw_dialog_dual(
            tv_text="Nous venons de découvrir la présence d'aliens sur Terre.",
            char_text="C'est fou comment la télévision peut nous manipuler."
        )

        next_btn = draw_choice("Continuer", HEIGHT - 250)

        global_keys()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_btn.collidepoint(event.pos):
                    return scene_alien_1()

        pygame.display.flip()
        clock.tick(60)

def scene_alien_1():
    while True:
        screen.blit(home_end, (0, 0))

        draw_dialog_dual(
            alien_text="JE N'AI PAS BEAUCOUP DE TEMPS,\nALORS ECOUTE ATTENTIVEMENT !"
        )

        next_btn = draw_choice("Continuer", HEIGHT - 250)

        global_keys()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_btn.collidepoint(event.pos):
                    return scene_alien_2()

        pygame.display.flip()
        clock.tick(60)

def scene_alien_2():
    while True:
        screen.blit(home_end, (0, 0))

        draw_dialog_dual(
            alien_text="NOUS SOMMES DES MILLIERS À MOURIR\nDANS DES CONDITIONS HORRIBLES",
            char_text="Quoi ?"
        )

        next_btn = draw_choice("Continuer", HEIGHT - 250)

        global_keys()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_btn.collidepoint(event.pos):
                    return scene_alien_3()

        pygame.display.flip()
        clock.tick(60)

def scene_alien_3():
    while True:
        screen.blit(home_end, (0, 0))

        draw_dialog_dual(
            alien_text="LES MÉDIAS TE CONTRÔLENT.ILS TE MONTRENT CE QU'ILS VEULENT.\n"
                       "ILS TE MENTENT ET FONT DE LA PROPAGANDE POLITIQUE OU COMMERCITAL, ILS VEULENT QUE TU NE SOIS PAS CAPABLE DE..."
        )

        next_btn = draw_choice("Continuer", HEIGHT - 250)

        global_keys()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_btn.collidepoint(event.pos):
                    return scene_final_tv()

        pygame.display.flip()
        clock.tick(60)

def scene_final_tv():
    while True:
        screen.blit(home_end, (0, 0))

        draw_dialog_dual(
            tv_text="Veuillez ignorer ce message.\nTout est sous contrôle."
        )

        off_btn = draw_choice("Éteindre la télévision", HEIGHT - 250)

        global_keys()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if off_btn.collidepoint(event.pos):
                    return scene_end()

        pygame.display.flip()
        clock.tick(60)

def scene_end():
    while True:
        screen.fill((0, 0, 0))

        end_text = end_font.render("THE END", True, (200, 0, 0))
        end_rect = end_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 100))

        message_text = font.render("Les informations ont normalisé", True, (200, 0, 0))
        message_rect = message_text.get_rect(center=(WIDTH//2, HEIGHT//2))

        message_text2 = font.render("les éléments les plus choquants", True, (200, 0, 0))
        message_rect2 = message_text2.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))

        screen.blit(end_text, end_rect)
        screen.blit(message_text, message_rect)
        screen.blit(message_text2, message_rect2)


        menu_btn = draw_choice("Menu", HEIGHT//2 + 100)

        global_keys()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_btn.collidepoint(event.pos):
                    return menu()

        pygame.display.flip()
        clock.tick(60)

menu()
