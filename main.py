import pygame
import time
import random

pygame.init()

# Define display resolution
display_width = 1280
display_height = 960

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
road_color = (150, 170, 130)
dark_cyan = (0, 145, 139)
light_cyan = (0, 195, 189)
light_road_color = (200, 220, 180)

# Define car size
car_width = 100
car_height = 200

# Define road boundaries
road_border_left = display_width / 2 - 300
road_border_right = display_width / 2 + 300 - car_width

# Define obstacles size
obstacle_width = 100
obstacle_height = 200

# Initialise resources and load images
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Race Game')
clock = pygame.time.Clock()
roadImg = pygame.image.load('road.png')
roadImg = pygame.transform.scale(roadImg, (600, display_height))
carImg = pygame.image.load('ambulance.png')
carImg = pygame.transform.scale(carImg, (car_width, car_height))
deco_treeImg = pygame.image.load('decoration_tree.png')
deco_treeImg = pygame.transform.scale(deco_treeImg, (150, 150))
obstacle_yellowImg = pygame.image.load('obstacle_yellow.png')
obstacle_yellowImg = pygame.transform.scale(obstacle_yellowImg, (obstacle_width, obstacle_height))
obstacle_blueImg = pygame.image.load('obstacle_blue.png')
obstacle_blueImg = pygame.transform.scale(obstacle_blueImg, (obstacle_width, obstacle_height))
obstacle_greenImg = pygame.image.load('obstacle_green.png')
obstacle_greenImg = pygame.transform.scale(obstacle_greenImg, (obstacle_width, obstacle_height))
red_overlayImg = pygame.image.load('red_filter.png')
red_overlayImg = pygame.transform.scale(red_overlayImg, (display_width, display_height))
logoImg = pygame.image.load('logo.png')
logoImg = pygame.transform.scale(logoImg, (int(display_width * 0.80), int(display_height * 0.3)))
menu_start_deselected = pygame.image.load('menu_start_deselected.png')
menu_start_deselected = pygame.transform.scale(menu_start_deselected, (int(display_width * 0.21), int(display_height * 0.10)))
menu_start_selected = pygame.image.load('menu_start_selected.png')
menu_start_selected = pygame.transform.scale(menu_start_selected, (int(display_width * 0.21), int(display_height * 0.10)))
menu_scores_deselected = pygame.image.load('menu_scores_deselected.png')
menu_scores_deselected = pygame.transform.scale(menu_scores_deselected, (int(display_width * 0.21), int(display_height * 0.10)))
menu_scores_selected = pygame.image.load('menu_scores_selected.png')
menu_scores_selected = pygame.transform.scale(menu_scores_selected, (int(display_width * 0.21), int(display_height * 0.10)))
menu_quit_deselected = pygame.image.load('menu_quit_deselected.png')
menu_quit_deselected = pygame.transform.scale(menu_quit_deselected, (int(display_width * 0.21), int(display_height * 0.10)))
menu_quit_selected = pygame.image.load('menu_quit_selected.png')
menu_quit_selected = pygame.transform.scale(menu_quit_selected, (int(display_width * 0.21), int(display_height * 0.10)))

obstaclesList = [obstacle_blueImg, obstacle_greenImg, obstacle_yellowImg]

# Draw road decorations according to a changing offset to mimic movements
def road_decorations(offset):
    pygame.draw.rect(gameDisplay, white, [display_width / 2 - 10, -150 + offset, 20, 150])
    pygame.draw.rect(gameDisplay, white, [display_width / 2 - 10, 50 + offset, 20, 150])
    pygame.draw.rect(gameDisplay, white, [display_width / 2 - 10, 250 + offset, 20, 150])
    pygame.draw.rect(gameDisplay, white, [display_width / 2 - 10, 450 + offset, 20, 150])
    pygame.draw.rect(gameDisplay, white, [display_width / 2 - 10, 650 + offset, 20, 150])
    pygame.draw.rect(gameDisplay, white, [display_width / 2 - 10, 850 + offset, 20, 150])

    gameDisplay.blit(deco_treeImg, (display_width / 2 + 320, -100 + offset))
    gameDisplay.blit(deco_treeImg, (display_width / 2 + 320, 100 + offset))
    gameDisplay.blit(deco_treeImg, (display_width / 2 + 320, 300 + offset))
    gameDisplay.blit(deco_treeImg, (display_width / 2 + 320, 500 + offset))
    gameDisplay.blit(deco_treeImg, (display_width / 2 + 320, 700 + offset))
    gameDisplay.blit(deco_treeImg, (display_width / 2 + 320, 900 + offset))

    gameDisplay.blit(deco_treeImg, (display_width / 2 - 470, -150 + offset))
    gameDisplay.blit(deco_treeImg, (display_width / 2 - 470, 50 + offset))
    gameDisplay.blit(deco_treeImg, (display_width / 2 - 470, 250 + offset))
    gameDisplay.blit(deco_treeImg, (display_width / 2 - 470, 450 + offset))
    gameDisplay.blit(deco_treeImg, (display_width / 2 - 470, 650 + offset))
    gameDisplay.blit(deco_treeImg, (display_width / 2 - 470, 850 + offset))

