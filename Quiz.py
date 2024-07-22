print("Welcome to the Basic Quiz Game!")
print("Note: If the answer is typed incorrectly, no marks will be given.")

# Initialize variables
marks = 0
ques_no = 0

# Define questions and correct answers
questions = [("What is the latest processor of Snapdragon for Laptop?",
              "Snapdragon X Elite"),
             ("What is the latest processor of Snapdragon for Mobile?",
              "Snapdragon 8 Gen 1"),
             ("What are the latest generations of CPUs offered by Intel?",
              "14th Gen"),
             ("What is the latest version of macOS?", "macOS 14 Sonoma"),
             ("What is the latest version of Windows?", "Windows 11")]

# Start the game
Start_the_game = input("Do you want to start the game? (yes/no): ")
if Start_the_game.lower() == 'yes':
    for question, correct_answer in questions:
        ques_no += 1
        user_answer = input(f"\n{ques_no}. {question}: ")
        if user_answer.lower() == correct_answer.lower():
            marks += 1
            print("Correct! You got 1 mark.")
        else:
            print(f"Incorrect! The correct answer is: {correct_answer}")

    # Calculate percentage
    try:
        percentage = (marks * 100) / ques_no
    except ZeroDivisionError:
        percentage = 0

    print(f"\nNumber of questions attempted: {ques_no}")
    print(f"Your score: {marks}/{ques_no} ({percentage:.2f}% correct)")
else:
    print("Thank you for considering the quiz. Have a great day!")
