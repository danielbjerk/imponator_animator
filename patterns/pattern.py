class Pattern():
	def __init__(self):
		pass

	def get_strength_map(self):
		mapping = dict()
		for diode in self.diodes:
				mapping[self.pos_to_pattern_coords[diode.pos]] = diode.strength
		return mapping

	def set_strength_map(self, mapping):
		coord_to_diode = dict(zip([self.pos_to_pattern_coords[d.pos] for d in self.diodes], self.diodes))
		for coord in mapping:
			coord_to_diode[coord].set_strength(mapping[coord])

	def clear_all_diodes(self):
		for d in self.diodes:
			d.reset_strength()
