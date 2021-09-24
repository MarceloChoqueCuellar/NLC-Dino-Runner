import pygame

from nlc_dino_runner.components import text_utils
from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.components.obstacles.obstacles import Obstacles
from nlc_dino_runner.components.obstacles.obstaclesManager import ObstaclesManager
<<<<<<< Updated upstream
from nlc_dino_runner.utils.constants import TITLE, ICON, SCREEN_WIDTH, SCREEN_HEIGHT, BG, FPS, SMALL_CACTUS, \
    LARGE_CACTUS
=======
from nlc_dino_runner.components.powerups.power_up_manager import PowerUpManager
from nlc_dino_runner.utils.constants import TITLE, ICON, SCREEN_WIDTH, SCREEN_HEIGHT, BG, FPS, CLOUD, RESET, GAME_OVER, \
    NORMAL_MODE, DARK_MODE
>>>>>>> Stashed changes
from nlc_dino_runner.components.dinosaur import Dinosaur
from nlc_dino_runner.utils.constants import ICON


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.playing = False
        self.x_pos_bg = 0
        self.y_pos_bg = 360
        self.game_speed = 20
        self.player = Dinosaur()
        self.obstacle_manager = ObstaclesManager()
        self.cactusSmall = Cactus(SMALL_CACTUS)
        self.cactusLarge = Cactus(LARGE_CACTUS)
        self.points = 0
        self.running = True
        self.death_count = 0

    def run(self):
        self.obstacle_manager.reset_obstacles()
        self.points = 0
        self.playing = True
<<<<<<< Updated upstream
=======
        self.life_manager.refill_lives()
        self.game_speed = 20
>>>>>>> Stashed changes
        while self.playing:
            self.event()
            self.update()
            self.draw()
       #pygame.quit()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
<<<<<<< Updated upstream
        self.screen.fill((255,255,255))
=======
        if self.points >= 1000:
            self.screen.fill(DARK_MODE)
        else:
            self.screen.fill(NORMAL_MODE)
        self.score()
>>>>>>> Stashed changes
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score()

        pygame.display.update()
        pygame.display.flip()

    def score(self):
        self.points += 1
        if self.points % 100 ==0:
            self.game_speed+= 1
        score_element, score_element_rect = text_utils.get_score_element(self.points)
        self.screen.blit(score_element, score_element_rect)

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))

        self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))

        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (self.x_pos_bg + image_width, self.y_pos_bg))
            self.x_pos_bg= 0
        self.x_pos_bg -= self.game_speed
        self.draw_clouds()

<<<<<<< Updated upstream
    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()
=======
    def draw_clouds(self):    #drawing the clouds
>>>>>>> Stashed changes

    def show_menu(self):
        self.running = True

        white_color= (255, 255, 255)
        self.screen.fill(white_color)

        self.print_menu_elements()

        pygame.display.update()

        self.handle_key_events_on_menu()

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

<<<<<<< Updated upstream
    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT // 2
=======
    def death(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.score()
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.life_manager.draw(self.screen)
        self.game_over()
        pygame.display.update()
        pygame.display.flip()

    def game_over(self):
        self.screen.blit(GAME_OVER, ((SCREEN_WIDTH // 2) - 180, (SCREEN_HEIGHT // 2) - 180))
>>>>>>> Stashed changes

        text, text_rect = text_utils.get_centered_message("Press any key to start")
        self.screen.blit(text, text_rect)

        death_score, death_score_rect = text_utils.get_centered_message("Death count: "+ str(self.death_count), height=half_screen_height + 50)
        self.screen.blit(death_score, death_score_rect)

        self.screen.blit(ICON, ((SCREEN_WIDTH // 2) - 40, half_screen_height - 150))