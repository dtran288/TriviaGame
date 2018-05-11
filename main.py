#First Line

from __future__ import print_function
from question import populate_question_database

if __name__ == '__main__':
    print("GAME STARTS")

    ## Introduction
    print('Hey sucker, here\'s the game')


    ## Get Player's Name
    # player_name = raw_input('Who you?')
    player_name = "Dany"
    num_questions = 2


    ##  Start Game
    print('Start TRIVIA')
    list_of_questions = populate_question_database(num_questions)
    for question in list_of_questions:
        question.display_question()

    ##  End Game
    print('Be GONE,%s !' %player_name)
