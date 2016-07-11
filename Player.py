
from Agent import *

class Player(Agent):

	def __init__(self, model, selected, position, vitality=10, speed=5,
				 melee_attack=None, range_attack=None, spirit=None, radius = 10):

		super(Player, self).__init__(model, selected, position, vitality, speed,
				melee_attack, range_attack, spirit, radius)

		self.grouptype = 'player'

		self.normalColour = (150+ random.randint(0, 20), 150+random.randint(0, 20), 255)
		self.selectedColour = (255,255,255)

		self.colour = self.normalColour


	def setSelected(self, value):
		self.selected = value

		self.updateColour()

	def getSelected(self):
		return self.selected

	def step(self):

		# move agent at constant speed towards goal
		self.moveTowards(self.goal_position)

	def updateColour(self):
		if self.selected:
			self.colour = self.selectedColour
		else:
			self.colour = self.normalColour
