class Question:
    def __init__(self, question, options):
        self.question = question
        self.options = options

    def display(self):
        print(self.question)
        for option in self.options:
            print(option)

def load_questions_from_file():
    questions = []
    try:
        with open('C:/Users/DELL/Desktop/quiz/questions.txt', 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 5):
                if i + 4 < len(lines):
                    question_text = lines[i].strip()
                    options = [lines[i+1].strip(), lines[i+2].strip(), lines[i+3].strip(), lines[i+4].strip()]
                    questions.append(Question(question_text, options))
    except (IOError, IndexError) as e:
        print(f"Error loading questions: {e}")
    return questions

def load_answers_from_file():
    answers = []
    try:
        with open('C:/Users/DELL/Desktop/quiz/answers.txt', 'r') as file:
            answers = [line.strip().upper() for line in file.readlines() if line.strip()]
    except IOError as e:
        print(f"Error loading answers: {e}")
    return answers

def save_score_to_file(username, score, total_score):
    try:
        with open('C:/Users/DELL/Desktop/quiz/score.txt', 'a') as file:
            file.write(f"{username}: {score}/{total_score}\n")
    except IOError as e:
        print(f"Error saving score: {e}")

def run_quiz():
    username = input("Enter your name: ").strip()
    questions = load_questions_from_file()
    correct_answers = load_answers_from_file()
    if not questions or not correct_answers or len(questions) != len(correct_answers):
        print("Mismatch or missing data in questions or answers. Exiting quiz.")
        return
    
    score = 0
    total_score = len(questions)
    
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question.question}")
        for option in question.options:
            print(option)
        
        while True:
            answer = input("Your answer (A/B/C/D): ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                break
            print("Invalid input. Please enter A, B, C, or D.")
        
        if i <= len(correct_answers) and answer == correct_answers[i-1]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answers[i-1]}.")
    
    print(f"\nYour final score is: {score}/{total_score}")
    save_score_to_file(username, score, total_score)

def main():
    print("Welcome to the Quiz Game!")
    try:
        run_quiz()
    except KeyboardInterrupt:
        print("\nQuiz interrupted. Goodbye!")
    print("Thank you for playing!")

if __name__ == '__main__':
    main()


