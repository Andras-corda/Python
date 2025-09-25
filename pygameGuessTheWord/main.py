import pygame
import random
import string
import json

# Installer
import sys, os, json

def resourcePath(relativePath):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        basePath = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        basePath = os.path.abspath(".")

    return os.path.join(basePath, relativePath)

# Init app
pygame.init()
windowWidth = 800
windowHeight = 600
screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Hangman")

# Fonts
font = pygame.font.SysFont("arial", 48)
smallFont = pygame.font.SysFont("arial", 28)

# Load word list from JSON
with open("mots.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    wordList = data["mots"]

# Reset game state
def resetGame():
    global secretWord, guessedLetters, errorCount, gameOver
    secretWord = random.choice(wordList).upper()
    guessedLetters = []
    errorCount = 0
    gameOver = False

# First play
resetGame()
maxErrors = 7
running = True
fullscreen = False

while running:
    screen.fill((30, 30, 30))

    # Display current word with underscores
    displayWord = ""
    for letter in secretWord:
        if letter in guessedLetters:
            displayWord += letter + " "
        else:
            displayWord += "_ "
    textWord = font.render(displayWord.strip(), True, (255, 255, 255))
    screen.blit(textWord, (windowWidth // 2 - textWord.get_width() // 2, 150))

    # Display guessed letters
    triedText = smallFont.render("Tried letters: " + " ".join(guessedLetters), True, (200, 200, 200))
    screen.blit(triedText, (50, 300))

    # Display error count
    errorText = smallFont.render(f"Errors: {errorCount}/{maxErrors}", True, (255, 100, 100))
    screen.blit(errorText, (50, 400))

    # Check win/lose
    if errorCount >= maxErrors:
        endText = font.render("You lost! The word was " + secretWord, True, (255, 50, 50))
        screen.blit(endText, (windowWidth // 2 - endText.get_width() // 2, 500))
        restartText = smallFont.render("Press SPACE to play again", True, (200, 200, 200))
        screen.blit(restartText, (windowWidth // 2 - restartText.get_width() // 2, 550))
        gameOver = True
    elif all(letter in guessedLetters for letter in secretWord):
        endText = font.render("You won!", True, (50, 255, 50))
        screen.blit(endText, (windowWidth // 2 - endText.get_width() // 2, 500))
        restartText = smallFont.render("Press SPACE to play again", True, (200, 200, 200))
        screen.blit(restartText, (windowWidth // 2 - restartText.get_width() // 2, 550))
        gameOver = True

    pygame.display.update()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Toggle fullscreen with F11
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    windowWidth, windowHeight = screen.get_size()
                else:
                    screen = pygame.display.set_mode((800, 600))
                    windowWidth, windowHeight = 800, 600
            elif gameOver:
                if event.key == pygame.K_SPACE:  
                    resetGame()
            else:
                if event.unicode.upper() in string.ascii_uppercase:
                    letter = event.unicode.upper()
                    if letter not in guessedLetters:
                        guessedLetters.append(letter)
                        if letter not in secretWord:
                            errorCount += 1

pygame.quit()
