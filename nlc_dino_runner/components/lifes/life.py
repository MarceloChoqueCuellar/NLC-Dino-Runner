from nlc_dino_runner.utils.constants import HEART, LIGHT_MODE
from pygame.sprite import Sprite


class Life(Sprite):
    def __init__(self, pos_x):
        self.image = HEART
        self.mode = LIGHT_MODE
        self.pos_x = pos_x
        self.life_rect = self.image[self.mode].get_rect()
        self.life_rect.x = self.pos_x
        self.life_rect.y = 40

    def update(self, mode):
        self.mode =mode

    def draw(self, screen):
        screen.blit(self.image[self.mode], (self.life_rect.x, self.life_rect.y))