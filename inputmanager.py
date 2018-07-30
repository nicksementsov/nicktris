# Input Manager
from pygame import event, key

import pygamecommons as pgc
import gamecommons as gc
import controller

class InputManager(object):
	"""Manages input for Nicktris game
	   Routes input from pygame events to Nicktris states"""

	def __init__(self):
		super(InputManager, self).__init__()

		self.controllers = []

	def addController(self, newController):
		self.controllers.append(newController)

	def handleInput(self, newEvent, owner=0):
		if (newEvent.type == pgc.KEYDOWN):
			if (newEvent.key in gc.USER_KEYS_NUM.keys()):
				self.pressKey(newEvent)

		elif (newEvent.type == pgc.KEYUP):
			if (newEvent.key in gc.USER_KEYS_NUM.keys()):
				self.releaseKey(newEvent)

	def pressKey(self, newEvent):
		# Quit everything
		if (newEvent.key == gc.USER_KEYS_DES.get('ESCAPE', None)):
			event.post(event.Event(pgc.QUIT))

		# Send a move event to an attached NTController
		elif ('HAT_' in gc.USER_KEYS_NUM.get(newEvent.key, None)):
			if (newEvent.key == 119):
				self.controllers[0].addImpulse((None, -1.0))
			elif (newEvent.key == 115):
				self.controllers[0].addImpulse((None, 1.0))
			elif (newEvent.key == 97):
				self.controllers[0].addImpulse((-1.0, None))
			elif (newEvent.key == 100):
				self.controllers[0].addImpulse((1.0, None))

	def releaseKey(self, newEvent):
		if ('HAT_' in gc.USER_KEYS_NUM.get(newEvent.key, None)):
			if (newEvent.key == 119):
				self.controllers[0].addImpulse((None, 1.0))
			elif (newEvent.key == 115):
				self.controllers[0].addImpulse((None, -1.0))
			elif (newEvent.key == 97):
				self.controllers[0].addImpulse((1.0, None))
			elif (newEvent.key == 100):
				self.controllers[0].addImpulse((-1.0, None))