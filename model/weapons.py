class Shot:
    def __init__(self, position_x, position_y) -> None:
        """
        Initialize a shot.

        This class represents a shot object with a specified position.

        :param position_x: The x-coordinate of the shot.
        :param position_y: The y-coordinate of the shot.
        :return: None
        """
        self.position_x = position_x
        self.position_y = position_y


class ShotPlayer(Shot):
    instances = []
    def __init__(self, position_x, position_y) -> None:
        """
        Initialize a player's shot.

        This class represents a shot fired by the player. It inherits from the Shot class and includes additional attributes.

        :param position_x: The x-coordinate of the shot.
        :param position_y: The y-coordinate of the shot.
        :return: None
        """
        super().__init__(position_x, position_y)
        self.select_img = "./assets/images/bala_player.png"
        self.exists = True
        self.instances.append(self)

    def move_up(self):
        """
        Move the player's shot upward.

        :return: None
        """
        self.position_y -= 4


class ShotEnemy(Shot):
    def __init__(self, position_x, position_y) -> None:
        """
        Initialize an enemy's shot.

        This class represents a shot fired by an enemy. It inherits from the Shot class and includes additional attributes.

        :param position_x: The x-coordinate of the shot.
        :param position_y: The y-coordinate of the shot.
        :return: None
        """
        super().__init__(position_x, position_y)
        self.select_img = "./assets/images/bala_enemy.png"

    def move_up(self):
        """
        Move the enemy's shot upward.

        :return: None
        """
        self.position_y -= 2

class Explotion(Shot):
    def __init__(self, position_x, position_y) -> None:
        """
        Initialize an explosion.

        This class represents an explosion object at a specified position. It inherits from the Shot class and includes
        additional attributes.

        :param position_x: The x-coordinate of the explosion.
        :param position_y: The y-coordinate of the explosion.
        :return: None
        """
        super().__init__(position_x, position_y)
        self.select_img = "./assets/images/explosion.png"