def obstacle(x, y, obstacle_img):
    gameDisplay.blit(obstacle_img, (x, y))

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeFont = pygame.font.Font('freesansbold.ttf', 120)
    TextSurf, TextRect = text_objects(text, largeFont)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(red_overlayImg, (0, 0))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def crash(final_score):
    message_display('You Crashed!')
    score_font = pygame.font.Font('freesansbold.ttf', 70)
    text_surface = score_font.render('Score: {:d}'.format(final_score), True, red)
    text_rect = text_surface.get_rect()
    text_rect.center = ((display_width / 2), (display_height / 2 + 200))
    gameDisplay.blit(text_surface, text_rect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def main_menu():

    menu_items = [menu_start_deselected, menu_scores_deselected, menu_quit_deselected]
    menu_item = 0

    menu_pos1 =((display_width / 2) - (display_width * 0.28 / 2), display_height / 2)
    menu_pos2 = ((display_width / 2) - (display_width * 0.28 / 2), display_height / 2 + display_height * 0.12)
    menu_pos3 = ((display_width / 2) - (display_width * 0.28 / 2), display_height / 2 + display_height * 0.24)

    in_main_menu = True

    while in_main_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and menu_item != 2:
                    menu_item += 1
                if event.key == pygame.K_UP and menu_item != 0:
                    menu_item -= 1
                if event.key == pygame.K_RETURN:
                    if menu_item == 0: game_loop()
                    elif menu_item == 2:
                        pygame.quit()
                        quit()


        if (menu_item == 0):
            menu_items[0] = menu_start_selected
            menu_items[1] = menu_scores_deselected
            menu_items[2] = menu_quit_deselected
        elif (menu_item == 1):
            menu_items[0] = menu_start_deselected
            menu_items[1] = menu_scores_selected
            menu_items[2] = menu_quit_deselected
        elif (menu_item == 2):
            menu_items[0] = menu_start_deselected
            menu_items[1] = menu_scores_deselected
            menu_items[2] = menu_quit_selected

        gameDisplay.fill(light_cyan)
        gameDisplay.blit(logoImg, ((display_width / 2) - (display_width * 0.80 / 2), display_height / 10))
        gameDisplay.blit(menu_items[0], menu_pos1)
        gameDisplay.blit(menu_items[1], menu_pos2)
        gameDisplay.blit(menu_items[2], menu_pos3)
        pygame.display.update()
        clock.tick(15)


def game_loop():
    x = (display_width * 0.50 - (car_width / 2))
    y = (display_height * 0.95 - car_height)

    left_movement = 0
    right_movement = 0

    obstacle_x = random.randrange(road_border_left, (road_border_right - obstacle_width))
    obstacle_y = -600
    obstacle_speed = 10
    obstacle_img = random.choice(obstaclesList)

    speed_increase = 0

    score = 0

    road_decorations_offset = 0

    gameExit = False
    while not gameExit:

        # Handle window close event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Handle arrow key events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left_movement = 15
                elif event.key == pygame.K_RIGHT:
                    right_movement = 15

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_movement = 0

                elif event.key == pygame.K_RIGHT:
                    right_movement = 0

        # Change car position in accordance with arrow key events
        x_change = right_movement - left_movement

        if (x + x_change) < road_border_left:
            x_change = 0
        elif (x + x_change) > road_border_right:
            x_change = 0
        else:
            x += x_change


        gameDisplay.fill(dark_cyan)
        gameDisplay.blit(roadImg, ((display_width / 2) - 300, 0))
        road_decorations(road_decorations_offset)
        road_decorations_offset += 5 + speed_increase
        if (road_decorations_offset > 200):
            road_decorations_offset = 0

        obstacle(obstacle_x, obstacle_y, obstacle_img)
        obstacle_y += obstacle_speed + speed_increase

        # Continuously generate random obstacles
        if obstacle_y > (display_height):
            obstacle_y = -300
            obstacle_x = random.randrange(road_border_left, road_border_right)
            obstacle_img = random.choice(obstaclesList)
            score += 1

            # Progressively increase speed to a maximum
            if speed_increase < 10:
                speed_increase += 0.7

        car(x, y)

        # Collision Handling
        if (y + 10) < (obstacle_y + obstacle_height) and (y + car_height) > (obstacle_y + 10):
            if (x + car_width) > (obstacle_x + 10) and (x + 10) < (obstacle_x + obstacle_width):
                crash(score)

        pygame.display.update()
        clock.tick(120)

main_menu()
pygame.quit()
quit()
