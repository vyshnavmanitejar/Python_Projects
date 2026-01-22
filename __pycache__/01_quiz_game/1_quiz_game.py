print("Enter to the Quiz game!")

playing = input("Do you want to play? (yes/no): ")

if playing.lower() != 'yes':
    print("May be next time!")
    exit()

def quiz_game():
    name = input("Enter your full name: ")
    count = 0

    while True:
        answer = input("""What is python programming language?\nOptions:\n\ta) A type of snake\n\tb) A programming language\n\tc) A general term for coding\n\td) A kind of coffee\n""")
        if answer.lower() == 'b':
            count += 1

        answer = input("""Which of these are data types in python?\nOptions:\n\ta) Integer, String, Float, Boolean\n\tb) Bist, Dict\n\tc) Dict, Int\n\td) Bool, List\n""")
        if answer.lower() == 'a':
            count += 1

        answer = input('''Which of these are data structures in python?\nOptions:\n\ta) List, Tuple, Set, Dictionary\n\tb) Array, Stack\n\tc) Queue, Tree\n\td) Graph, Hashmap\n''')
        if answer.lower() == 'a':
            count += 1

        answer = input('''What is class in python?\nOptions:\n\ta) A Keyword\n\tb) A function\n\tc) A variable\n\td) A blueprint for creating object\n''')
        if answer.lower() == 'd':
            count += 1

        answer = input('''What is an object in python?\nOptions:\n\ta) A function\n\tb) An instance of a class\n\tc) A variable\n\td) A method\n''')
        if answer.lower() == 'b':
            count += 1

        break
    return name, count

name, count = quiz_game()
print("Congractulations!\nYou have completed the quiz!")
print(f"{name}\n{(count/5)*100}%")