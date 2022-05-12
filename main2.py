import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("background.png")

def get_font(size):
    return pygame.font.Font("font .ttf", size)

def zenith():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        zenith_img=pygame.image.load('zenith.webp')

        PLAY_TEXT = get_font(25).render("", True, "white")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(1220, 700),
                           text_input="BACK", font=get_font(25), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def hron():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        OPTIONS_TEXT = get_font(45).render("", True, "white")
        HRON_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, HRON_RECT)

        OPTIONS_BACK = Button(image=None, pos=(1220, 700),
                              text_input="BACK", font=get_font(25), base_color="white", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        ZENITH_BUTTON = Button(image=pygame.image.load("zenith.webp"), pos=(130, 130),
                             text_input="" , font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        HRON_BUTTON = Button(image=pygame.image.load("HRON.png"), pos=(400, 130),
                                text_input="", font=get_font(5), base_color="#d7fcd4", hovering_color="White")
        for button in [ZENITH_BUTTON, HRON_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ZENITH_BUTTON.checkForInput(MENU_MOUSE_POS):
                    zenith()
                if HRON_BUTTON.checkForInput(MENU_MOUSE_POS):
                    hron()

        pygame.display.update()


main_menu()