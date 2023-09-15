import pygame
from random import choice
from model.characters import Player, Enemy, Character
from model.weapons import Shot, ShotPlayer, Explotion
from model.features import ScoreCard, FinishText
from .convert_to_byte import font_to_bytes


def init_game() -> None:
    # Inicializo a pygame en nuestro programa
    pygame.init()

    ## Establezco el tamaño de nuestro pantalla
    pantalla : pygame.surface = pygame.display.set_mode((800, 600)) # 800 de ancho y 600 de ancho

    ## Programo que sucede frente al evento QUIT que es el presionar en la X de nuestra pantalla
    se_ejecuta = True

    ## Declaracion del jugador: 
    player_1 = Player(pantalla) 

    ## Declaracion de los enemigos:
    for i in range(20): # 20 enemigos guardas en el atributo instances de la clase
        Enemy(pantalla)

    ## Declaracion de la bala del jugador:
    for i in range(10): # 10 balas creadas en el atributo instances de la clase
        ShotPlayer(-100,-100)

    ## Declaración de la explosion
    explosion_1 = Explotion(-100,-100)
    
    ## Declaro un puntero para ir iterando la creación inicial de mis balas
    shot_selection = 0

    ## Declaro mi variable puntaje donde iré llevando la cuenta de los puntos acumulados en el juego
    score_card = ScoreCard()
    font_as_bytes = font_to_bytes("./assets/fonts/MIDELTONEROUGH.ttf")
    font : pygame.font = pygame.font.Font(font_as_bytes, 32) # Único tipo de fuente que pygame trae por defecto. Se pueden importar otros
    
    ## Agregar musica de fondo:
    pygame.mixer.music.load("./assets/sounds/MusicaFondo.mp3")
    pygame.mixer.music.set_volume(0.3) # Regula el volumen con un numero del 0 al 1. Por default es 1
    pygame.mixer.music.play(-1) # Es para que se vuelva a repetir cuando termina

    ## Declaro mi texto final para cuando concluya el juego
    final_text = FinishText() 
    font_as_bytes = font_to_bytes("./assets/fonts/MIDELTONEROUGH.ttf")
    final_font : pygame.font = pygame.font.Font(font_as_bytes, 96) 

    ## Declaro variable de juego finalizado:
    game_finish = False

    # Loop central del juego
    ## Mostramos la pantalla para que la vea el usuario hasta que aprete en la X
    while se_ejecuta:

        ### Modifico el color de fondo de mi pantalla
        pantalla.fill((205, 144, 228)) # Escala RGB para setear color de fondo de mi pantalla 
        ### Cargo la imagen que voy a usar de fonde de mi juego
        wall_image = pygame.image.load("./assets/images/fondo_juego.jpg")
        ### Transformo el tamaño de mi imagen usando el metodo scale de la clase transform
        wall_game = pygame.transform.scale(wall_image, (800, 600))
        ### Enciendo el fonde dentro de cada iteración de mi juego. 
        pantalla.blit(wall_game, (0,0))
        ### Muestro el score_card
        show_score(font, score_card, pantalla)

        if game_finish:
            end_game(final_font, final_text, pantalla)

        ### Reviso cada uno de los eventos que existen en la nomenclatura de Pygame
        for evento in pygame.event.get():
            ### Si el evento es un evento QUIT entonces cambio el valor booleano de mi variable se_ejecuta
            if evento.type == pygame.QUIT:
                se_ejecuta = False

            ### Si el evento es un evento de KEYDOWN (Tecla presionada):
            if evento.type == pygame.KEYDOWN:
                #### Si la tecla es la de izquierda:
                if evento.key == pygame.K_LEFT:
                    player_1.move_left()
                    for enemy in Enemy.instances:
                        choice([enemy.move_random_x(), enemy.move_random_y()])
                #### Si la tecla es la de derecha:
                elif evento.key == pygame.K_RIGHT:
                    player_1.move_right()
                    for enemy in Enemy.instances:
                        choice([enemy.move_random_x(), enemy.move_random_y()])
                #### Si la tecla es la de arriba:
                elif evento.key == pygame.K_UP:
                    player_1.move_up()
                    for enemy in Enemy.instances:
                        choice([enemy.move_random_x(), enemy.move_random_y()])
                #### Si la tecla es la de abajo:
                elif evento.key == pygame.K_DOWN:
                    player_1.move_down()
                    for enemy in Enemy.instances:
                        choice([enemy.move_random_x(), enemy.move_random_y()])
                elif evento.key == pygame.K_SPACE:
                    shot_sound = pygame.mixer.Sound("./assets/sounds/disparo.mp3")
                    shot_sound.play()
                    make_shot(pantalla, player_1, ShotPlayer.instances[shot_selection])
                    if shot_selection < 9:
                        shot_selection += 1
                    else:
                        shot_selection = 0

        ### Pinto al jugador en la pantalla:
        make_character(pantalla, player_1)
        ### Pinto a los enemigos en la pantalla: 
        for enemy in Enemy.instances:
            if enemy.lives:
                make_character(pantalla, enemy)
                enemy.standar_move()

            # Perder el juego
            if enemy.position_y > 400:
                for enemy_2 in Enemy.instances:
                    enemy_2.lives = False  
                game_finish = True
                break

        ### Pinto a las balas y las muevo si el valor no es negativo
        for shot in ShotPlayer.instances:
            if shot.position_x >= 0 and shot.position_y >= 0 and shot.exists:
                shot.move_up()
                reprint_shot(pantalla, shot)
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

        ### Actualizo la pantalla para que se vean nuestras novedades
        pygame.display.update()


def end_game(font: pygame.font, final_text: FinishText, pantalla: pygame.surface) -> None:
    text = font.render(f"{final_text.content}", True, (255, 255, 255))
    pantalla.blit(text, (final_text.text_x, final_text.text_y))


def set_name_and_icon() -> None:
    # Personalizar la pantalla de pygame
    ## Titulo e icono:
    pygame.display.set_caption("Invasión Espacial")
    icono = pygame.image.load("./assets/images/invasion-espacial.png")
    pygame.display.set_icon(icono)


def make_character(pantalla: pygame.surface, character: Character) -> None:
    img_character = pygame.image.load(character.select_img)
    pantalla.blit(img_character, (character.position_x, character.position_y))


def make_shot(pantalla: pygame.surface, character: Character, shot: Shot) -> None:
    shot.position_x = character.position_x + 16
    shot.position_y = character.position_y - 40
    img_shot = pygame.image.load(shot.select_img)
    pantalla.blit(img_shot, (shot.position_x, shot.position_y))


def reprint_shot(pantalla: pygame.surface, shot: Shot) -> None:
    img_shot = pygame.image.load(shot.select_img)
    pantalla.blit(img_shot, (shot.position_x, shot.position_y))


def calculate_distance(position_x_1, position_y_1, position_x_2, position_y_2) -> float:
    return ((position_x_2 - position_x_1)**2 + (position_y_2 - position_y_1)**2) ** 1/2


def show_score(font: pygame.font, score_card: ScoreCard, pantalla: pygame.surface):
    text = font.render(f"Puntaje: {score_card.score}", True, (255, 255, 255))
    pantalla.blit(text, (score_card.text_x, score_card.text_y))
