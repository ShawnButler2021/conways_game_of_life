from grid import Grid
from display import CLIDisplay


if __name__ == '__main__':
    rounds = 1000
    width, height = 50, 50

    gg = Grid(width, height, 0)
    gd = CLIDisplay(width, height)
    
    gg.random_map( width*height/2 )


    for r in range(rounds):
        print( f'Round {r+1}: ' + str(len(gg.alive)) )
        gg.iterate()
        gd.print(gg.alive)
