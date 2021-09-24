import pygame.time

from nlc_dino_runner.components.obstacles.bird import Bird
from nlc_dino_runner.components.obstacles.cactus import Cactus
<<<<<<< HEAD
from nlc_dino_runner.utils.constants import SMALL_CACTUS, BIRD
=======
<<<<<<< Updated upstream
from nlc_dino_runner.utils.constants import SMALL_CACTUS
=======
from nlc_dino_runner.utils.constants import SMALL_CACTUS, BIRD, DINO_DEAD
>>>>>>> Stashed changes
>>>>>>> main


class ObstaclesManager:

    def __init__(self):
        self.obstacles = []

<<<<<<< HEAD
=======
<<<<<<< Updated upstream
    def update(self, game):
        if len(self.obstacles_list) == 0:
            self.obstacles_list.append(Cactus(SMALL_CACTUS))
=======
>>>>>>> main
    def update(self, game, points):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
            if points >= 350:
                self.obstacles.append(Bird(BIRD))
<<<<<<< HEAD

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.power_up_manager.hammer.rect.colliderect(obstacle.rect):
                self.obstacles.remove(obstacle)
=======
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if isinstance(obstacle, Bird):
                obstacle.fly()
            if game.power_up_manager.hammer.rect.colliderect(obstacle.rect):
                if obstacle in self.obstacles:
                    self.obstacles.remove(obstacle)
>>>>>>> Stashed changes
>>>>>>> main

            if game.player.dino_rect.colliderect(obstacle.rect):
<<<<<<< HEAD
=======
<<<<<<< Updated upstream
                pygame.time.delay(1000)
                game.playing = False
                game.death_count+=1
                break
=======
>>>>>>> main
                if game.player.shield:
                    self.obstacles.remove(obstacle)
                elif game.life_manager.life_counter() == 1:
                    game.life_manager.delete_life()
<<<<<<< HEAD
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    game.life_manager.delete_life()
                    self.obstacles.remove(obstacle)
=======
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
>>>>>>> main

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []

