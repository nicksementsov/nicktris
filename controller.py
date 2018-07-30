# Controller
import gamecommons as gc
import prop

class Controller(object):
	"""Base controller for Nicktris props"""
	def __init__(self, newProp=None):
		super(Controller, self).__init__()
		self.ownProp = None
		if (newProp != None):
			self.possess(newProp)

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

	def tick(self, frameTime):
		if (self.impulse[0] != 0.0):
			self.ownProp.push((self.impulse[0], 0.0), frameTime)
		else:
			self.ownProp.speed[0] = 0.0

		if (self.impulse[1] != 0.0):
			self.ownProp.push((0.0, self.impulse[1]), frameTime)
		else:
			self.ownProp.speed[1] = 0.0

