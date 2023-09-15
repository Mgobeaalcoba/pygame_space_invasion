
class Shot:
    def __init__(self, position_x, position_y) -> None:
        self.position_x = position_x
        self.position_y = position_y


class ShotPlayer(Shot):
    instances = []
    def __init__(self, position_x, position_y) -> None:
        super().__init__(position_x, position_y)
        self.select_img = "./assets/images/bala_player.png"
        self.exists = True
        self.instances.append(self)

    def move_up(self):
        self.position_y -= 4


class ShotEnemy(Shot):
    def __init__(self, position_x, position_y) -> None:
        super().__init__(position_x, position_y)
        self.select_img = "./assets/images/bala_enemy.png"

    def move_up(self):
        self.position_y -= 2

class Explotion(Shot):
    def __init__(self, position_x, position_y) -> None:
        super().__init__(position_x, position_y)
        self.select_img = "./assets/images/explosion.png"