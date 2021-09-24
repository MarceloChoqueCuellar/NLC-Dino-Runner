import pygame.time

from nlc_dino_runner.components.obstacles.cactus import Cactus
<<<<<<< Updated upstream
from nlc_dino_runner.utils.constants import SMALL_CACTUS
=======
from nlc_dino_runner.utils.constants import SMALL_CACTUS, BIRD, DINO_DEAD
>>>>>>> Stashed changes


class ObstaclesManager:

    def __init__(self):
        self.obstacles_list = []

<<<<<<< Updated upstream
    def update(self, game):
        if len(self.obstacles_list) == 0:
            self.obstacles_list.append(Cactus(SMALL_CACTUS))
=======
    def update(self, game, points):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
            if points >= 350:
                self.obstacles.append(Bird(BIRD))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if isinstance(obstacle, Bird):
                obstacle.fly()
            if game.power_up_manager.hammer.rect.colliderect(obstacle.rect):
                if obstacle in self.obstacles:
                    self.obstacles.remove(obstacle)
>>>>>>> Stashed changes

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)
            if game.player.dino_rect.colliderect(obstacle.rect):
<<<<<<< Updated upstream
                pygame.time.delay(1000)
                game.playing = False
                game.death_count+=1
                break
=======
                if game.player.shield:
                    self.obstacles.remove(obstacle)
                elif game.life_manager.life_counter() == 1:
                    game.life_manager.delete_life()
                    game.player.image = DINO_DEAD
                    game.death_count += 1
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    game.death()
                    pygame.time.delay(1500)
                    break
                else:
                    game.life_manager.delete_life()
                    if obstacle in self.obstacles:
                        self.obstacles.remove(obstacle)
>>>>>>> Stashed changes

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list = []