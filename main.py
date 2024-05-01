import random
import rich
import datetime
import time
import os.path
import csv
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

def writedata(file,data1,data2,data3):
    with open(file, "a") as f:
        writer = csv.writer(f)
        writer.writerow([data1,data2,data3])


def play_quiz(selected_quiz):
    
    randomised_quiz_list = selected_quiz.copy()
    random.shuffle(randomised_quiz_list)
    timestamp = create_timestamp()
    start_time = time.time()
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

    end_time = time.time()
    session_duration = end_time-start_time
    rounded_duration = round(session_duration,1)
    percentage_correct = (correctly_answered/total_questions)*100
    writedata(file_name,timestamp,percentage_correct,rounded_duration)
    rprint(f"[blue]You started this quiz on {timestamp}[/blue]")
    rprint(f"[blue]You correctly answered {correctly_answered} out of {total_questions} questions[/blue]")
    rprint(f"[blue]That means you got {percentage_correct}% correct[/blue]")
    rprint(f"[blue]The quiz took you {rounded_duration} seconds[/blue]")


file_name = "data.csv"
if (not os.path.isfile(file_name)):
    created_file = open(file_name, "w")
    created_file.write("date,percentage correct,session duration\n")
    created_file.close()


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
            print("Goodbye!")
        case _:
            rprint("[yellow]Invalid menu input. Try again.[/yellow]")
            

