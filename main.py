from __future__ import print_function

import pygame

from Model import *
from Controller import *
from View import *

class Game:

	def __init__(self, size, frame_rate=60):

		
		self.size=size
		self.frame_rate = frame_rate

		pygame.init()
		self.surface = pygame.display.set_mode(self.size)
		
		self.running = False

		self.clock = pygame.time.Clock()

		self.view = View(frame_rate=frame_rate)
		self.model = Model(view=self.view, size=self.size)
		self.controller = Controller(self.model)

		self.model.addAgent('AI')

	def play(self):
		self.running = True
		self.run()

	def pause(self):
		self.running = False

	def run(self):


		# TODO: modify play/pause/run interaction to easily 
		#    be able to play/pause the game

		while self.running:

			self.controller.getMouseInput()
			
			self.model.step()
			
			self.view.draw(self.surface, self.model)
			
			self.clock.tick(self.view.frame_rate)
			
			pygame.display.flip()


if __name__ == "__main__":

	G = Game(size=(640, 640))

	G.play()
	
	

	
	



		
