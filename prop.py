# Prop
import gamecommons as gc
from pygame import rect

class Prop(object):
	"""Basic Nicktris class that has presence in the game world"""

	def __init__(self, moveable, X=0, Y=0, Xs=10, Ys=10, maxSpeed=2.0):
		super(Prop, self).__init__()
		self.X = X		# X Position
		self.Y = Y		# Y Position
		self.Xs = Xs	# Width
		self.Ys = Ys	# Height

		self.speed = [0.0, 0.0]
		self.maxSpeed = maxSpeed
		self.rect = self.makeRect()

	def makeRect(self):
		self.rect = None
		return rect.Rect(self.X - (self.Xs / 2), self.Y - (self.Ys / 2), 
			self.Xs, self.Ys)

	def getRect(self):
		return self.rect

	def move(self):
		newLoc = self.speed.copy()
		self.X += newLoc[0]
		self.Y += newLoc[1]
		self.rect = self.makeRect()

	def push(self, direction, frameTime):
		'''Push an Actor, forcing them to move at max speed next tick'''
		self.speed = [direction[0] * self.maxSpeed, direction[1] * self.maxSpeed]

	__push = push

	def slow(self, direction, frameTime):
		self.speed[1]

	def tick(self, frameTime):
		self.move()