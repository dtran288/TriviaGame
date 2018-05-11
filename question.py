from __future__ import print_function
import urllib, json

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
        print(self.correct_answer)
        print(self.incorrect_answers)

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





