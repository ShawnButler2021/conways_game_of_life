
class CLIDisplay:
    def __init__(self, width, height):
        self.width, self.height = width, height

        self.dead_char = '.'
        self.alive_char = '0'

    def print(self, alives):

        map = []
        for _ in range(self.height):
            row = [self.dead_char for _ in range(self.width) ]
            map.append(row)


        for alive in alives:
            x, y = alive
            x = int(x)
            y = int(y)
            map[y][x] = self.alive_char


        for row in map:
            print( ''.join(row) )
        print()

