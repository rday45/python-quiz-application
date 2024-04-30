import random
import rich
import datetime
import time
from rich import print as rprint
from art import *
from all_questions import *


bubble_greeting = text2art("Welcome\nTo\nPython Quiz App")
happy_art = art("yawning")
sad_art = art("dislike2")

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

#Need to add functionality to enable writing to a CSV file 
def play_quiz(selected_quiz):
    randomised_quiz_list = selected_quiz.copy()
    random.shuffle(randomised_quiz_list)
    timestamp = create_timestamp()
    correctly_answered = 0 
    total_questions = len(randomised_quiz_list)
    for question in randomised_quiz_list:
        question.print_question()
        is_correct = question.answer_check()
        if is_correct:
            correctly_answered += 1
            print("")
            rprint(f"[green]That is correct! {happy_art}[/green]")
        else:
            print("")
            rprint(f"[red]That is incorrect! {sad_art}[/red]")

    print(f"you started this quiz on {timestamp}")
    print(f"you correctly answered {correctly_answered} out of {total_questions} questions")



    
    

# --------------  App logic -------------------------

while menu_choice!="6":
    menu_choice = (input(selection_message))
    match menu_choice:
        case "1":
            play_quiz(geography_question_list)
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
            

