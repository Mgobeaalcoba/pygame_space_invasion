import pygame
from random import choice
from model.characters import Player, Enemy, Character
from model.weapons import Shot, ShotPlayer, Explosion
from model.features import ScoreCard, FinishText
from .convert_to_byte import font_to_bytes


def init_game() -> None:
    """
    Initialize and run the game loop.

    This function initializes the Pygame library, sets up the game window, creates game objects, and runs the main game loop.

    :return: None
    """
    pygame.init()

    screen: pygame.surface = pygame.display.set_mode((800, 600))

    running = True

    player_1 = Player(screen)

    for i in range(20):
        Enemy(screen)

    for i in range(10):
        ShotPlayer(-100, -100)

    explosion_1 = Explosion(-100, -100)

    shot_selection = 0

    score_card = ScoreCard()
    font_as_bytes = font_to_bytes("./assets/fonts/MIDELTONEROUGH.ttf")
    font: pygame.font = pygame.font.Font(font_as_bytes, 32)

    pygame.mixer.music.load("./assets/sounds/MusicaFondo.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    final_text = FinishText()
    font_as_bytes = font_to_bytes("./assets/fonts/MIDELTONEROUGH.ttf")
    final_font: pygame.font = pygame.font.Font(font_as_bytes, 96)

    game_finish = False

    while running:
        screen.fill((205, 144, 228))
        wall_image = pygame.image.load("./assets/images/fondo_juego.jpg")
        wall_game = pygame.transform.scale(wall_image, (800, 600))
        screen.blit(wall_game, (0, 0))
        show_score(font, score_card, screen)

        if game_finish:
            end_game(final_font, final_text, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_1.move_left()
                    for enemy in Enemy.instances:
                        choice([enemy.move_random_x(), enemy.move_random_y()])
                elif event.key == pygame.K_RIGHT:
                    player_1.move_right()
                    for enemy in Enemy.instances:
                        choice([enemy.move_random_x(), enemy.move_random_y()])
                elif event.key == pygame.K_UP:
                    player_1.move_up()
                    for enemy in Enemy.instances:
                        choice([enemy.move_random_x(), enemy.move_random_y()])
                elif event.key == pygame.K_DOWN:
                    player_1.move_down()
                    for enemy in Enemy.instances:
                        choice([enemy.move_random_x(), enemy.move_random_y()])
                elif event.key == pygame.K_SPACE:
                    shot_sound = pygame.mixer.Sound("./assets/sounds/disparo.mp3")
                    shot_sound.play()
                    make_shot(screen, player_1, ShotPlayer.instances[shot_selection])
                    if shot_selection < 9:
                        shot_selection += 1
                    else:
                        shot_selection = 0

        make_character(screen, player_1)

        for enemy in Enemy.instances:
            if enemy.lives:
                make_character(screen, enemy)
                enemy.standar_move()

            if enemy.position_y > 400:
                for enemy_2 in Enemy.instances:
                    enemy_2.lives = False
                game_finish = True
                break

        for shot in ShotPlayer.instances:
            if shot.position_x >= 0 and shot.position_y >= 0 and shot.exists:
                shot.move_up()
                reprint_shot(screen, shot)
                for enemy in Enemy.instances:
                    distance = calculate_distance(shot.position_x, shot.position_y, enemy.position_x, enemy.position_y)
                    if distance <= 500:
                        collision_sound = pygame.mixer.Sound("./assets/sounds/Golpe.mp3")
                        collision_sound.play()
                        explosion_1.position_x = enemy.position_x
                        explosion_1.position_y = enemy.position_y
                        enemy.position_x = -100
                        enemy.position_y = -100
                        enemy.lives = False
                        score_card.score += 100

        pygame.display.update()


def end_game(font: pygame.font, final_text: FinishText, screen: pygame.surface) -> None:
    """
    Display the final text on the screen when the game is over.

    :param font: The font to use for the final text.
    :param final_text: The text to display when the game is over.
    :param screen: The game screen surface.
    :return: None
    """
    text = font.render(f"{final_text.content}", True, (255, 255, 255))
    screen.blit(text, (final_text.text_x, final_text.text_y))


def set_name_and_icon() -> None:
    """
    Set the game window's title and icon.

    :return: None
    """
    pygame.display.set_caption("Space Invasion")
    icon = pygame.image.load("./assets/images/invasion-espacial.png")
    pygame.display.set_icon(icon)


def make_character(screen: pygame.surface, character: Character) -> None:
    """
    Display a character on the game screen.

    :param screen: The game screen surface.
    :param character: The character to display.
    :return: None
    """
    img_character = pygame.image.load(character.select_img)
    screen.blit(img_character, (character.position_x, character.position_y))


def make_shot(screen: pygame.surface, character: Character, shot: Shot) -> None:
    """
    Display a shot on the game screen.

    :param screen: The game screen surface.
    :param character: The character firing the shot.
    :param shot: The shot to display.
    :return: None
    """
    shot.position_x = character.position_x + 16
    shot.position_y = character.position_y - 40
    img_shot = pygame.image.load(shot.select_img)
    screen.blit(img_shot, (shot.position_x, shot.position_y))


def reprint_shot(screen: pygame.surface, shot: Shot) -> None:
    """
    Redraw a shot on the game screen.

    :param screen: The game screen surface.
    :param shot: The shot to redraw.
    :return: None
    """
    img_shot = pygame.image.load(shot.select_img)
    screen.blit(img_shot, (shot.position_x, shot.position_y))


def calculate_distance(position_x_1, position_y_1, position_x_2, position_y_2) -> float:
    """
    Calculate the distance between two points.

    :param position_x_1: The x-coordinate of the first point.
    :param position_y_1: The y-coordinate of the first point.
    :param position_x_2: The x-coordinate of the second point.
    :param position_y_2: The y-coordinate of the second point.
    :return: The distance between the two points.
    :rtype: float
    """
    return ((position_x_2 - position_x_1) ** 2 + (position_y_2 - position_y_1) ** 2) ** 0.5


def show_score(font: pygame.font, score_card: ScoreCard, screen: pygame.surface) -> None:
    """
    Display the player's score on the game screen.

    This function renders the player's score on the game screen using the specified font and position.

    :param font: The font to use for rendering the score.
    :param score_card: The object containing the player's score information.
    :param screen: The game screen surface.
    :return: None
    """
    text = font.render(f"Score: {score_card.score}", True, (255, 255, 255))
    screen.blit(text, (score_card.text_x, score_card.text_y))

