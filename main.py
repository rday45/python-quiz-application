import random
import rich
import datetime
import art

from art import *
from rich import print as rprint

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

while menu_choice!="6":
    #menu selection may need to be recreated as a separate function if the assignment requires us to use exceptions to handle errors.
    menu_choice = (input(selection_message))
    

