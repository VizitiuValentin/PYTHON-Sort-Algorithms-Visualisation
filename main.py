import pygame
import random
import sorting_algoriths as alg

pygame.font.init()
pygame.mixer.init()

FPS = 120

WIDTH = 1300
HEIGTH = 650

WINDOW = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Sorting Algorithms Visualisation")

# Menu assets
MENU_BG = pygame.image.load("Assets/menu_bg.png")

BUTTON_HIGHLIGHT = pygame.image.load("Assets/button.png")
BUTTON_HIGHLIGHT.set_alpha(100)

# Sort screen assets
SORT_BG = pygame.image.load("Assets/sorting_screen.png")
FILLER = pygame.image.load("Assets/filler.png")
BACK_TO_MENU = pygame.image.load("Assets/back_to_menu.png")
YELLOW_BUTTON = pygame.Surface((400, 37))
YELLOW_BUTTON.set_alpha(100)
YELLOW_BUTTON.fill((255, 255, 0))

BIP = pygame.mixer.Sound("Assets/bip.wav")

DONE_TEXT = pygame.font.SysFont("Arial", 40)
QUIT_TEXT = pygame.font.SysFont("Arial", 30)


def draw_sorting_screeen(array, comparasions):
    WINDOW.blit(SORT_BG, (0, 0))
    WINDOW.blit(QUIT_TEXT.render("Press here to finish sorting instantly.", True, (255, 255, 255)), (0, 615))
    mouse_x, mouse_y = pygame.mouse.get_pos()

    comp_text = pygame.font.SysFont("ARial", 20)
    text = comp_text.render("Total comparisons: " + str(comparasions) + "   Sorting algorithm: Bubble Sort", False,
                            (255, 255, 255))
    WINDOW.blit(text, (0, 0))

    if mouse_y > 613 and mouse_y < 650 and mouse_x >= 0 and mouse_x < 400:
        WINDOW.blit(YELLOW_BUTTON, (0, 613))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_y > 613 and mouse_y < 650 and mouse_x >= 0 and mouse_x < 400:
                array.sort()

    X = 0
    for number in array:
        LINE = pygame.Surface((5, number * 3))
        LINE.fill((255, 0, 0))
        WINDOW.blit(LINE, (X, 608 - number * 3))  # Will print at the 608 Y coord, minus the length of the line

        X += 7
    pygame.display.update()


def draw_menu(mouse_x, mouse_y):
    pygame.display.update()
    WINDOW.blit(MENU_BG, (0, 0))

    # Open the menu_bg.png file in Paint to see these values easily
    # Algorithm pick buttons
    if mouse_x > 60 and mouse_x < 305 and mouse_y > 108 and mouse_y < 154:
        WINDOW.blit(BUTTON_HIGHLIGHT, (57, 105))
    elif mouse_x > 60 and mouse_x < 305 and mouse_y > 163 and mouse_y < 209:
        WINDOW.blit(BUTTON_HIGHLIGHT, (57, 160))
    elif mouse_x > 60 and mouse_x < 305 and mouse_y > 218 and mouse_y < 264:
        WINDOW.blit(BUTTON_HIGHLIGHT, (57, 215))
    elif mouse_x > 60 and mouse_x < 305 and mouse_y > 273 and mouse_y < 319:
        WINDOW.blit(BUTTON_HIGHLIGHT, (57, 270))
    elif mouse_x > 60 and mouse_x < 305 and mouse_y > 328 and mouse_y < 374:
        WINDOW.blit(BUTTON_HIGHLIGHT, (57, 325))
    elif mouse_x > 60 and mouse_x < 305 and mouse_y > 383 and mouse_y < 429:
        WINDOW.blit(BUTTON_HIGHLIGHT, (57, 380))

    # Animation type
    elif mouse_x > 382 and mouse_x < 628 and mouse_y > 108 and mouse_y < 154:
        WINDOW.blit(BUTTON_HIGHLIGHT, (379, 105))
    elif mouse_x > 382 and mouse_x < 628 and mouse_y > 163 and mouse_y < 209:
        WINDOW.blit(BUTTON_HIGHLIGHT, (379, 160))

    # Start button
    elif mouse_x > 669 and mouse_x < 943 and mouse_y > 108 and mouse_y < 154:
        WINDOW.blit(BUTTON_HIGHLIGHT, (694, 105))


