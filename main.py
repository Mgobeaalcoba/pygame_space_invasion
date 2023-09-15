from service.game_cycle import set_name_and_icon, init_game

def run() -> None:
    """
    The main entry point of the game.

    This function sets the name and icon for the game window and initializes the game.

    :return: None
    """
    set_name_and_icon()
    init_game()
    

if __name__ == '__main__':
    run()
