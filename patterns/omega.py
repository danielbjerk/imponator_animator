from patterns.diode import Diode

class Omega():
    def __init__(self):

        diode_poses = [
                (80, 80),
                (300, 300)
                ]
        pattern_coords = [
                (0, 0),
                (8, 1)
                ]
        self.pos_to_pattern = dict(zip(diode_poses, pattern_coords))

        colors = [(0,0,0)] + [(255 - 13*i, 0, 0) for i in range(15)]
        self.diodes = [Diode(40, diode_poses[i], colors) for i in range(2)]#16)]

