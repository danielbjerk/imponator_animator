from patterns.pattern import Pattern
from patterns.diode import Diode

class Omega(Pattern):
	def __init__(self, origin=(50,50), width=450, clickable_diodes=True):
		super().__init__()		
		
		# Pattern requires size (450, 450)
		pattern_width = 450
		diode_positions = [
				(350, 300), 
				(250, 300), 
				(100, 300), 
				(0, 300), 
				(250, 250), 
				(100, 250), 
				(300, 200), 
				(50, 200), 
				(320, 150), 
				(20, 150), 
				(300, 80), 
				(50, 80), 
				(250, 30), 
				(100, 30), 
				(200, 0), 
				(150, 0)
				]

		scale_factor = width/pattern_width
		if pattern_width * scale_factor < 50: raise(Exception("Pattern too small!"))
		diode_positions_scaled = [(int(p[0] * scale_factor), int(p[1] * scale_factor)) for p in diode_positions]
		diode_radius = int(40 * scale_factor)
		diode_positions_offset = [(p[0] + origin[0], p[1] + origin[1]) for p in diode_positions_scaled]

		colors = [(0,0,0)] + [(255 - 13*i, 0, 0) for i in range(15)][::-1]
		self.diodes = [
				Diode(  diode_radius, diode_positions_offset[i], 
						colors, clickable_diodes
				) for i in range(len(diode_positions_offset))
				]

		pattern_coordinates = [ # Corresponds to diode-positions
		(0, 1),
		(1, 1),
		(1,0),
		(0,0),
		(2,1),
		(2,0),
		(3,1),
		(3,0),
		(4,1),# 8
		(4,0),
		(5,1),
		(5,0),
		(6,1),# 12
		(6,0),
		(7,1),
		(7,0)
		]
		self.pos_to_pattern_coords = dict(zip(diode_positions_offset, pattern_coordinates))
