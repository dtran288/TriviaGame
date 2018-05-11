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







