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
    
    def print_question(self):
        print(" ")
        print(f"Question: {self.question}")
        print(" ")
        print(f"A - {self.a}")
        print(f"B - {self.b}")
        print(f"C - {self.c}")
        print(f"D - {self.d}")
        print(" ")
    
    def answer_check(self):
        valid_input = False
        while not valid_input:
            user_input = input("Enter A,B,C or D: ").lower()
            if user_input == "a" or user_input == "b" or user_input == "c" or user_input == "d":
                valid_input = True
                if user_input == self.answer:
                    return True
                else:
                    return False
            else:
                print("")
                rprint("[yellow]Invalid quiz input. Try again.[/yellow]")
                print("")
    
    def print_answer(self):
        print(" ")
        question_answer = self.answer.upper()
        rprint(f"[green]The correct answer is: {question_answer}.")


# ----------------  Variables ------------------------ #
g1 = MultipleChoiceQuestion(
    "What is the capital city of France?",
    "Sydney",
    "Baghdad",
    "Paris",
    "Toulouse",
    "c"
)

g2 = MultipleChoiceQuestion(
    "Which ocean is Samoa found in?",
    "Atlantic Ocean",
    "Pacific Ocean",
    "Indian Ocean",
    "Arctic Ocean",
    "b"
)

g3 = MultipleChoiceQuestion(
    "How many continents are there on Earth?",
    "7",
    "5",
    "8",
    "10",
    "a"

)

g4 = MultipleChoiceQuestion (
    "What is the surface layer of the earth called?",
    "The crust",
    "The shell",
    "The mantle",
    "The core",
    "a"

)
g5 = MultipleChoiceQuestion(
    "How many named oceans are found on Earth?",
    "10",
    "4",
    "3",
    "5",
    "b"
)


geography_question_list = [g1,g2,g3,g4,g5]
