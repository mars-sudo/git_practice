class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_questions(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"-{response}")


# The class starts with a survey question that you provide and includes an empty list to store reponses.
# The class has methods to print the survey question, add a new response to the response list,
# and print all the responses stored in the list. 

# To create an instance representing a particular survey, you display the survey question with 
# show_qustion(), store a response using store_response(), and show the results with show_results()
