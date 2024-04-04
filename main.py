from game import Game
import time
game = Game()
game2 = Game()
game.printBoard()
game2.printBoard()
ruch = None
while True:
    #time.sleep(1)
    ruch = game.nextMove(ruch)
    game.printBoard()
    #time.sleep(1)
    ruch = game2.nextMove(ruch)
    game2.printBoard()