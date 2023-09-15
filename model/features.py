class ScoreCard:
    def __init__(self) -> None:
        """
        Initialize a scorecard.

        This class is used to keep track of the player's score and control its visibility on the game screen.

        :return: None
        """
        self.visible = True
        self.score = 0
        self.text_x = 10
        self.text_y = 10 


class FinishText:
    def __init__(self) -> None:
        """
        Initialize finish text.

        This class defines the content and position of the "Game Over" text that appears on the screen when the game ends.

        :return: None
        """
        self.content = "Game Over"
        self.text_x = 250
        self.text_y = 250
