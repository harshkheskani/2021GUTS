import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackathon.settings')

import django
django.setup()
from quiz_app.models import *

def populate():

    english_questions = [
        {"question": "What is a Verb?", "wrongAnswers":["A word reffering to a place", "A word to describe", "A word to exaggerate"], "correctAnswer": "A doing word"},
        {"question": "What is an Adjective?", "wrongAnswers":["A word to exaggerate", "A word reffering to a place", "A doing word"], "correctAnswer": "A word to describe"},
        {"question": "Who wrote A Christmas Carol?", "wrongAnswers":["JK Rowling", "William Shakespeare", "Homer"], "correctAnswer": "Charles Dickens"},
        {"question": "Who wrote Romeo and Juliet", "wrongAnswers":["JK Rowling", "Charles Dickens", "Homer"], "correctAnswer": "William Shakespeare"}
    ]

    maths_questions = [
        #ADD MATHS QUESIONS HERE IN THE SAME FORMAT AS THE ENGLISH QUESTIONS
        {"question": "How many faces does a Cube have?", "wrongAnswers": [4, 3, 5], "correctAnswer": 6},
        {"question": "If a banana costs 40p and I give the shopkeeper 50p. What is my change?", "wrongAnswers": ["5p", "20p", "1p"], "correctAnswer": "10p"},
        {"question": "What is the perimeter of a circle called?", "wrongAnswers": ["radius", "diameter", "square"], "correctAnswer": "circumference"},
        {"question": "What does the Roman Numeral 'X' equal?", "wrongAnswers": [1, 5, 100], "correctAnswer": 10},
        {"question": "What are the even numbers in the sequence: 2, 5, 7, 9, 10", "wrongAnswers": ["2 and 5", "5, 7 and 9", "9 and 10"], "correctAnswer": "2 and 10"},
        {"question": "If there are 64 popsicles to split among 16 students, how many popsicles do each student get?", "wrongAnswers": [5, 1, 2], "correctAnswer": 4} 
    ]

    german_questions = [
        #ADD GERMAN QUESTIONS HERE IN THE SAME FORMAT AS THE ENGLISH QUESTIONS
        {"question": "Translate: Wie heißt du?", "wrongAnswers": ["How are you?", "How old are you?", "Do you have any pets?"], "correctAnswer": "What is your name?"},
        {"question": "What is a glove in German?", "wrongAnswers": ["Handy", "Hund", "Schuh"], "correctAnswer": "Handschuh"},
        {"question": "Translate: Wann hast du Geburtstag?", "wrongAnswers": ["What is your name?", "How old are you?", "Do you have any pets?"], "correctAnswer": "When is your birthday?"},
        {"question": "How do you say Scotland in German?", "wrongAnswers": ["Deutschland", "Frankreich", "Spanien"], "correctAnswer": "Schottland"},
        {"question": "What are feminine words denoted by?", "wrongAnswers": ["der", "das", "den"], "correctAnswer": "die"}
    ]

    history_questions = [
        {"question":"How many Olympians were there?","wrongAnswers":[10, 8 ,15],"correctAnswer": 12},
        {"question":"Who was the oldest Olympian?","wrongAnswers":["Poseidon", "Hera", "Artemis"],"correctAnswer": "Zeus"},
        {"question":"In which year did the second world war start in?","wrongAnswers":[1940, 1937, 1942],"correctAnswer":1939},
        {"question":"Who was know as Breaveheart","wrongAnswers":["Willian Wallace", "Bonnie Prince Charlie", "Flora MacDonald"],"correctAnswer":"Robert the Bruce"},
        {"question":"What monuments were built in Giza","wrongAnswers":["Luxor Temple", "Abu Simbel", "Karnak"],"correctAnswer":"Pyramids of Giza"},
        {"question":"What is the amphitheatre called in Rome?","wrongAnswers":["Pantheon", "Arch of Titus", "Trajan's Column"],"correctAnswer":"Colosseum"},
        {"question":"According to gtrrk myth, who made horses?","wrongAnswers":["Hades","Hestia","Hera"],"correctAnswer":"Poseidon"},
        {"question":"Where do the Vikings come from?","wrongAnswers":["Germany", "United Kingdom", "India"],"correctAnswer":"Scandinavia"},
        {"question":"How many wives did Henry the VIII have?","wrongAnswers":[10, 3, 8],"correctAnswer": 6},
        {"question":"With organ did the Ancient Egyptians believe intelligence came from?","wrongAnswers":["Lungs", "Kidney", "Brain"],"correctAnswer": "Heart"}  
    ]

    #Add any catagories here
    categories = {
        'English': {'questions': english_questions},
        'Maths': {'questions': maths_questions},
        'German': {'questions': german_questions},
        'History': {'questions': history_questions}
    }

    for cat, cat_data in categories.items():
        c = add_cat(cat)
        for q in cat_data["questions"]:
            add_question(c, q["question"], q["wrongAnswers"], q["correctAnswer"])

    #Print out all of the catagories that have been added
    for c in Category.objects.all():
        for q in Question.objects.filter(category=c):
            print(f"- {c}: {q}")

def add_question(cat, question, wrongAnswers, correctAnswer):
    q = Question.objects.get_or_create(category=cat, question=question)[0]
    q.wAnswer1 = wrongAnswers[0]
    q.wAnswer2 = wrongAnswers[1]
    q.wAnswer3 = wrongAnswers[2]
    q.correctAnswer = correctAnswer
    q.save()
    return q

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == "__main__":
    print("Starting Rango population script...")
    populate()
