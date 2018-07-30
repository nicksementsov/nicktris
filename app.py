import sys
import pygame

import prop
import inputmanager
import controller
import gamecommons as gc

size = width, height = 1280, 720

def drawArrow(arrowRect, colour=(255, 0, 0)):
	arrowSurface = pygame.Surface((arrowRect.width, arrowRect.height),
		pygame.HWSURFACE | pygame.SRCALPHA)

	pygame.draw.line(arrowSurface,
		colour,
		((arrowRect.width / 2) - (arrowRect.width / 3), arrowRect.height / 2),
		((arrowRect.width / 2) + (arrowRect.width / 3), arrowRect.height / 2))

	pygame.draw.line(arrowSurface,
		colour,
		(arrowRect.width / 2, (arrowRect.height / 2 - (arrowRect.height / 3))),
		(arrowRect.width / 2, (arrowRect.height / 2 + (arrowRect.height / 3))))

	return arrowSurface


def drawText(vFont, vText, vColour):
	renderedText = vFont.render(vText, True, vColour)
	textRect = renderedText.get_rect()
	return (renderedText, textRect)

if __name__ == '__main__':
	# Pygame setup
	pygame.init()
	gameScreen = pygame.display.set_mode((gc.SCREEN_X, gc.SCREEN_Y),
		pygame.HWSURFACE | pygame.DOUBLEBUF)

	pygame.display.set_caption("Nicktris")
	gameClock = pygame.time.Clock()

	# Debug stuff
	if (gc.NTDEBUG):
		print("Nicktris in debug mode")
		DEBUG_FONT = pygame.font.SysFont(None, 24)

	# Game setup
	GAME_COLOURS = gc.GAME_COLOURS()

	playerOne = prop.Prop(True, 25, 360, 10, 30)
	playerController = controller.Controller(playerOne)

	inMan = inputmanager.InputManager()
	inMan.addController(playerController)

	gameActors = [playerOne]
	gameControllers = [playerController]

	# TODO Joystick setup

	# TODO Sound setup


	# Start loop
	frameTime = 0
	TOQUIT = False
	while not TOQUIT:
		frameTime = gameClock.tick(gc.MAXFPS)
		for event in pygame.event.get():

			# We're out
			if event.type == pygame.QUIT:
				if (gc.NTDEBUG):
					print("Quitting")
				TOQUIT = True

			# Keep checking events
			else:	
				# User pressed a joystick button
				# TODO Handle joystick input

				# User pressed a key
				if event.type in (pygame.KEYDOWN, pygame.KEYUP):
					inMan.handleInput(event)

		# Keep running
		gameScreen.fill(GAME_COLOURS.BLACK)

		for gameController in gameControllers:
			gameController.tick(frameTime)

		for actor in gameActors:
			actor.tick(frameTime)


		#****************************************************
		# Draw debug stuff
		if (gc.NTDEBUG):
			debugText = drawText(DEBUG_FONT, 
				"D " + str(int(gameClock.get_fps())),
				GAME_COLOURS.GREEN)

			debugText[1].left = 1
			debugText[1].top = 1
			gameScreen.blit(debugText[0], debugText[1])

			for actor in gameActors:
				pygame.draw.rect(gameScreen,
					GAME_COLOURS.GREEN,
					actor.getRect(),
					1)
				arrowSurface = drawArrow(actor.getRect())
				gameScreen.blit(arrowSurface, actor.getRect())
		#****************************************************


		pygame.display.flip()

	pygame.quit()
	sys.exit()
