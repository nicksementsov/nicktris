# Basic Controller
from math import sqrt
import gamecommons as gc
import prop

class Controller(object):
	"""Base controller for Nicktris props"""
	def __init__(self, newProp=None):
		super(Controller, self).__init__()
		
		self.ownProp = None
		if (newProp != None):
			self.possess(newProp)
		else:
			self.possess(prop.Prop(True))

		self.impulse = [0.0, 0.0] # X Y

	def possess(self, newProp):
		if (gc.NTDEBUG):
			print("Possessing new prop")
		self.ownProp = newProp

	def dispossess(self):
		self.ownProp = None

	def modHat(self, direction, mod):
		'''Press or release a HAT direction'''
		# 0: North, 1: South, 2: West, 3: East
		if (direction == 0):
			self.impulse[1] += -1.0 * mod
		elif (direction == 1):
			self.impulse[1] += 1.0 * mod

		if (direction == 2):
			self.impulse[0] += -1.0 * mod
		elif (direction == 3):
			self.impulse[0] += 1.0 * mod

	def normImpulse(self):
		'''Normalize impulse vector'''
		newPush = self.impulse.copy()
		if (abs(newPush[0]) == 1.0 and abs(newPush[1]) == 1.0):
			ratio = sqrt(pow(1.0, 2.0) / 2.0)
			newPush[0] *= ratio
			newPush[1] *= ratio
		return newPush

	def applyImpulse(self, frameTime):
		newPush = self.normImpulse()
		self.ownProp.push((newPush[0], newPush[1]), frameTime)
		# X
		'''if (newPush[0] != 0.0):
									self.ownProp.push((newPush[0], 0.0), frameTime)
								else:
									self.ownProp.speed[0] = 0.0
						
								# Y
								if (newPush[1] != 0.0):
									self.ownProp.push((0.0, newPush[1]), frameTime)
								else:
									self.ownProp.speed[1] = 0.0'''

	__applyImpulse = applyImpulse

	def tick(self, frameTime):
		self.applyImpulse(frameTime)

		

