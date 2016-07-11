
from Agent import *

class AI(Agent):

	def __init__(self, model, selected, position, vitality=10, speed=2,
				 melee_attack=None, range_attack=None, spirit=None, radius = 10):

		super(AI, self).__init__(model, selected, position, vitality, speed,
				melee_attack, range_attack, spirit, radius)

		self.grouptype = 'AI'

		self.colour = (100,0,0)

	def step(self):

		# if the agent is an AI, we need to calculate it's goal position

		# go towards nearest player character

		nearestAgent = None
		shortestDist = float('inf')
		for agent in self.model.players:
	
			distance = dist(agent.getPosition(), self.getPosition())
			if distance <= shortestDist:
				nearestAgent = agent
				shortestDist = distance

		if nearestAgent != None:
			self.setGoalPosition(nearestAgent.getPosition())

			if shortestDist <= nearestAgent.radius + self.radius:
				nearestAgent.kill()


		# move agent at constant speed towards goal
		self.moveTowards(self.goal_position)


