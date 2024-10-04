import pygame
import constants

# Inicializar Pygame
pygame.init()

# Clase para el jugador
class Player():
    #constructor del objeto
    def __init__(self, x, y, animations):
        self.flip = False
        self.animations = animations
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animations[self.frame_index]
        self.shape = pygame.Rect(0, 0, 20, 20)
        self.shape.center = (x, y)
      
# ****metodos de la clase*****
# dibujar el objeto 
    def draw(self, interfaz):
        image_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(image_flip, self.shape)
       # pygame.draw.rect(interfaz, (255, 255, 0), self.shape) 

# actualizar las animaciones
    def update(self):
       cooldown_animation = 100
       self.image = self.animations[self.frame_index]

       if pygame.time.get_ticks() - self.update_time >= cooldown_animation:
           self.frame_index = self.frame_index +1
           self.update_time = pygame.time.get_ticks()
       if self.frame_index == len(self.animations):
           self.frame_index = 0    


# mover el objeto
    def move(self, move_on_x , move_on_y):
        if move_on_x < 0:
            self.flip = True
        elif move_on_x > 0:   
            self.flip = False
 
        self.shape.x = self.shape.x + move_on_x
        self.shape.y = self.shape.y + move_on_y
    