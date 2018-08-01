# TrisController
import controller

class TrisController(controller.Controller):
	"""Subclass of controller for Nicktris game"""
	def __init__(self, newProp=None):
		super(TrisController, self).__init__(newProp)

		self.jumpTime = 500
		self.jumpTimer = 0.0
		self.jumpingTime = 0.0
		self.startedJump = False
		self.canJump = False

	def applyImpulse(self, frameTime):
		self.jumpTimer += frameTime

		if (self.jumpTimer >= self.jumpTime):
			self.jumpTimer = 0.0
			self.ownProp.speed = [self.impulse[0] * 32, self.impulse[1] * 32]
		else:
			self.ownProp.speed = [0.0, 0.0]