score = 0

print("Welcome to the Quiz!")
print("Let's get started...\n")

# Question 1
print("Q1: What is the capital of India?")
answer = input("Your answer: ").lower()
if answer == "delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 2
print("\nQ2: Who developed Python?")
answer = input("Your answer: ").lower()
if "guido" in answer and "rossum" in answer:
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 3
print("\nQ3: What does CPU stand for?")
answer = input("Your answer: ").lower()
if "central processing unit" in answer:
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nQuiz Over! Your score is:", score, "/ 3")

