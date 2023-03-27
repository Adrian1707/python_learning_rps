from enum import Enum
import random

class GameResult(Enum):
    WIN = 1
    TIE = 0
    LOSS = -1

class RPSGame:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def play_game(self, player_choice):
        computer_choice = random.choice(self.choices)
        if player_choice == computer_choice:
            return GameResult.TIE
        elif (player_choice == 'rock' and computer_choice == 'scissors' or
              player_choice == 'paper' and computer_choice == 'rock' or
              player_choice == 'scissors' and computer_choice == 'paper'):
            return GameResult.WIN
        else:
            return GameResult.LOSS
