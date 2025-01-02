# Masai-Project-IIT-Mandi
# Quiz Application
This Python application is a command-line quiz game designed to ask users multiple-choice questions, evaluate their answers, and track their scores. The application reads questions and answers from external text files and stores user scores with their names in another text file.
# Working 
-> Prompts the user to enter their name.

-> Loads questions and answers using load_quiz_content() from "questions.txt".

-> Iterates through each question:

-> Displays the question and options.

-> Asks the user to select an option (A, B, C, or D).

-> Checks if the answer is correct from "answers.txt" and updates the score.

-> Displays the final score.

-> Saves the score to "score.txt" using record_score().
# File Dependencies
questions.txt: Contains quiz questions and their options (5 lines per question: 1 question + 4 options).

answers.txt: Contains the correct answers (one per line).

score.txt: Stores player names and scores.

