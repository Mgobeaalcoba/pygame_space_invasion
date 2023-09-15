from random import choice


class Character:

    position_x = 0 
    position_y = 0

    def __init__(self, screen) -> None:
        """
        Initialize a game character.

        :param screen: The game screen surface.
        :type screen: pygame.Surface
        """
        self.screen = screen


class Player(Character):
    
    position_x = 318 
    position_y = 516

    def __init__(self, screen) -> None:
        """
        Initialize the player character.

        :param screen: The game screen surface.
        :type screen: pygame.Surface
        """
        super().__init__(screen)
        self.select_img = './assets/images/nave-player.png'
        self.lives = True

    def move_left(self) -> None:
        """
        Move the player character left.

        :return: None
        """
        if self.position_x >= 0 and self.position_x <= 736:
            self.position_x -= 4
        elif self.position_x > 736:
            self.position_x = 736
        else:
            self.position_x = 0
    
    def move_right(self) -> None:
        """
        Move the player character right.

        :return: None
        """
        if self.position_x >= 0 and self.position_x <= 736:
            self.position_x += 4
        elif self.position_x > 736:
            self.position_x = 736
        else:
            self.position_x = 0
    
    def move_up(self) -> None:
        """
        Move the player character up.

        :return: None
        """
        if self.position_y >= 0 and self.position_y <= 536:
            self.position_y -= 2
        elif self.position_y > 536:
            self.position_y = 536
        else:
            self.position_y = 0

    def move_down(self) -> None:
        """
        Move the player character down.

        :return: None
        """
        if self.position_y >= 0 and self.position_y <= 536:
            self.position_y += 2
        elif self.position_y > 536:
            self.position_y = 536
        else:
            self.position_y = 0


class Enemy(Character):
    # Class variable to store instances
    instances = []

    def __init__(self, screen) -> None:
        """
        Initialize an enemy character.

        :param screen: The game screen surface.
        :type screen: pygame.Surface
        """
        super().__init__(screen)
        self.position_x = choice([32, 128, 224, 320, 416, 512, 608, 704])
        self.position_y = choice([32, 128, 224])
        __enemies_list = [
            "./assets/images/nave-espacial.png",
            "./assets/images/nave-extraterrestre.png",
            "./assets/images/enemigo.png",
            "./assets/images/astronave.png",
            "./assets/images/ovni.png",
            "./assets/images/ovni2.png",
            "./assets/images/ovni3.png"
        ]
        self.select_img = choice(__enemies_list)
        self.moviment_x = 2
        self.moviment_y = 2
        self.lives = True
        Enemy.instances.append(self)

    def move_random_x(self) -> None:
        """
        Move the enemy character randomly in the x-axis.

        :return: None
        """
        if self.position_x >= 0 and self.position_x <= 736:
            self.position_x += choice([-1,1])
        elif self.position_x > 736:
            self.position_x = 736
        else:
            self.position_x = 0

    def move_random_y(self) -> None:
        """
        Move the enemy character randomly in the y-axis.

        :return: None
        """
        if self.position_y >= 0 and self.position_y <= 536:
            self.position_y += choice([-1,1])
        elif self.position_y > 536:
            self.position_y = 536
        else:
            self.position_y = 0

    def standar_move(self) -> None:
        """
        Move the enemy character in a standard pattern.

        :return: None
        """
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

