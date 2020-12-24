import pygame
import math
import random

pygame.init()

# Setting up the display
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman App")

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) /2)
starty = 400
A = 65

for i in range(26):
    x = startx + GAP * 2 + (RADIUS * 2 + GAP) * (i % 13)
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x,y,chr(A + i),True])


# Fonts
LETTER_FONT = pygame.font.SysFont('Arial', 30)
WORD_FONT = pygame.font.SysFont("Arial",35)
TITLE_FONT = pygame.font.SysFont("Arial",50)


# Loading images
images = []
for i in range(7):
    image = pygame.image.load("images/hangman"+ str(i) + ".png")
    images.append(image)

# Game variables
hangman_status = 0
words = ["HELLO","GAME","TEST","APPLE","BOOT","AMAZING"]
word = random.choice(words)
guessed = []

#colors
WHITE = (255,255,255)
DARK_GREY = (32,33,38)
DARK_BLUE = (9,18,82)
BLACK = (0,0,0)

# Setting up the game loop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    # fill screen with color
    win.fill(DARK_BLUE)

    # draw title
    text = TITLE_FONT.render("HANGMAN GAME",1,BLACK)
    win.blit(text,(WIDTH/2 - text.get_width()/2,20))

    #draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word+= letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word,1,BLACK)
    win.blit(text,(400,200))


    # draw buttons
    for letter in letters:
        x,y,ltr,visible = letter
        if visible:
         pygame.draw.circle(win,BLACK,(x,y),RADIUS,3)
         # render the text
         text = LETTER_FONT.render(ltr,1,BLACK)
         win.blit(text, (x-text.get_width()/2,y-text.get_height()/2))

    # draw an image
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def dispaly_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)



while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x,m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                  dis = math.sqrt((x-m_x)**2 + (y-m_y)**2)
                  if dis < RADIUS:
                      letter[3] = False
                      guessed.append(ltr)
                      if ltr not in word:
                        hangman_status+=1
    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        dispaly_message("YOU WIN!")
        break

    if hangman_status == 6:
        dispaly_message("YOU LOST!")
        break

pygame.quit()