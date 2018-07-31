#
NTDEBUG = True
SCREEN_X = 1280
SCREEN_Y = 720
MAXFPS = 60.0

# User keybinds by description
USER_KEYS_DES = {	'HAT_N': 119,		# w
					'HAT_S': 115,		# s
					'HAT_W': 97,		# a
					'HAT_E': 100,		# d
					'ACT_R': 101,
					'ESCAPE': 27} 		# ESCAPE

# User keybinds by pygame number
USER_KEYS_NUM = {119:	'HAT_N',		# w
					115:	'HAT_S',	# s
					97:		'HAT_W',	# a
					100:	'HAT_E',	# d
					101:	'ACT_R',
					27:		'ESCAPE'}	# ESCAPE

CONTR_BINDS = {	119:	0,		# Hat north
				115:	1,		# Hat south
				97:		2,		# Hat west
				100:	3,		# Hat east
				101:	4}		# Action regular

GAME_COLOURS = {'BLACK'}

class GAME_COLOURS(object):
	"""Default colours and methods for creating new colours"""
	
	def __init__(self):
		super(GAME_COLOURS, self).__init__()
		self.BLACK 	= 0,	 0,		0
		self.GREEN 	= 0,	 255,	0
		self.RED	= 255,	 0,		0
		self.BLUE 	= 0,	 0,		255
		self.COLOURS = [self.GREEN, self.BLUE, self.RED, self.BLACK]
		