import random
import rich
import datetime
from rich import print as rprint
from art import *
from all_questions import *



bubble_greeting = text2art("Welcome\nTo\nPython Quiz App")

selection_message = """
Enter 1 to play quiz
Enter 2 to add a question
Enter 3 to delete a question
Enter 4 to view play history
Enter 5 to clear play history
Enter 6 to quit

Enter a number: """


rprint(f"[magenta]{bubble_greeting}[/magenta]") 

menu_choice ="none"

#--------------- functions --------------------------#

def create_timestamp():
    current_time = datetime.datetime.now()
    timestamp = f"{current_time.day}-{current_time.month}-{current_time.year} {current_time.hour}:{current_time.minute}:{current_time.second}"
    return timestamp

#This needs to be completed    
def play_quiz(selected_quiz):
    randomised_quiz_list = selected_quiz.copy()
    random.shuffle(randomised_quiz_list)
    timestamp = create_timestamp()
    correctly_answered = 0 
    total_questions = len(randomised_quiz_list)
    for question in randomised_quiz_list:
        question.print_question()

    
    

# --------------  App logic -------------------------

while menu_choice!="6":
    menu_choice = (input(selection_message))
    match menu_choice:
        case "1":
            print("Game is playing")
        case "2":
            print("Adding a question")
        case "3":
            print("deleting a question")
        case "4":
            print("viewing play history")
        case "5":
            print("clearing play history")
        case "6":
            print("goodbye")
        case _:
            print("that was an invalid selection. Try again.")
            
