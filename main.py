import pygame
from checkers.constents import WIDTH, HEIGHT,SQUARE_SIZE,BLACK,WHITE  #import consent variable
from checkers.game import Game
from minimax.algorithm import minimax

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers') #name of game

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main(): #the actuall game tha have the event loop
    start = True #open game
    clock = pygame.time.Clock() # keeps track of time
    game = Game(WIN)


    while start:
        clock.tick(60) # update the clock

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 2, WHITE, game)
            game.ai_move(new_board)

        if game.winner() !=None:
            print(game.winner())
            start=False

        for event in pygame.event.get(): # collects all events that happend at a current time
            if event.type == pygame.QUIT: # this means terminate all events when we click exits
                start = False # close game
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                row,col = get_row_col_from_mouse(pos)
                game.select(row,col)

        game.update()

    pygame.quit()

main()