from survey import AnonymousSurvey 

# Define a question, and make a survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_questions()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
    
# Show the survey results
print ("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

# This program defines a question ("What langauge did you first learn to speak")
# and creates an AnonymousSurvey object with that question. 
# The program calls show_question() to display the question and then prompt for
# responses. Each response is stored as it is received. 
# When all responses have entered, show_results() prints the survey results. 


