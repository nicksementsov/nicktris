# Prop
import gamecommons as gc
from pygame import rect

class Prop(object):
	"""Basic Nicktris class that has presence in the game world"""

	def __init__(self, moveable, X=0, Y=0, Xs=10, Ys=10, maxSpeed=2.0, acceleration=0.2, deceleration=0.5):
		super(Prop, self).__init__()
		self.X = X		# X Position
		self.Y = Y		# Y Position
		self.Xs = Xs	# Width
		self.Ys = Ys	# Height

		self.speed = [0.0, 0.0]
		self.maxSpeed = maxSpeed
		self.acceleration = acceleration

		self.rect = self.makeRect()

	def makeRect(self):
		return rect.Rect(self.X - (self.Xs / 2), self.Y - (self.Ys / 2), 
			self.Xs, self.Ys)

	def getRect(self):
		return self.rect

	def move(self, newLoc):
		self.X += newLoc[0]
		self.Y += newLoc[1]
		self.rect = self.makeRect()

	def push(self, direction, frameTime):
		self.speed[0] += ((direction[0] * self.acceleration) * frameTime)
		if (self.speed[0] > self.maxSpeed):
			self.speed[0] = self.maxSpeed
		elif (self.speed[0] < self.maxSpeed * -1.0):
			self.speed[0] = self.maxSpeed * -1.0

		self.speed[1] += ((direction[1] * self.acceleration) * frameTime)
		if (self.speed[1] > self.maxSpeed):
			self.speed[1] = self.maxSpeed
		elif (self.speed[1] < self.maxSpeed * -1.0):
			self.speed[1] = self.maxSpeed * -1.0

	def slow(self, direction, frameTime):
		self.speed[1]

	def tick(self, frameTime):
		self.move(self.speed)