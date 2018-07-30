#
NTDEBUG = True
SCREEN_X = 1280
SCREEN_Y = 720
MAXFPS = 60

# User keybinds by description
USER_KEYS_DES = {	'HAT_N': 119,		# w
					'HAT_S': 115,		# s
					'HAT_W': 97,		# a
					'HAT_E': 100,		# d
					'ESCAPE': 27} 		# ESCAPE

# User keybinds by pygame number
USER_KEYS_NUM = {119:	'HAT_N',		# w
					115:	'HAT_S',	# s
					97:		'HAT_W',	# a
					100:	'HAT_E',	# d
					27:		'ESCAPE'}	# ESCAPE

GAME_COLOURS = {'BLACK'}

class GAME_COLOURS(object):
	"""Default colours and methods for creating new colours"""
	
	def __init__(self):
		super(GAME_COLOURS, self).__init__()
		self.BLACK 	= 0,	 0,		0
		self.GREEN 	= 0,	 255,	0
		self.RED	= 255,	 0,		0
		self.BLUE 	= 0,	 0,		255
		