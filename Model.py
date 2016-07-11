import random
from Agent import *
from AI import *
from Player import *
from calc import *

import time

class Model:

	curSelected = []
	score = 0
	limit = 3

	def __init__(self, view, size):

		self.view = view

		self.players = []
		self.AIs = []

		self.size=size

		self.startTime = time.time()

		return

	def getScore(self):
		return self.score

	def getAgents(self):
		return self.players+self.AIs
	
	def leftClick(self, position):


	###Left Click Select and Move Behavior
		for agent in self.players:
			if agent.getSelected():
				agent.setGoalPosition(position)
				return

		for agent in self.players:
			
			found = agent.isAtPosition(position)
			agent.setSelected(found)
			if found:
				self.curSelected = []
				self.curSelected.append(agent)
				

	def rightClick(self, position):



	##Right click deselect behavior
		self.curSelected = []
		for agent in self.players:
			
			found = agent.isAtPosition(position)
			agent.setSelected(found)




	def addAgent(self, grouptype):

		loc = [random.randint(0, self.size[0]),
				random.randint(0, self.size[1])]

		if grouptype == 'player':
			
			agent = Player(self, False, loc)
			self.players.append(agent)

		elif grouptype == 'AI':

			agent = AI(self, False, loc, speed=2)
			self.AIs.append(agent)


		

		
	def step(self):

		for agent in self.players+self.AIs:
			agent.step()

		for agent in (self.players+self.AIs)[::-1]:
			if agent.toDie:
				self.handleDeath(agent)

		self.updateScore('time_step')
		self.updateDifficulty()

		if self.checkAdd():
			self.addAgent('player')


	

	

	def updateDifficulty(self):

		goodPersonSpeed = 5.
		badPersonSpeed = (goodPersonSpeed*self.score/200.0 + 2.*1)/(1 + self.score/200.0)

		for agent in self.AIs:
			agent.speed = max(2, badPersonSpeed)

	def updateScore(self, event):

		if event == 'time_step':
			self.score += 100*0.25/self.view.frame_rate

		elif event == 'death':
			self.score = max(self.score-100., 0)

	def handleDeath(self, agent):

		try:
			self.players.remove(agent)
		except:
			self.AIs.remove(agent)
			
		self.updateScore('death')

	def checkAdd(self):

		if len(self.players) < self.limit:
			return True
		return False