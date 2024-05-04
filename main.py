
#imports all required packages and or libraries 
import random
import rich
import datetime
import time
import os.path
import csv
import plotext
from rich import print as rprint
from art import *
from all_questions import *


bubble_greeting = text2art("Welcome\nTo\nPython Quiz App")
happy_art = art("yawning")
sad_art = art("dislike2")

selection_message = """
Enter 1 to play quiz
Enter 2 to display all questions and answers
Enter 3 to view play history
Enter 4 to clear play history
Enter 5 to quit

Enter a number: """


#--------------- functions --------------------------#
#creates a time stamp in an easy to understand Australian format
def create_timestamp():
    current_time = datetime.datetime.now()
    timestamp = f"{current_time.day}-{current_time.month}-{current_time.year} {current_time.hour}:{current_time.minute}:{current_time.second}"
    return timestamp

#This function is used to create a file to store play history data at launch if one does not already exist. It's also used to clear play history data.
def create_new_file(file):
    created_file = open(file, "w")
    created_file.write("date,percentage correct,session duration\n")
    created_file.close()



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

#This function displays the users play history as a multi column graph. Error handling occurs through exceptions if no data is present.
def display_play_history():
    play_history = open('data.csv','r')
    file = csv.DictReader(play_history)
    session_dates = []
    percentages = []
    durations = []
    for col in file:
        session_dates.append(col['date'])
        percentages.append(col['percentage correct'])
        durations.append(col['session duration'])
    play_history.close()
    percentages_as_number = [eval(i) for i in percentages]
    durations_as_number = [eval(i) for i in durations]
    try:
        plotext.simple_multiple_bar(session_dates, [percentages_as_number, durations_as_number], width = 100, labels = ['% Of Answers Correct', 'Session Duration in Seconds'])
        print("────────────────────────────────────────── Play History ────────────────────────────────────────────")
        plotext.show()
    except IndexError:
        rprint("[yellow]Cannot display play history - no data found![/yellow]")
    except:
        rprint("[yellow]Cannot display play history - something went wrong![/yellow]")

def display_all_answers(quiz_list):
    for question in quiz_list:
        question.print_question()
        question.print_answer()


# --------------  App logic -------------------------

rprint(f"[magenta]{bubble_greeting}[/magenta]") 

file_name = "data.csv"

if (not os.path.isfile(file_name)):
    create_new_file(file_name)


menu_choice = "none"

while menu_choice!="5":
    menu_choice = (input(selection_message))
    match menu_choice:
        case "1":
            play_quiz(humanities_quiz)
        case "2":
            display_all_answers(humanities_quiz)
        case "3":
            display_play_history()
        case "4":
            create_new_file(file_name)
            rprint("[blue]Your play history has been cleared[/blue]")
        case "5":
            print("Goodbye")
        case _:
            rprint("[yellow]Invalid menu input. Try again.[/yellow]")
            








