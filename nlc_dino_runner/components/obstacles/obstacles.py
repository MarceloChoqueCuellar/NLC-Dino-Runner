import random

from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, LIGHT_MODE


class Obstacles(Sprite):
    def __init__(self, image, obstacle_type):
        self.image = image
        self.mode = LIGHT_MODE
        self.obstacle_type = obstacle_type
        self.rect = self.image[self.mode][self.obstacle_type].get_rect()
        self.rect.x = SCREEN_HEIGHT + random.randint(800, 1000)# 1100

    def update(self, game_speed, obstacles_list,mode):
        self.mode = mode
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles_list.pop(0)

    def draw(self, screen):
        screen.blit(self.image[self.mode][self.obstacle_type], self.rect)

