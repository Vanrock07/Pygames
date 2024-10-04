import pygame
import constants
import characters
# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((constants.screen_width, constants.screen_height))
pygame.display.set_caption("Practica 1 Pygame")

def scale_image (image, scale):
     w = image.get_width()
     h = image.get_height()
     new_image = pygame.transform.scale(image, (w*scale, h*scale))
     return new_image

animations = []

# Cargar animaciones
for i in range (7):
     img = pygame.image.load(f"assets//images//characters//main_character//{i+2}.png")
     img = scale_image(img, constants.scale) 
     animations.append(img)

# definir la velocidad de movimiento
frameRate = pygame.time.Clock()

# variables de movimiento
move_left =False
move_right = False  
move_up = False
move_down = False


# Crear jugador
player = characters.Player(50, 50, animations) # se crea el objeto en la posicion 50 50

# Bucle principal del juego
running = True
while running:

    frameRate.tick(constants.fps) # asegura que el juego este a 60 fps

    screen.fill(constants.background) # pintar la pantalla en negro

    # calcular movimiento del jugador
    move_on_x = 0
    move_on_y = 0

    if move_left == True:
            move_on_x = -5
    if move_right == True:
            move_on_x = 5
    if move_up == True: 
            move_on_y = -5
    if move_down == True:
            move_on_y = 5  
 
    player.move(move_on_x, move_on_y)     # mover el objeto
    player.update()                      # animar el objeto   

    player.draw(screen) 
    
                    # dibuja el objeto

    for event in pygame.event.get():      # bucle que mantiene la ventana abierta
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

    pygame.display.update()   # actualiza en cada iteracion

pygame.quit()