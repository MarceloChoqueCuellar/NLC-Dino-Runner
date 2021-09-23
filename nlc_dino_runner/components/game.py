import pygame

from nlc_dino_runner.components import text_utils
from nlc_dino_runner.components.life.life_manager import LifeManager
from nlc_dino_runner.components.obstacles.obstaclesManager import ObstaclesManager
from nlc_dino_runner.components.powerups.power_up_manager import PowerUpManager
from nlc_dino_runner.utils.constants import TITLE, ICON, SCREEN_WIDTH, SCREEN_HEIGHT, BG, FPS, CLOUD, RESET
from nlc_dino_runner.components.dinosaur import Dinosaur
import random


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        #clouds
        self.separation = random.randint(350, 450)
        self.x_pos_cloud1 = 0 + self.separation
        self.x_pos_cloud2 = 0 + self.separation * 2
        self.x_pos_cloud3 = 0 + self.separation * 3
        self.x_pos_cloud4 = 0 + self.separation * 4
        self.y_pos_cloud1 = random.randint(100, 250)
        self.y_pos_cloud2 = random.randint(100, 250)
        self.y_pos_cloud3 = random.randint(100, 250)
        self.y_pos_cloud4 = random.randint(100, 250)
        self.separation = 250

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.playing = False
        self.x_pos_bg = 250
        self.y_pos_bg = 360

        self.game_speed = 20
        self.player = Dinosaur()
        self.obstacle_manager = ObstaclesManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.running = True
        self.death_count = 0
        self.life_manager = LifeManager()

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def show_menu(self):
        self.running = True

        white_color = (255, 255, 255)
        self.screen.fill(white_color)

        self.print_menu_elements()

        pygame.display.update()

        self.handle_key_events_on_menu()

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT // 2

        if self.death_count == 0:
            text, text_rect = text_utils.get_centered_message("Press any key to start")
            self.screen.blit(text, text_rect)
        else:
            text, text_rect = text_utils.get_centered_message("Press any key to restart")
            self.screen.blit(text, text_rect)
            # Imprimiendo icono restart
            self.screen.blit(RESET, ((SCREEN_WIDTH // 2) - 40, half_screen_height + 25))

        death_score, death_score_rect = text_utils.get_centered_message(
            "Death count: " + str(self.death_count), height=half_screen_height + 110)
        self.screen.blit(death_score, death_score_rect)

        # Imprimiendo el dinosaurio de la portada
        self.screen.blit(ICON, ((SCREEN_WIDTH // 2) - 40, half_screen_height - 150))

        actual_score, actual_score_rect = text_utils.get_centered_message("Your score: " + str(self.points),
                                                                        height=half_screen_height + 150)
        self.screen.blit(actual_score, actual_score_rect)
        self.screen.blit(death_score, death_score_rect)

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def run(self):
        self.points = 0
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups(self.points, self.player)
        self.playing = True
        self.life_manager.refill_lives()
        while self.playing:
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self, self.points)
        self.power_up_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.score()
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.life_manager.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        score_element, score_element_rect = text_utils.get_score_element(self.points)
        self.screen.blit(score_element, score_element_rect)
        self.player.check_invincibility(self.screen)

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))

        #drawing the track
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

        #drawing the clouds

        self.screen.blit(CLOUD, (self.x_pos_cloud1, self.y_pos_cloud1))
        self.screen.blit(CLOUD, (self.x_pos_cloud2, self.y_pos_cloud2))
        self.screen.blit(CLOUD, (self.x_pos_cloud3, self.y_pos_cloud3))
        self.screen.blit(CLOUD, (self.x_pos_cloud4, self.y_pos_cloud4))
        self.x_pos_cloud1 -= self.game_speed // 2
        self.x_pos_cloud2 -= self.game_speed // 2
        self.x_pos_cloud3 -= self.game_speed // 2
        self.x_pos_cloud4 -= self.game_speed // 2

        if self.x_pos_cloud1 <= -SCREEN_WIDTH//4:
            self.x_pos_cloud1 = SCREEN_WIDTH
            self.y_pos_cloud1 = random.randint(100, 250)

        if self.x_pos_cloud2 <= -SCREEN_WIDTH//4:
            self.x_pos_cloud2 = SCREEN_WIDTH
            self.y_pos_cloud2 = random.randint(100, 250)

        if self.x_pos_cloud3 <= -SCREEN_WIDTH//4:
            self.x_pos_cloud3 = SCREEN_WIDTH
            self.y_pos_cloud3 = random.randint(100, 250)

        if self.x_pos_cloud4 <= -SCREEN_WIDTH//4:
            self.x_pos_cloud4 = SCREEN_WIDTH
            self.y_pos_cloud4 = random.randint(100, 250)



