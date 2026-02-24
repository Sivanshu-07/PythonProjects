<<<<<<< HEAD
import json

# Load questions from the json file
with open("questions.json","r") as file:
    data = json.load(file)

score = 0
question = data["questions"]

for q in question :
    print(f"\nQ{q["id"]}.{q["question"]}")

    for key,value in q["options"].items():
        print(f'{key}.{value}')

    user_ans = int(input("Enter your answer"))

    if user_ans == q["correct_answer"]:
        print("✅ Correct")
        score += 1
    else:
        print("❌ Wrong")
        print(f"Correct answer was option {q['correct_answer']}")

# Final score
print(f"\nYour final score: {score}/{len(question)}")

=======
import json

# Load questions from the json file
with open("questions.json","r") as file:
    data = json.load(file)

score = 0
question = data["questions"]

for q in question :
    print(f"\nQ{q["id"]}.{q["question"]}")

    for key,value in q["options"].items():
        print(f'{key}.{value}')

    user_ans = int(input("Enter your answer"))

    if user_ans == q["correct_answer"]:
        print("✅ Correct")
        score += 1
    else:
        print("❌ Wrong")
        print(f"Correct answer was option {q['correct_answer']}")

# Final score
print(f"\nYour final score: {score}/{len(question)}")

>>>>>>> e0d4995 (Added Personal Expense Tracker Project)
