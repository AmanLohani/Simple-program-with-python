import random

movies = ['John wick', 'Jason borne', 'Fast and furious', 'Mission impossible', 'The purge', 'Infinity saga','Terminator']


def play():
    player1 = input("Player 1 enter your name")
    player2 = input("Player 2 enter your name")
    pp1 = 0
    pp2 = 0
    turn = 0
    willing = True
    while willing:
        if turn % 2 == 0:
            print(player1, ",it is your turn.")
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)

            not_said = True
            while not_said:
                letter = input("Enter letter")
                if (is_present(letter, picked_movie)):
                    modified_qn = unlock(modified_qn, picked_movie, ch)
                    print(modified_qn)
                    d = input("Press 1 to guess the movie or enter 2 to unlock one more letter")
                    if d == 1:

                else:
                    print(letter, " not found")
        else:

        turn = turn + 1


def create_question(movie):
    print(movie)


play()