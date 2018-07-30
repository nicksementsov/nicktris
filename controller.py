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

	def addImpulse(self, newImpulse):
		if (newImpulse[0] != None):
			self.impulse[0] += newImpulse[0]
		if (newImpulse[1] != None):
			self.impulse[1] += newImpulse[1]

	def tick(self, frameTime):
		if (self.impulse[0] != 0.0):
			self.ownProp.push((self.impulse[0], 0.0), frameTime)
		else:
			self.ownProp.speed[0] = 0.0

		if (self.impulse[1] != 0.0):
			self.ownProp.push((0.0, self.impulse[1]), frameTime)
		else:
			self.ownProp.speed[1] = 0.0

