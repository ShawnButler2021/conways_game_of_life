import random
import numpy as np

class Grid:
    def __init__(self, width, height, seed=42):
        self.width = width
        self.height = height
        random.seed(seed)

        self.alive = np.empty( (1,2) )
        self.alive[0] = 0,0
        self.alive = np.delete(self.alive, 0,0)

    def random_map(self, num_to_place=None):
        if not num_to_place:
            num_to_place = random.randint(1, self.width*self.height)

        cell_count = 0
        while cell_count < num_to_place:
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            coord = np.array( [x,y], ndmin=2 )

            if coord not in self.alive:
                self.alive = np.append(self.alive, coord, axis=0)
                cell_count+=1
    
    def remove_cell(self, coord):
        if type(coord) != np.array:
            coord = np.array(coord, ndmin=2 )

        try:
            self.alive = np.delete( self.alive, coord, 0 )
        except ValueError: # cell is dead, therefore can ignore
            pass

    def apply_ruleset(self, conn, coord):
        # true = cell lives
        # false = cell dies
        matches = 0
        try:
            matches = np.any(np.all(self.alive == coord.flatten(), axis=1))
        except ValueError:
            print(matches)

        if conn == 3:
            return True
        elif conn == 2 and matches != 0:
            return True
        elif 2 >= conn >= 0:
            return False
        elif 4 <= conn <= 8:
            return False
        else:
            print( f'Error: {conn} connections' ) 
            return False

    def get_connections(self, coord):
        # use Euclidean distance
        connections = np.array(
            [
                c for c in self.alive
                if np.linalg.norm(coord - c) < 2
            ]
        )
        return len(connections)

    def iterate(self):
        self.alive = np.sort(self.alive)
        alive = []

        for y in range(self.height):
            for x in range(self.width):
                coord = np.array( [x,y], ndmin=2 )

                connections = self.get_connections( coord )
                if self.apply_ruleset( connections, coord ):
                    alive.append( (x,y) )

        self.alive = np.array(alive, ndmin=2 )

