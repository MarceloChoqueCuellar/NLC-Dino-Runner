import pygame.time

from nlc_dino_runner.components.obstacles.bird import Bird
from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS, BIRD


class ObstaclesManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game, points):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
            if points >= 350:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.power_up_manager.hammer.rect.colliderect(obstacle.rect):
                self.obstacles.remove(obstacle)

            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles.remove(obstacle)
                elif game.life_manager.life_counter() == 1:
                    game.life_manager.delete_life()
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    game.life_manager.delete_life()
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []

