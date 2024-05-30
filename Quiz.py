# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:29:14 2023

@author: ikbel
"""

import pgzrun
import random

WIDTH = 800
HEIGHT = 600

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 120, 230)
GREEN = (50, 200, 50)
RED = (200, 50, 50)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

# Define the quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "answers": ["Paris", "Rome", "Berlin", "Madrid"],
        "correct": "Paris",
        "hint": "It's known as the 'City of Love'."
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answers": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct": "Mars",
        "hint": "It's named after the Roman god of war."
    },
    {
        "question": "What is the largest mammal in the world?",
        "answers": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
        "correct": "Blue Whale",
        "hint": "It's a marine mammal."
    },
    # Add more questions here
    {
        "question": "What is the largest ocean in the world?",
        "answers": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
        "correct": "Pacific Ocean",
        "hint": "It's the deepest and largest ocean."
    },
    {
        "question": "Who painted the Mona Lisa?",
        "answers": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"],
        "correct": "Leonardo da Vinci",
        "hint": "He was a famous Italian polymath."
    }
]

current_question = 0
score = 0

# Load background and button images
background = r'bk.png'
button = r'button.png'


def draw():
    screen.fill(BLUE)
    screen.blit(background, (0, 0))
    screen.draw.text(questions[current_question]["question"], (50, 50), color=WHITE, fontsize=30)
    
    y = 150
    for answer in questions[current_question]["answers"]:
        screen.blit(button, (50, y))
        screen.draw.text(answer, (60, y + 10), color=WHITE, fontsize=25)
        y += 100

    screen.draw.text("Score: " + str(score), (50, 500), color=WHITE, fontsize=30)
    screen.draw.text("Press 'H' for Hint", (50, 550), color=WHITE, fontsize=20)

def on_mouse_down(pos):
    global current_question, score
    index = (pos[1] - 150) // 100

    if 0 <= index < len(questions[current_question]["answers"]):
        if questions[current_question]["answers"][index] == questions[current_question]["correct"]:
            score += 5  # Increased points for a correct answer
            
        current_question = random.randint(0, len(questions) - 1)

def on_key_down(key):
    global score
    if key == keys.H:
        # Provide a hint and deduct points if the hint is used
        hint = questions[current_question]["hint"]
        print("Hint: " + hint)
        score -= 2  # Deduct points for using a hint

        # Display the hint on the screen
        screen.draw.text("Hint: " + hint, (50, 450), color=WHITE, fontsize=20)


pgzrun.go()
