########################
#**********************#
#** Jeu du dinosaure **#
#**     Cours  1     **#
#**********************#
########################

#---------------------------------------------------#
#------------ Zone des initialisations -------------# 
#---------------------------------------------------#

#--- Imports ---#
## Import du module Pygame
import pygame

## Import du module os, permettant de gérer les chemins de fichiers 
## et de dossiers de manière indépendante du système d'exploitation
import os

## Initialisation de tous les modules Pygame
pygame.init()   


#--- Initialisation des paramètres ---#

## Dimensions de la fenêtre de jeu 
largeur = 1600              ## Largeur (en pixels) de la fenêtre de jeu
hauteur = 600               ## hauteur (en pixels) de la fenêtre de jeu
alignBottom = 100           ## Altitude de référence
alignLeft = 20              ## Position pour l'alignement gauche 
## Paramètres de couleurs
blanc = (255, 255, 255)     ## Code RVB du blanc
noir = (0, 0, 0)            ## Code RVB du noir
## Paramètres de saut
isJumping = False           ## Pour vérifier si l'image est en train de sauter
jumpUp = 15                 ## Vitesse verticale initiale
jumpGravity = 0.5           ## Force de gravité
jumpVelocity = 0            ## Vitesse verticale du saut en temps réel (- vers le bas / + vers le haut)
## Dinosaure
dinoWidth = 100             ## Largeur du dino
dinoHeight = 125            ## Hauteur du dino
dinoRefY = hauteur-alignBottom-dinoHeight ## Positionnement du dino sur la base de référence
## Arrière-plan
backgroundX = 0             ## Abscisse de départ de l'arrière plan
backgroundSpeed = 2         ## Vitesse de défilement de l'arrière plan

#---------------------------------------------------------#
#------------- Création de la fenêtre de jeu -------------# 
#---------------------------------------------------------#

# Module "display" en lien avec l'affichage de la fenêtre et les fonctionnalités associées
fenetre = pygame.display.set_mode((largeur, hauteur))
## Crée la fenêtre avec les dimensions définies
## Retourne une "surface" sur laquelle afficher des éléments du jeu 
## Stocke la surface dans une variable pour pouvoir y réaccéder plus tard

#pygame.display.set_caption("Le jeu du dinosaure")
## Donne un titre à la fenêtre (caption = légende)
## Pas stocké dans une variable car on n'a pas besoin d'y réaccéder plus tard
   
#------------------------------------------------#
#------------ Paramètres des images -------------# 
#------------------------------------------------#

#--- Dino ---#
dinoImage = pygame.image.load(os.path.join('images', 'dino.png'))
## Charge l'image
## La stocke dans une variable pour pouvoir y faire appel plus tard 
dino = pygame.transform.scale(dinoImage, (dinoWidth, dinoHeight))
## Redimensionne l'image aux dimensions définies
## Ecrase l'image originelle par celle redimensionnée
dinoRect = pygame.Rect(alignLeft, dinoRefY, dinoWidth, dinoHeight)
## Crée un rectanlge au-dessus de l'image du dino pour gérer les interactions

#--- arrière plan ---#
backgroundImage = pygame.image.load(os.path.join('images', 'background.png'))   ## Charge l'image
background = pygame.transform.scale(backgroundImage, (largeur, hauteur))        ## Redimensionne l'image

#---------------------------------------------#
#------------- Boucle principale -------------# 
#---------------------------------------------#

running = True
## Variable booléenne qui régit l'exécution de la boucle
## La boucle permet de répéter des lignes de code autant de fois que nécessaire
## La boucle est exécutée tant que "running" a la valeur logique True

while running :
    #--------------------------------------------------#
    #------------- Gestion des événements -------------#
    #--------------------------------------------------#

    # Evenement = action / occurence générée par le système / l'utilisateur
    # à laquelle le programme peut réagir
    for event in pygame.event.get() :
        ## pygame.event.get() retourne une liste de tous les événements en attente 
        ### que l’utilisateur a effectués depuis le dernier appel  
        ## for est une boucle qui parcourt chaque événement de cette liste
        if event.type == pygame.QUIT :
            ## Si le type d'événement actuel est "pygame.QUIT"
            ## pygame.QUIT est l'événement quand l’utilisateur 
            ### clique sur le bouton de fermeture de la fenêtre
            running = False
            ## Fait passer la variable booléenne à Faux pour sortir de la boucle de jeu


    #-------------------------------------------#
    #------------- Gestion du Fond -------------#
    #-------------------------------------------#

    # Mise à jour de l'affichage
    fenetre.fill(blanc)

    # Déplacer le fond vers la gauche
    backgroundX -= backgroundSpeed

    # Réinitialiser la position du fond lorsque la première image disparaît
    if backgroundX <= -largeur :
        backgroundX = 0

    # Dessiner deux images de fond pour créer l'effet de défilement
    ## blit : Affichage (objet, (positionX, positionY))
    fenetre.blit(background, (backgroundX, 0))  # Affichage de l'image de fond principale
    fenetre.blit(background, (backgroundX + largeur, 0))  # Affichage de la deuxième image de fond 

    #-------------------------------------------#
    #------------- Gestion du Dino -------------#
    #-------------------------------------------#
    # Affichage de l'image 'dino'
    fenetre.blit(dino, (dinoRect.x, dinoRect.y))

    # Liste des trouches enfoncées
    keys_pressed = pygame.key.get_pressed()
    # Si la touche espace est enfoncée et qu'on est pas déjà pendant un saut
    if keys_pressed[pygame.K_SPACE] and not(isJumping) :
        isJumping = True        ## Indique que le saut commence
        jumpVelocity = -jumpUp  ## Affecte la vitesse verticale de saut

    # Logique de Saut
    if isJumping :
        ## si le contrôleur de saut est vrai
        dinoRect.y += jumpVelocity  
        ## Appliquer l'incrément de hauteur de saut vertical    
        jumpVelocity += jumpGravity 
        ## Faire varier la vitesse en fonction de la gravité 
        ## la vitesse commence à -jumpUp !!! y vers le bas !!!
        ## on ajoute la gravité -> le saut ralenti
        ## quand jumpVelocity = 0, sommet du saut
        ## ensuite le signe de la vitesse change -> le perso redescend 

        # Vérifier si l'image touche le sol    
        if dinoRect.y >= dinoRefY :       
            dinoRect.y = dinoRefY   ## Remettre le dino au sol
            isJumping = False       ## Finir le saut
            jumpVelocity = 0        ## Réinitialiser la vitesse
            

    #----------------------------------------------------------#
    #------------- Rafraichissement de la fenêtre -------------#
    #----------------------------------------------------------#
    # Mise à jour de l'intégralité de la surface d'affichage
    pygame.display.flip()

    # Contrôle de la vitesse de la boucle (FPS)
    pygame.time.Clock().tick(60)

# Quitter Pygame proprement
pygame.quit()