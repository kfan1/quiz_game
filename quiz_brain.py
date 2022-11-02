class Brain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        answer = input(f'Q{self.question_number+1}. {self.question_list[self.question_number].text} (true/false) ').lower()
        self.question_number += 1
        answer = answer[:1]
        self.check_answer(answer)

    def check_answer(self, answer):
        if answer == self.question_list[self.question_number-1].answer[:1].lower():
            self.score += 1
            print("You got that right!")
            print(f"You got {self.score} out of {self.question_number} correct\n")
        else:
            print("You got that wrong.")
            print(f"You got {self.score} out of {self.question_number} correct\n")
