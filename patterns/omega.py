from patterns.diode import Diode

class Omega():
    def __init__(self):
        first_color = (0, 0, 0)
        self.strength_to_color = [first_color] + [(105 + 20*i, 0, 0) for i in range(15)]

        diode_poses = [
                (10, 10),
                (300, 300)
                ]
        pattern_coords = [
                (0, 0),
                (8, 1)
                ]
        self.diodes = [Diode(diode_poses[i], pattern_coords[i]) for i in range(2)]#16)]

