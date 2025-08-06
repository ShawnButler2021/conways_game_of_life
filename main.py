from grid import Grid
from display import CLIDisplay


if __name__ == '__main__':
    rounds = 3
    width, height = 4,4

    gg = Grid(width, height, 0)
    gd = CLIDisplay(width, height)
    
    gg.random_map( 4 )
    gd.print(gg.alive)


    for r in range(rounds):
        print( f'Round {r+1}: ' + str(len(gg.alive)) )
        gg.iterate()
        gd.print(gg.alive)
