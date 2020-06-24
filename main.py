"""
sudoku solving script
"""

from sys import argv

from board import Board




if __name__ == '__main__':
    # for cmd line use, input 81-char string as first arg 

    s = argv[1]

    b = Board(s)

    print()
    print()
    print('Input:')
    print()
    b.show_nicely()
    print()


    if b.solve():
        print('SUCCESS')

        print()
        print('Result:')
        print()
        b.show_nicely()
        print()
    else:
        print('FAILED ... board is unsolvable.')
        print('Board remains unchanged, or empty cells still remain.')
        
        print()
        print('Result:')
        print()
        b.show_nicely()
        print()

