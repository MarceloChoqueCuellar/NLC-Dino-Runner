import random

from nlc_dino_runner.utils.constants import CLOUD, SCREEN_WIDTH


class Cloud:
    SEPARATION = random.randint(350, 450)

    def __init__(self):
        self.x_pos_cloud1 = 0 + self.SEPARATION
        self.x_pos_cloud2 = 0 + self.SEPARATION * 2
        self.x_pos_cloud3 = 0 + self.SEPARATION * 3
        self.x_pos_cloud4 = 0 + self.SEPARATION * 4
        self.y_pos_cloud1 = random.randint(100, 250)
        self.y_pos_cloud2 = random.randint(100, 250)
        self.y_pos_cloud3 = random.randint(100, 250)
        self.y_pos_cloud4 = random.randint(100, 250)
        self.separation = 250

    def draw(self, screen, game_speed):
        screen.blit(CLOUD, (self.x_pos_cloud1, self.y_pos_cloud1))
        screen.blit(CLOUD, (self.x_pos_cloud2, self.y_pos_cloud2))
        screen.blit(CLOUD, (self.x_pos_cloud3, self.y_pos_cloud3))
        screen.blit(CLOUD, (self.x_pos_cloud4, self.y_pos_cloud4))
        self.x_pos_cloud1 -= game_speed // 2
        self.x_pos_cloud2 -= game_speed // 2
        self.x_pos_cloud3 -= game_speed // 2
        self.x_pos_cloud4 -= game_speed // 2

        if self.x_pos_cloud1 <= -SCREEN_WIDTH // 4:
            self.x_pos_cloud1 = SCREEN_WIDTH
            self.y_pos_cloud1 = random.randint(100, 250)

        if self.x_pos_cloud2 <= -SCREEN_WIDTH // 4:
            self.x_pos_cloud2 = SCREEN_WIDTH
            self.y_pos_cloud2 = random.randint(100, 250)

        if self.x_pos_cloud3 <= -SCREEN_WIDTH // 4:
            self.x_pos_cloud3 = SCREEN_WIDTH
            self.y_pos_cloud3 = random.randint(100, 250)

        if self.x_pos_cloud4 <= -SCREEN_WIDTH // 4:
            self.x_pos_cloud4 = SCREEN_WIDTH
            self.y_pos_cloud4 = random.randint(100, 250)