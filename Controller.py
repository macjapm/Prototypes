from __future__ import print_function
import pygame
import random
class Controller:

	def __init__(self, model):

		self.model = model

		# create tkinter canvas
		
		return
	def getMouseInput(self):

		position = None

		whichMouse = None

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			pressed = pygame.mouse.get_pressed()

			if pressed[0]:
				whichMouse = 'left'
			elif pressed[2]:
				whichMouse = 'right'

			position = pygame.mouse.get_pos()

			

		if position == None: return
		
		#print(whichMouse, position)

		if whichMouse == 'left':
			self.model.leftClick(position)
		elif whichMouse == 'right':
			self.model.rightClick(position)
			return
