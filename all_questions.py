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
    #prints the question associated with the object
    def print_question(self):
        print(" ")
        print(f"Question: {self.question}")
        print(" ")
        print(f"A - {self.a}")
        print(f"B - {self.b}")
        print(f"C - {self.c}")
        print(f"D - {self.d}")
        print(" ")
    #checks user answer and returns a value
    def answer_check(self):
        valid_input = False
        while not valid_input:
            user_input = input("Enter A,B,C or D to select an answer or 5 to quit: ").lower()
            if user_input =="5":
                return "quit"
            elif user_input == "a" or user_input == "b" or user_input == "c" or user_input == "d":
                valid_input = True
                if user_input == self.answer:
                    return "correct"
                else:
                    return "incorrect"
            else:
                print("")
                rprint("[yellow]Invalid quiz input. Try again.[/yellow]")
                print("")
    #prints both question and answer for the quiz object
    def print_answer(self):
        question_answer = self.answer.upper()
        rprint(f"[green]The correct answer is: {question_answer}.")


#creates quiz objects
geo1 = MultipleChoiceQuestion(
    "What is the capital city of France?",
    "Sydney",
    "Baghdad",
    "Paris",
    "Toulouse",
    "c"
)

geo2 = MultipleChoiceQuestion(
    "Which ocean is Samoa found in?",
    "Atlantic Ocean",
    "Pacific Ocean",
    "Indian Ocean",
    "Arctic Ocean",
    "b"
)

geo3 = MultipleChoiceQuestion(
    "How many continents are there on Earth?",
    "7",
    "5",
    "8",
    "10",
    "a"
)

geo4 = MultipleChoiceQuestion(
    "What is the surface layer of the earth called?",
    "The crust",
    "The shell",
    "The mantle",
    "The core",
    "a"
)
geo5 = MultipleChoiceQuestion(
    "How many named oceans are found on Earth?",
    "10",
    "4",
    "3",
    "5",
    "b"
)


his1 = MultipleChoiceQuestion(
    "What title belonged to the ruler of Egypt in ancient times?",
    "Lord",
    "Mr",
    "Pharaoh",
    "Emperor",
    "c"
)

his2 = MultipleChoiceQuestion(
    "In which year did the french revolution take place?",
    "1900",
    "2020",
    "1400",
    "1789",
    "d"
)

his3 = MultipleChoiceQuestion(
    "Which person was a prime minister of Australia?",
    "Paul Keating",
    "Billy Bob",
    "John Romero",
    "Tony Stark",
    "a"
)

his4 = MultipleChoiceQuestion(
    "What year marked the start of World War 1?",
    "1914",
    "1980",
    "1900",
    "1918",
    "a"
)

his5 = MultipleChoiceQuestion(
    "Garum was a popular in which society?",
    "Chinese",
    "Egyptian",
    "Russian",
    "Roman",
    "d"
)

#creates list of quiz objects

humanities_quiz = [geo1,his1,geo2,his2,geo3,his3,geo4,his4,geo5,his5]