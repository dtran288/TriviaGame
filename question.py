from __future__ import print_function
from random import shuffle
import urllib, json, copy

class Question:

    def __init__(self, question, correct_answer, incorrect_answers):
        """
        This is the initialization function of the class Question

        :param question: a string that contains the question
        :param correct_answer: a string of the correction asnwer
        :param incorrect_answers: a list of strings of incorrect answers
        """
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers


    def display_question(self):
        """Prints Question"""
        print(self.question)

        # oldList orders responses first with correct answer, then incorrect answers
        old_list = copy.copy(self.incorrect_answers)
        old_list.extend([self.correct_answer])
        print('OLD LIST:')
        print(old_list)

        new_list = copy.copy(old_list)
        shuffle(new_list)
        print('NEW LIST:')
        print(new_list)

        #Forloop new_list display
        for x in range(len(new_list)):
            if x == 0:
                print('A '+ new_list[x])
            if x == 1:
                print('B '+ new_list[x])
            if x == 2:
                print('C '+ new_list[x])
            if x == 3:
                print('D '+ new_list[x])

        #Gather user input, A, B, C, D integer values
        input = raw_input("What is your answer? ")
        num = int(input)

        if old_list[3] == new_list[num]:
            print('Winner winner, chicken dinner!')
        else:
            print('GTFO!')



def populate_question_database(num_questions):
    """
    Fetches data from the url, turns it into Question objects and returns it as a list
    User can specify the number of questions through the argument num_questions
    """
    assert type(num_questions) is int
    assert num_questions < 11
    assert num_questions > 1

    # Get question database API from the url
    url = "https://opentdb.com/api.php?amount=" + str(num_questions) + "&type=multiple"
    response = urllib.urlopen(url)
    # This will be a dictionary with results being key that points to the list of dictionary of questions
    question_db = json.loads(response.read())

    list_of_questions = [] # initialize the empty list of questions
    # Read through all questions and create a Question object for each of them
    for question_dict in question_db['results']:
        question = question_dict['question']
        correct_answer = question_dict['correct_answer']
        incorrect_answers = question_dict['incorrect_answers']

        list_of_questions.append(Question(question, correct_answer, incorrect_answers))

    return list_of_questions





