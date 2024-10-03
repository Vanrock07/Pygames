import pygame
import constants

# Inicializar Pygame
pygame.init()

# Clase para el jugador
class Player():
    #constructor del objeto
    def __init__(self, x, y):
        self.shape = pygame.Rect(0, 0, 20, 20)
        self.shape.center = (x, y)
      
# ****metodos de la clase*****
# dibujar el objeto 
    def draw(self, interfaz):
        pygame.draw.rect(interfaz, (255, 255, 0), self.shape) 

# mover el objeto
    def move(self, move_on_x , move_on_y):
        self.shape.x = self.shape.x + move_on_x
        self.shape.y = self.shape.y + move_on_y
    