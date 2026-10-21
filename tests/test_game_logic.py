from streamlit.testing.v1 import AppTest
from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_hints_point_toward_secret():
    # Regression: hints used to be reversed ("Too High" said "Go HIGHER!")
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_attempts_left_starts_at_full_limit():
    # Regression: attempts started at 1, so Normal showed "Attempts left: 7" instead of 8
    at = AppTest.from_file("../app.py").run()
    assert at.session_state.attempts == 0
    assert "Attempts left: 8" in at.info[0].value

def test_player_gets_all_attempts_before_losing():
    # Regression: starting at 1 also ended the game one guess early (after 7 on Normal)
    at = AppTest.from_file("../app.py").run()
    wrong_guess = 1 if at.session_state.secret != 1 else 2

    for _ in range(7):
        at.text_input(key="guess_input_Normal").input(str(wrong_guess))
        at.button[0].click().run()
    assert at.session_state.status == "playing"

    at.text_input(key="guess_input_Normal").input(str(wrong_guess))
    at.button[0].click().run()
    assert at.session_state.status == "lost"
