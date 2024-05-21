import random

def random_q(mydict):

    questions = []
    for word in mydict:
        questions.append(word)

    num = random.randrange(len(mydict))

    question = questions[num]
    return question