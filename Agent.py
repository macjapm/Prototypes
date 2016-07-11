from __future__ import print_function
import pygame
import random

from calc import *

class Agent(object):

	def __init__(self, model, selected, position, vitality=10, speed=5,
				 melee_attack=None, range_attack=None, spirit=None, radius = 10):


		self.model = model

		self.selected = selected
		self.position = position
		self.vitality = vitality
		self.speed = speed
		self.melee_attack = melee_attack
		self.range_attack = range_attack
		self.spirit = spirit
		self.radius = radius


		self.goal_position = self.position

		# when this is true, the agent is removed from the model agents list
		self.toDie = False

	def getPosition(self):
		return self.position
	def setPosition(self, position):
		self.position = position
		

	def setGoalPosition(self, position):
		self.goal_position = position


	def isAtPosition(self, position):

		return dist(self.position, position) <= self.radius

	

	def step(self):

		self.moveTowards((0,0))

	def moveTowards(self, position):

		# move agent at constant speed towards goal
		delta = addVec(self.goal_position, multVec(-1., self.position))
		length = dist((0,0), delta)
		
		if length <= self.radius/2: 
			return
		
		direction = multVec(1./length, delta)
		
		newPos = addVec(self.position, multVec(self.speed, direction))

		self.setPosition(newPos)



	def kill(self):

		self.toDie = True
	
