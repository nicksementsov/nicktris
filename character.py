# Character
import prop

class Character(prop.Prop):
	"""Character with acceleration and momentum"""
	def __init__(self, moveable=True, X=0, Y=0, Xs=10, Ys=10, maxSpeed=2.0, acceleration=0.1, deceleration=0.5):
		super(Character, self).__init__(moveable, X, Y, Xs, Ys, maxSpeed)
		self.acceleration = acceleration
		self.deceleration = deceleration

		self.rotation = [1.0, 0.0]
		self.rotSpeed = 0.01

	def push(self, direction, frameTime):
		'''Push an Actor, respecting their acceleration'''
		super(Character, self).push(direction, frameTime)

'''		def apush(aDirection, aFrameTime, axis):
			if (direction[axis] != self.rotation[axis]):
				dirDif = direction[axis] - self.rotation[axis]
				if (abs(dirDif) < 0.005):
					self.rotation[axis] = direction[axis]
				elif (dirDif > 0):
					self.rotation[axis] += self.rotSpeed
				elif (dirDif < 0):
					self.rotation[axis] -= self.rotSpeed
			

			if (aDirection[axis] != 0):
				self.speed[axis] += self.rotation[axis] * self.acceleration
				if (abs(self.speed[axis]) > self.maxSpeed * abs(self.rotation[axis])):
					self.speed[axis] = self.maxSpeed * self.rotation[axis]

		
		apush(direction, frameTime, 0)
		apush(direction, frameTime, 1)'''