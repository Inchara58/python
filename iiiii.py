questions = {
    "What is the capital of France? ": "paris",
    "What is 5 + 7? ": "12",
    "Which planet is known as the Red Planet? ": "mars"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question).lower()
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"\nYour final score: {score}/{len(questions)}")