def main():
    array = [i for i in range(1, 187)]
    random.shuffle(array)
    clock = pygame.time.Clock()

    algorithm = 0
    animation_type = 1
    # To check if different parts of the program are done runnning
    running = 1
    menu = 1
    sorting = 1

    WARN_TEXT = pygame.font.SysFont("Arial", 30)
    warning = WARN_TEXT.render("Please select an algorithm first!", True, (255, 0, 0))
    algorithms = {0: "Please select", 1: "Bubble Sort", 2: "Quick Sort", 3: "None", 4: "None", 5: "None", 6: "None"}
    animations = {1: "Show every swap", 2: "Show only once every run"}
    while running:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        while menu:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            draw_menu(mouse_x, mouse_y)

            if mouse_x > 669 and mouse_x < 943 and mouse_y > 108 and mouse_y < 154 and algorithm in (0, 3, 4, 5 ,6):
                WINDOW.blit(warning, (695, 158))
            WINDOW.blit(WARN_TEXT.render("Current settings: ", False, (0, 0, 0)), (0, 650 - 3 * 30 - 15))
            WINDOW.blit(WARN_TEXT.render("Algorithm: " + algorithms[algorithm], True, (0, 0, 0)),
                        (0, 650 - 2 * 30 - 10))
            WINDOW.blit(WARN_TEXT.render("Animation type: " + animations[animation_type], True, (0, 0, 0)),
                        (0, 650 - 40))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse_x > 60 and mouse_x < 305 and mouse_y > 108 and mouse_y < 154:
                        algorithm = 1
                    elif mouse_x > 60 and mouse_x < 305 and mouse_y > 163 and mouse_y < 209:
                        algorithm = 2
                    elif mouse_x > 60 and mouse_x < 305 and mouse_y > 218 and mouse_y < 264:
                        algorithm = 3
                    elif mouse_x > 60 and mouse_x < 305 and mouse_y > 273 and mouse_y < 319:
                        algorithm = 4
                    elif mouse_x > 60 and mouse_x < 305 and mouse_y > 328 and mouse_y < 374:
                        algorithm = 5
                    elif mouse_x > 60 and mouse_x < 305 and mouse_y > 383 and mouse_y < 429:
                        algorithm = 6

                    elif mouse_x > 382 and mouse_x < 628 and mouse_y > 108 and mouse_y < 154:
                        animation_type = 1
                    elif mouse_x > 382 and mouse_x < 628 and mouse_y > 163 and mouse_y < 209:
                        animation_type = 2

                    elif mouse_x > 669 and mouse_x < 943 and mouse_y > 108 and mouse_y < 154 and algorithm not in (0, 3, 4, 5 ,6):
                        menu = 0
                        pygame.display.update()

        # Sorts the list based on the algorithm picked

        print(array)
        if algorithm == 1:
            alg.bubble_sort(array, animation_type)
        if algorithm == 2:
            alg.quick_sort(array, 0, len(array)-1, animation_type, 0)
        print(array)

        done_sort = 1
        while done_sort:
            pygame.font.init()
            text = DONE_TEXT.render("DONE SORTING!", True, (255, 255, 255))
            WINDOW.blit(text, (0, 30))
            WINDOW.blit(BACK_TO_MENU, (0, 80))
            mouse_x, mouse_y = pygame.mouse.get_pos()
            YELLOW = pygame.Surface((252, 52))
            YELLOW.set_alpha(100)
            YELLOW.fill((255, 255, 0))

            if mouse_x > 2 and mouse_x < 250 and mouse_y > 80 and mouse_y < 80 + 50:
                WINDOW.blit(YELLOW, (0, 80))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse_x > 2 and mouse_x < 250 and mouse_y > 80 and mouse_y < 80 + 50:
                        main()
            pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
