import quiz_brain
from question_model import Question
from data import question_data


question_bank = []
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))
    # this feels unnecessary to make a class for something so simple, can just be:
    # question_bank.append(question_data[i])
    # and the print will be print(question_bank[x]["text"]) instead of print(question_bank[x].text) but I guess it's just good practice


# x = random.randint(0, len(question_bank))
# print(question_bank[x].text)

quiz1 = quiz_brain.Brain(question_bank)


while quiz1.still_has_questions():
    quiz1.next_question()
