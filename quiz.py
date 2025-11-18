import json

def load_questions():
    """Load questions from the JSON file."""
    try:
        with open("questions.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: 'questions.json' file not found!")
        return []

def run_quiz(questions):
    score = 0

    print("\n===== SIMPLE QUIZ APPLICATION =====\n")

    for index, q in enumerate(questions, start=1):
        print(f"Q{index}. {q['question']}")
        
        for i, opt in enumerate(q['options'], start=1):
            print(f"   {i}. {opt}")
        
        while True:
            try:
                user_answer = int(input("Your answer (1-4): "))
                if 1 <= user_answer <= 4:
                    break
                else:
                    print("Please enter a number between 1-4.")
            except ValueError:
                print("Enter a valid number.")

        if user_answer == q["answer"]:
            print("✔ Correct!\n")
            score += 1
        else:
            print(f"✘ Wrong! Correct answer is {q['answer']}: {q['options'][q['answer']-1]}\n")

    print("===== QUIZ COMPLETED =====")
    print(f"Your Score: {score} / {len(questions)}")

def main():
    questions = load_questions()
    if questions:
        run_quiz(questions)

if __name__ == "__main__":
    main()