class ScoreCard:
    def __init__(self) -> None:
        self.visible = True
        self.score = 0
        self.text_x = 10
        self.text_y = 10 


class FinishText:
    def __init__(self) -> None:
        self.content = "Game Over"
        self.text_x = 250
        self.text_y = 250 