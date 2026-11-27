class Question:
    def __init__(self, question, category):
        self.question = question
        self.category = category


class Choice:
    def __init__(self, choice, emotion):
        self.choice = choice
        self.emotion = emotion


class Submission:
    def __init__(self, submission, response):
        self.submission = submission
        self.response = response
