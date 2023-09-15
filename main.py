from service.game_cycle import set_name_and_icon, init_game


def run() -> None:
    set_name_and_icon()
    init_game()

    input("Presiona Enter para salir...")



if __name__ == '__main__':
    run()