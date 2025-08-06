import random


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

            if (x,y) not in self.alive:
                self.alive.append( (x,y) )
                cell_count+=1
    
    def remove_cell(self, coord):
        try:
            self.alive.remove( coord )
        except ValueError: # cell is dead, therefore can ignore
            pass


    def apply_ruleset(self, conn, coord):
        # true = cell lives
        # false = cell dies
        if conn == 3:
            return True
        elif conn == 2 and coord in self.alive:
            return True
        elif conn < 3 and conn >= 0:
            return False
        elif conn > 3 and conn < 9:
            return False
        else:
            print( f'Error: {conn} connections' ) 
            return False
               

    def get_connections(self, x, y):
        x_low, y_low = x-1, y-1
        x_high, y_high = x+1, y+1
        possible = [
            (x_low, y_low),
            (x_low, y),
            (x_low, y_high),
            (x_high, y_low),
            (x_high, y),
            (x_high, y_high),
            (x, y_low),
            (x, y_high)
            ]
        connections = [
            c for c in self.alive
            if c in possible
            ]
        return len(connections)

               


    def iterate(self):
        self.alive.sort()
        alive = []

        for y in range(self.height):
            for x in range(self.width):
                connections = self.get_connections(x,y)
                if self.apply_ruleset( connections, (x,y) ):
                    alive.append( (x,y) )

        self.alive = alive


