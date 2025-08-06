import random
import numpy as np


class Grid:
    def __init__(self, width, height, seed=42):
        self.width = width
        self.height = height
        random.seed(seed)

        self.alive = []

    def random_map(self, num_to_place=None):
        if not num_to_place:
            num_to_place = random.randint(1, self.width*self.height)

        cell_count = 0
        while cell_count < num_to_place:
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            coord = (x, y)

            if coord not in self.alive:
                self.alive.append(coord)
                cell_count+=1
    
    def remove_cell(self, coord):
        try:
            self.alive.remove(coord)
        except ValueError: # cell is dead, therefore can ignore
            pass

    def apply_ruleset(self, conn, coord):
        # true = cell lives
        # false = cell dies
        if conn == 3:
            return True
        elif conn == 2 and coord in self.alive:
            return True

        return False

    def get_connections(self, coord):
        # use Euclidean distance
        current_alive = np.array(self.alive, ndmin=2 ).reshape( len(self.alive), 2 )
        coord = np.array(coord, ndmin=2 ).flatten()

        dist = np.linalg.norm(current_alive - coord, axis=1)
        mask = (0 < dist) & (dist < 2)
        connections = len(current_alive[mask])

        return connections

    def iterate(self):
        self.alive.sort()
        alive = []

        for y in range(self.height):
            for x in range(self.width):
                coord = (x,y)

                connections = self.get_connections( coord )
                if self.apply_ruleset( connections, coord ):
                    alive.append( (x,y) )

        self.alive = alive

