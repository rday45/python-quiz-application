import random
import rich
import datetime
import art

from art import *
from rich import print as rprint

# ---------------- Classes ---------------------------- #

class MultipleChoiceQuestion:
    def __init__(self, question,a,b,c,d,answer):
        self.question = question
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.answer = answer

# ----------------  Variables ------------------------ #
q1 = MultipleChoiceQuestion(
    "What is the capital city of France?",
    "Sydney",
    "Baghdad",
    "Paris",
    "Toulouse",
    "c"
)

q2 = MultipleChoiceQuestion(
    "Which ocean is Samoa found in?",
    "Atlantic Ocean",
    "Pacific Ocean",
    "Indian Ocean",
    "Artic OCean",
    "b"
)

q3 = MultipleChoiceQuestion(
    "How many continents are there on Earth?",
    "7",
    "5",
    "8",
    "10",
    "a"

)

q4 = MultipleChoiceQuestion (
    "What is the surface layer of the earth called?",
    "The crust",
    "The shell",
    "The mantle",
    "The core",
    "a"

)

question_list = [q1,q2,q3,q4]

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



# --------------  App logic -------------------------# 

while menu_choice!="6":
    #menu selection may need to be recreated as a separate function if the assignment requires us to use exceptions to handle errors.
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
    

