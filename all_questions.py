# ---------------- Classes ---------------------------- #
#Add a method to display questions
#Add a method to check answer based on user input  (MAYBE DONT DO THIS YET)
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
    "Artic OCean",
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
