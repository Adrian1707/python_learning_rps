import unittest
from unittest.mock import patch
from RPSGame import RPSGame, GameResult

class TestRPSGame(unittest.TestCase):
    @patch('random.choice')
    def test_play_game_rock_win(self, mock_choice):
        mock_choice.return_value = 'scissors'
        game = RPSGame()
        result = game.play_game('rock')
        self.assertEqual(result, GameResult.WIN)

    @patch('random.choice')
    def test_play_game_rock_tie(self, mock_choice):
        mock_choice.return_value = 'rock'
        game = RPSGame()
        result = game.play_game('rock')
        self.assertEqual(result, GameResult.TIE)

    @patch('random.choice')
    def test_play_game_rock_loss(self, mock_choice):
        mock_choice.return_value = 'paper'
        game = RPSGame()
        result = game.play_game('rock')
        self.assertEqual(result, GameResult.LOSS)

    @patch('random.choice')
    def test_play_game_paper_win(self, mock_choice):
        mock_choice.return_value = 'rock'
        game = RPSGame()
        result = game.play_game('paper')
        self.assertEqual(result, GameResult.WIN)

    @patch('random.choice')
    def test_play_game_paper_tie(self, mock_choice):
        mock_choice.return_value = 'paper'
        game = RPSGame()
        result = game.play_game('paper')
        self.assertEqual(result, GameResult.TIE)

    @patch('random.choice')
    def test_play_game_paper_loss(self, mock_choice):
        mock_choice.return_value = 'scissors'
        game = RPSGame()
        result = game.play_game('paper')
        self.assertEqual(result, GameResult.LOSS)

    @patch('random.choice')
    def test_play_game_scissors_win(self, mock_choice):
        mock_choice.return_value = 'paper'
        game = RPSGame()
        result = game.play_game('scissors')
        self.assertEqual(result, GameResult.WIN)

    @patch('random.choice')
    def test_play_game_scissors_tie(self, mock_choice):
        mock_choice.return_value = 'scissors'
        game = RPSGame()
        result = game.play_game('scissors')
        self.assertEqual(result, GameResult.TIE)

    @patch('random.choice')
    def test_play_game_scissors_loss(self, mock_choice):
        mock_choice.return_value = 'rock'
        game = RPSGame()
        result = game.play_game('scissors')
        self.assertEqual(result, GameResult.LOSS)
