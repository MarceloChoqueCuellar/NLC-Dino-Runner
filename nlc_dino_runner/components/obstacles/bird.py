from nlc_dino_runner.components.obstacles.obstacles import Obstacles
import random
<<<<<<< HEAD

=======
>>>>>>> main
from nlc_dino_runner.utils.constants import BIRD


class Bird(Obstacles):
    X_POS = 2200

    def __init__(self, image):
        self.type = random.randint(0, 1)
<<<<<<< HEAD
=======

>>>>>>> main
        super().__init__(image, self.type)
        self.rect.x = self.X_POS
        self.rect.y = random.randint(230, 300)
        self.step_index = 0
        self.flying = True

<<<<<<< HEAD
        # while self.flying:
        #     self.image = self.image[self.step_index // 10]
        #     self.step_index += 1
        #     if self.step_index >= 10:
        #         self.step_index = 0
=======
    def fly(self):
        self.obstacle_type = (self.step_index // 5)

        self.step_index += 1
        self.rect.x -= 5
        if self.step_index >= 10:
            self.step_index = 0

>>>>>>> main



