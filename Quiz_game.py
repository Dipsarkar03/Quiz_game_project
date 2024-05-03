#Quiz game project:
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        for question in self.questions:
            answer = input(question.prompt + ":" + "\n")
            if answer.lower() == question.answer:
                self.score += 1
                print("Correct!")
            else:
                print("Incorrect!")
        print("You got", self.score, "correct answer out of", len(self.questions), "questions.")
        print("So, You got", ((100 * self.score)/len(self.questions)),"% marks out of 100% marks")


question_prompts = [
    "The Holy Scripture The Religion of God is written by? (a) Riaz Ahmed Gohar Shahi, (b) Younus Al Gohar",
    "Who has the prophethood and knowledge of Heart (Qalb)? (a) Adam as. (b) Ibraheem as.",
    "what is the position of the carnal self in the human body? (a) In head (b) Naval point",
    "In which language does Allah speak with Angels? (a) Suryani (b) Arabic",
    "For what reason do humans become impure? (a) Celestial soul, (b) Ethereal soul, (c) Carnal self"
]

answer_list = ['a','a','b','a','c']


if __name__=="__main__":
    print("-------------------------------Quiz Game Start-------------------------------------")
    question_list = []
    score = 0
    counter = 0
    for question in question_prompts:
        question_list.append(Question(question, answer_list[counter]))
        counter += 1

    quiz = Quiz(question_list)
    quiz.run_quiz()





