from .gameobject import GameObject, globals
import pygame
from pygame import Vector2

font = pygame.font.SysFont("comicsansms", 24)

class Intro(GameObject):
    
    def __init__(self, onAfter):
        super().__init__("Intro")
        self.intro_text = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi.",
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat.",
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    ]
        self.text_y = globals.var.screen_size.y


    def update(self, events):
        self.text_y -= 0.2
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  #skip intro com enter
                    onAfter()

    def draw(self, screen):

        for i, line in enumerate(self.intro_text):
            text_surface = font.render(line, True,globals.var.YELLOW)
            screen.blit(text_surface, (globals.var.screen_size.x // 2 - text_surface.get_width() // 2, self.text_y + i * 30))

       