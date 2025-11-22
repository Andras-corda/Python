########################
#**********************#
#**   Flappy Bird    **#
#**********************#
#**  B1J5            **#
#**  Corda Andras 1  **#
#**  Fays Hugo    2  **#
#**********************#
########################

import pygame
import os
import random

pygame.init()

# Paramètres

largeur = 800
hauteur = 600
blanc = (255,255,255)
noir = (0,0,0)
vert = (0,200,0)
rouge = (200,0,0)

fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Flappy Bird")

# Images
bird = pygame.image.load(os.path.join('images','dino.png'))
bird = pygame.transform.scale(bird, (60,50))
background = pygame.image.load(os.path.join('images','background.png'))
background = pygame.transform.scale(background, (largeur, hauteur))


# Variables

bird_x = 150
bird_y = hauteur // 2
bird_vy = 0
gravity = 0.5
flap = -8

pipe_width = 100
pipe_gap = 180
pipe_speed = 1
pipes = []

score = 0
font = pygame.font.SysFont("Arial", 30)

game_over = False
running = True
game_started = False     # ← AJOUT : pour remplacer le while True

clock = pygame.time.Clock()

# Premier tuyau
pipe_y_top = random.randint(150, hauteur - 150 - pipe_gap)
pipes.append({"x": largeur, "y_top": pipe_y_top, "passed": False})


pseudo_valide = False

while not pseudo_valide :
    pseudo = str(input("Votre pseudo : "))
    if not pseudo :
        print("Veillez insérer un pseudo")
    elif not pseudo[0].isalpha(): 
        print("Le premier caractère doit être une lettre")
    elif len(pseudo) < 3 : 
        print("le pseudo doit avoir 3 caractère minimum") 
    else :
        pseudo_valide = True

age_valide = False
while not age_valide :
    try : 
        age = int(input(f"{pseudo}, veillez donner votre age : "))
        if age <= 0 : 
            print("Age invalide")
        else : 
            print("Ok")
            age_valide = True
            break
    except ValueError:
        print("Age invalide, Veillez insérer des chiffres uniquement")

if age < 5 : 
    pipe_speed = 1
elif age < 8 :
    pipe_speed = 2
elif age < 10 :
    pipe_speed = 3
elif age < 12 : 
    pipe_speed = 4
else : 
    pipe_speed = 5 

print(pipe_speed)


# -------------------------------
# ** ANCIEN while True supprimé **
# -------------------------------
#
# Ici on affiche "Appuyez sur espace"
# Le jeu NE COMMENCE PAS tant que l’espace n’est pas appuyé
#

while running:

    clock.tick(60)

    # Événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

                if not game_started:
                    game_started = True     # ← On démarre la partie seulement ici

                elif game_over:
                    # Réinitialiser
                    pipes = []
                    pipe_y_top = random.randint(150, hauteur - 150 - pipe_gap)
                    pipes.append({"x": largeur, "y_top": pipe_y_top, "passed": False})
                    bird_y = hauteur // 2
                    bird_vy = 0
                    score = 0
                    game_over = False
                    game_started = True

                else:
                    bird_vy = flap


    # Mécanique de jeu 
    if game_started and not game_over:
        # Gravité
        bird_vy += gravity
        bird_y += bird_vy

        # Déplacement des tuyaux
        for pipe in pipes:
            pipe["x"] -= pipe_speed

        # Nouveau tuyau
        if pipes[-1]["x"] < largeur - 300:
            pipe_y_top = random.randint(150, hauteur - 150 - pipe_gap)
            pipes.append({"x": largeur, "y_top": pipe_y_top, "passed": False})

        # Supprimer les tuyaux hors écran
        new_pipes = []
        for pipe in pipes:
            if pipe["x"] + pipe_width > 0:
                new_pipes.append(pipe)
        pipes = new_pipes

        # Collision et score
        for pipe in pipes:
            top_rect = pygame.Rect(pipe["x"], 0, pipe_width, pipe["y_top"])
            bottom_rect = pygame.Rect(pipe["x"], pipe["y_top"] + pipe_gap, pipe_width, hauteur)
            bird_rect = pygame.Rect(bird_x, bird_y, 60, 50)

            if pipe["x"] + pipe_width < bird_x and pipe["passed"] == False:
                score += 1
                pipe["passed"] = True

            if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
                game_over = True

        # Sol ou plafond
        if bird_y > hauteur - 50 or bird_y < 0:
            game_over = True

    # Affichage 
    fenetre.blit(background, (0,0))

    # Écran d’attente (NOUVEAU)
    if not game_started:
        texte_start = font.render("Appuyez sur ESPACE pour commencer", True, noir)
        fenetre.blit(texte_start, (largeur//2 - texte_start.get_width()//2, hauteur//2))

    else:
        for pipe in pipes:
            pygame.draw.rect(fenetre, vert, (pipe["x"], 0, pipe_width, pipe["y_top"]))
            pygame.draw.rect(fenetre, vert, (pipe["x"], pipe["y_top"] + pipe_gap, pipe_width, hauteur))

        fenetre.blit(bird, (bird_x, bird_y))

        texte_score = font.render("Score : " + str(score), True, noir)
        fenetre.blit(texte_score, (20,20))

    if game_over:
        texte_over = font.render("GAME OVER - Espace pour recommencer", True, rouge)
        fenetre.blit(texte_over, (largeur//2 - texte_over.get_width()//2, hauteur//2))

    pygame.display.flip()

pygame.quit()
