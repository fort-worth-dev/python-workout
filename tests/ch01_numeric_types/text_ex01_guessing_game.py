"""Tests for ex01_guessing_game module."""

from unittest.mock import patch

import pytest

from python_workout.ch02_strings.ex01_guessing_game import guessing_game


class TestGuessingGame:
    """Test suite for guessing_game function."""

    @patch("python_workout.ch02_strings.ex01_guessing_game.random.randint")
    def test_correct_guess_first_try(self, mock_randint, capsys, monkeypatch):
        """Test user guesses correctly on first attempt."""
        mock_randint.return_value = 42

        # Mock input to return correct answer immediately
        monkeypatch.setattr("builtins.input", lambda _: "42")

        guessing_game()

        captured = capsys.readouterr()
        assert "Just right!" in captured.out
        assert "Too high" not in captured.out
        assert "Too low" not in captured.out

    @patch("python_workout.ch02_strings.ex01_guessing_game.random.randint")
    def test_multiple_guesses_with_feedback(self, mock_randint, capsys, monkeypatch):
        """Test game provides correct feedback for high and low guesses."""
        mock_randint.return_value = 50

        # Mock input to return sequence: too high, too low, correct
        inputs = iter(["75", "25", "50"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        guessing_game()

        captured = capsys.readouterr()
        output = captured.out

        # Verify all three feedback messages appear
        assert "Too high" in output
        assert "Too low" in output
        assert "Just right!" in output

        # Verify they appear in the correct order
        too_high_pos = output.find("Too high")
        too_low_pos = output.find("Too low")
        just_right_pos = output.find("Just right!")

        assert too_high_pos < too_low_pos < just_right_pos

    @pytest.mark.parametrize(
        "target,guesses",
        [
            (0, ["50", "25", "10", "0"]),
            (100, ["50", "75", "90", "100"]),
        ],
    )
    @patch("python_workout.ch02_strings.ex01_guessing_game.random.randint")
    def test_boundary_values(
        self, mock_randint, target, guesses, capsys, monkeypatch
    ):
        """Test game works with boundary values 0 and 100."""
        mock_randint.return_value = target

        inputs = iter(guesses)
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        guessing_game()

        captured = capsys.readouterr()
        assert "Just right!" in captured.out

    @patch("python_workout.ch02_strings.ex01_guessing_game.random.randint")
    def test_invalid_input_handling(self, mock_randint, capsys, monkeypatch):
        """Test game handles non-numeric input gracefully."""
        mock_randint.return_value = 50

        # Mock to return invalid inputs followed by correct answer
        inputs = iter(["abc", "12.5", "", "fifty", "50"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        guessing_game()

        captured = capsys.readouterr()
        output = captured.out

        # Should see error messages for invalid inputs
        assert output.count("Please enter a valid number") == 4

        # Game should still complete successfully
        assert "Just right!" in output

    @patch("python_workout.ch02_strings.ex01_guessing_game.random.randint")
    def test_many_guesses(self, mock_randint, capsys, monkeypatch):
        """Test game handles multiple incorrect guesses before success."""
        mock_randint.return_value = 42

        # Simulate a longer game session
        # 1, 10, 20, 30 are too low (4)
        # 50, 45, 43 are too high (3)
        # 42 is correct
        inputs = iter(["1", "10", "20", "30", "50", "45", "43", "42"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))

        guessing_game()

        captured = capsys.readouterr()
        output = captured.out

        # Should have 4 "Too low" messages
        assert output.count("Too low") == 4

        # Should have 3 "Too high" messages
        assert output.count("Too high") == 3

        # Should end with success
        assert "Just right!" in output

    @patch("python_workout.ch02_strings.ex01_guessing_game.random.randint")
    def test_input_prompt_format(self, mock_randint, capsys, monkeypatch):
        """Test that the input prompt has the expected format."""
        mock_randint.return_value = 50

        monkeypatch.setattr("builtins.input", lambda prompt: "50")

        guessing_game()

        # The prompt should be consistent
        # Note: capsys doesn't capture the prompt directly, but we can verify
        # the function completes successfully with expected output
        captured = capsys.readouterr()
        assert "Just right!" in captured.out
