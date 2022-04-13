import pygame, sys
import button
#create display window
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Εταιρία Ρεύματος')

#load button images
zenith_img = pygame.image.load('zenith.webp').convert_alpha()
elpedison_img = pygame.image.load('elpedison.webp').convert_alpha()
iron_img = pygame.image.load('iron.webp').convert_alpha()
dei_img = pygame.image.load('dei.webp').convert_alpha()
fysiko_img = pygame.image.load('fisiko.png').convert_alpha()
volton_img = pygame.image.load('volton.webp').convert_alpha()
protergia_img = pygame.image.load('protergia.webp').convert_alpha()
voltera_img = pygame.image.load('voltera.png').convert_alpha()
wattvolt_img = pygame.image.load('wattvolt.jpg.png').convert_alpha()
nrg_img = pygame.image.load('nrg.jpg.png').convert_alpha()

#create button instances
zenith = button.Button(100, 200, zenith_img, 1.25)
elpedison = button.Button(450, 200, elpedison_img, 0.35)
iron = button.Button(100, 600, iron_img, 0.35)
dei = button.Button(800,200, dei_img, 0.7)
fysiko = button.Button(1500, 600, fysiko_img, 0.6)
volton = button.Button(450, 600, volton_img, 0.35)
wattvolt = button.Button(800, 600, wattvolt_img, 0.35)
voltera = button.Button(1180, 600, voltera_img, 0.42)
nrg = button.Button(1500, 200, nrg_img, 0.78)
protergia = button.Button(1150, 200, protergia_img, 0.28)

