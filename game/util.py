class Box:
	box = {corner: chr(ord_) for corner, ord_ in {
		'top left': 9556, 'top right': 9559,
		'bottom left': 9562, 'bottom right': 9565,
		'horizontal': 9552, 'vertical': 9553
	}.items()}

	@staticmethod
	def encapsulate(text: str, pad_x: int = 1, pad_y: int = 0) -> str:
		text = text.split('\n')

		width = max(map(lambda line_: len(line_), text)) + pad_x * 2

		spaces_above_below = \
			'' if not pad_y else pad_y * (Box.box['vertical'] + ' ' * width + Box.box['vertical'] + '\n')
		spaces_left_right = ' ' * pad_x

		# Top line
		res = ''  # Box.box['top left'] + Box.box['horizontal'] * width + Box.box['top right'] + '\n'

		# Spaces above
		res += spaces_above_below

		# Content
		for line in text:
			res += Box.box['vertical'] + spaces_left_right
			res += line + ' ' * (width - pad_x * 2 - len(line))
			res += spaces_left_right + Box.box['vertical'] + '\n'

		# Spaces below
		res += spaces_above_below

		# Bottom line
		res += Box.box['bottom left'] + Box.box['horizontal'] * width + Box.box['bottom right']

		return res
