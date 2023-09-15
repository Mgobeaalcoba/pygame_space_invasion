from random import choice


class Character:

    position_x = 0 
    position_y = 0

    def __init__(self, screen) -> None:
        self.screen = screen


class Player(Character):
    
    position_x = 318 
    position_y = 516

    def __init__(self, screen) -> None:
        super().__init__(screen)
        self.select_img = './assets/images/nave-player.png'
        self.lives = True

    def move_left(self) -> None:
        if self.position_x >= 0 and self.position_x <= 736:
            self.position_x -= 4
        elif self.position_x > 736:
            self.position_x = 736
        else:
            self.position_x = 0
    
    def move_right(self) -> None:
        if self.position_x >= 0 and self.position_x <= 736:
            self.position_x += 4
        elif self.position_x > 736:
            self.position_x = 736
        else:
            self.position_x = 0
    
    def move_up(self) -> None:
        if self.position_y >= 0 and self.position_y <= 536:
            self.position_y -= 2
        elif self.position_y > 536:
            self.position_y = 536
        else:
            self.position_y = 0

    def move_down(self) -> None:
        if self.position_y >= 0 and self.position_y <= 536:
            self.position_y += 2
        elif self.position_y > 536:
            self.position_y = 536
        else:
            self.position_y = 0


class Enemy(Character):
    # Variable de clase para almacenar las instancias
    instances = []

    def __init__(self, screen) -> None:
        super().__init__(screen)
        self.position_x = choice([32, 128, 224, 320, 416, 512, 608, 704])
        self.position_y = choice([32, 128, 224])
        __enemies_list = ["./assets/images/nave-espacial.png", "./assets/images/nave-extraterrestre.png", "./assets/images/enemigo.png", "./assets/images/astronave.png", "./assets/images/ovni.png", "./assets/images/ovni2.png", "./assets/images/ovni3.png"]
        self.select_img = choice(__enemies_list)
        self.moviment_x = 2
        self.moviment_y = 2
        self.lives = True
        Enemy.instances.append(self)

    def move_random_x(self) -> None:
        if self.position_x >= 0 and self.position_x <= 736:
            self.position_x += choice([-1,1])
        elif self.position_x > 736:
            self.position_x = 736
        else:
            self.position_x = 0

    def move_random_y(self) -> None: 
        if self.position_y >= 0 and self.position_y <= 536:
            self.position_y += choice([-1,1])
        elif self.position_y > 536:
            self.position_y = 536
        else:
            self.position_y = 0

    def standar_move(self) -> None:
        if self.position_x >= 0 and self.position_x <= 736:
            self.position_x += self.moviment_x
        elif self.position_x >= 736:
            self.moviment_x *= -1
            self.position_x += self.moviment_x
            self.position_y += 16
        else:
            self.moviment_x *= -1
            self.position_x += self.moviment_x
            self.position_y += 16