#game loop
run = True
while run:
	screen.fill((8,8,8))
	if zenith.draw(screen):
		zenith = button.Button(800, 100, zenith_img, 1.25)
		elpedison = button.Button(450, 20000, elpedison_img, 0.35)
		iron = button.Button(100, 6000, iron_img, 0.35)
		dei = button.Button(800, 2000, dei_img, 0.7)
		fysiko = button.Button(1500, 6000, fysiko_img, 0.6)
		volton = button.Button(450, 6000, volton_img, 0.35)
		wattvolt = button.Button(800, 6000, wattvolt_img, 0.35)
		voltera = button.Button(1180, 6000, voltera_img, 0.42)
		nrg = button.Button(1500, 2000, nrg_img, 0.78)
		protergia = button.Button(1150, 2000, protergia_img, 0.28)
	if elpedison.draw(screen):
		zenith = button.Button(10000, 20000, zenith_img, 1.25)
		elpedison = button.Button(800,100, elpedison_img, 0.35)
		iron = button.Button(100, 6000, iron_img, 0.35)
		dei = button.Button(800, 2000, dei_img, 0.7)
		fysiko = button.Button(1500, 6000, fysiko_img, 0.6)
		volton = button.Button(450, 6000, volton_img, 0.35)
		wattvolt = button.Button(800, 6000, wattvolt_img, 0.35)
		voltera = button.Button(1180, 6000, voltera_img, 0.42)
		nrg = button.Button(1500, 2000, nrg_img, 0.78)
		protergia = button.Button(1150, 2000, protergia_img, 0.28)
	if iron.draw(screen):
		zenith = button.Button(10000, 20000, zenith_img, 1.25)
		elpedison = button.Button(450, 20000, elpedison_img, 0.35)
		iron = button.Button(800, 100, iron_img, 0.35)
		dei = button.Button(800, 2000, dei_img, 0.7)
		fysiko = button.Button(1500, 6000, fysiko_img, 0.6)
		volton = button.Button(450, 6000, volton_img, 0.35)
		wattvolt = button.Button(800, 6000, wattvolt_img, 0.35)
		voltera = button.Button(1180, 6000, voltera_img, 0.42)
		nrg = button.Button(1500, 2000, nrg_img, 0.78)
		protergia = button.Button(1150, 2000, protergia_img, 0.28)
	if dei.draw(screen):
		zenith = button.Button(100, 20000, zenith_img, 1.25)
		elpedison = button.Button(450, 20000, elpedison_img, 0.35)
		iron = button.Button(100, 6000, iron_img, 0.35)
		dei = button.Button(800, 100, dei_img, 0.7)
		fysiko = button.Button(1500, 6000, fysiko_img, 0.6)
		volton = button.Button(450, 6000, volton_img, 0.35)
		wattvolt = button.Button(800, 6000, wattvolt_img, 0.35)
		voltera = button.Button(1180, 6000, voltera_img, 0.42)
		nrg = button.Button(1500, 2000, nrg_img, 0.78)
		protergia = button.Button(1150, 2000, protergia_img, 0.28)
	if fysiko.draw(screen):
		zenith = button.Button(100, 2000, zenith_img, 1.25)
		elpedison = button.Button(450, 20000, elpedison_img, 0.35)
		iron = button.Button(100, 6000, iron_img, 0.35)
		dei = button.Button(800, 2000, dei_img, 0.7)
		fysiko = button.Button(800, 100, fysiko_img, 0.6)
		volton = button.Button(450, 6000, volton_img, 0.35)
		wattvolt = button.Button(800, 6000, wattvolt_img, 0.35)
		voltera = button.Button(1180, 6000, voltera_img, 0.42)
		nrg = button.Button(1500, 2000, nrg_img, 0.78)
		protergia = button.Button(1150, 2000, protergia_img, 0.28)
	if volton.draw(screen):
		zenith = button.Button(100, 2000, zenith_img, 1.25)
		elpedison = button.Button(450, 20000, elpedison_img, 0.35)
		iron = button.Button(100, 6000, iron_img, 0.35)
		dei = button.Button(800, 2000, dei_img, 0.7)
		fysiko = button.Button(1500, 6000, fysiko_img, 0.6)
		volton = button.Button(800, 100, volton_img, 0.35)
		wattvolt = button.Button(800, 6000, wattvolt_img, 0.35)
		voltera = button.Button(1180, 6000, voltera_img, 0.42)
		nrg = button.Button(1500, 2000, nrg_img, 0.78)
		protergia = button.Button(1150, 2000, protergia_img, 0.28)
	if voltera.draw(screen):
		zenith = button.Button(100, 2000, zenith_img, 1.25)
		elpedison = button.Button(450, 20000, elpedison_img, 0.35)
		iron = button.Button(100, 6000, iron_img, 0.35)
		dei = button.Button(800, 2000, dei_img, 0.7)
		fysiko = button.Button(1500, 6000, fysiko_img, 0.6)
		volton = button.Button(450, 6000, volton_img, 0.35)
		wattvolt = button.Button(800, 6000, wattvolt_img, 0.35)
		voltera = button.Button(800, 100, voltera_img, 0.42)
		nrg = button.Button(1500, 2000, nrg_img, 0.78)
		protergia = button.Button(1150, 2000, protergia_img, 0.28)
	if nrg.draw(screen):
		zenith = button.Button(100, 2000, zenith_img, 1.25)
		elpedison = button.Button(450, 20000, elpedison_img, 0.35)
		iron = button.Button(100, 6000, iron_img, 0.35)
		dei = button.Button(800, 2000, dei_img, 0.7)
		fysiko = button.Button(1500, 6000, fysiko_img, 0.6)
		volton = button.Button(450, 6000, volton_img, 0.35)
		wattvolt = button.Button(800, 6000, wattvolt_img, 0.35)
		voltera = button.Button(1180, 6000, voltera_img, 0.42)
		nrg = button.Button(800, 100, nrg_img, 0.78)
		protergia = button.Button(1150, 2000, protergia_img, 0.28)
	if wattvolt.draw(screen):
		zenith = button.Button(100, 2000, zenith_img, 1.25)
		elpedison = button.Button(450, 20000, elpedison_img, 0.35)
		iron = button.Button(100, 6000, iron_img, 0.35)
		dei = button.Button(800, 2000, dei_img, 0.7)
		fysiko = button.Button(1500, 6000, fysiko_img, 0.6)
		volton = button.Button(450, 6000, volton_img, 0.35)
		wattvolt = button.Button(800, 100, wattvolt_img, 0.35)
		voltera = button.Button(1180, 6000, voltera_img, 0.42)
		nrg = button.Button(1500, 2000, nrg_img, 0.78)
		protergia = button.Button(1150, 2000, protergia_img, 0.28)
	if protergia.draw(screen):
		zenith = button.Button(100, 2000, zenith_img, 1.25)
		elpedison = button.Button(450, 20000, elpedison_img, 0.35)
		iron = button.Button(100, 6000, iron_img, 0.35)
		dei = button.Button(800, 2000, dei_img, 0.7)
		fysiko = button.Button(1500, 6000, fysiko_img, 0.6)
		volton = button.Button(450, 6000, volton_img, 0.35)
		wattvolt = button.Button(800, 6000, wattvolt_img, 0.35)
		voltera = button.Button(1180, 6000, voltera_img, 0.42)
		nrg = button.Button(1500, 2000, nrg_img, 0.78)
		protergia = button.Button(800, 100, protergia_img, 0.28)

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()