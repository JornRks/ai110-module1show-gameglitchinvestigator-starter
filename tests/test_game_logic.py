from streamlit.testing.v1 import AppTest
from logic_utils import check_guess, parse_guess

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
#tests for edge cases (challenge 1)
def test_decimal_guesses_round_to_nearest_whole_number():
    # Regression: decimals were truncated, so "19.99" became 19 instead of 20
    assert parse_guess("19.99") == (True, 20, None)
    assert parse_guess("19.4") == (True, 19, None)

def test_halves_round_up():
    # Python's round() would give 2 here; the game rounds halves up
    assert parse_guess("2.5") == (True, 3, None)
    assert parse_guess("7.5") == (True, 8, None)

def test_scientific_notation_is_accepted():
    # Regression: "1e2" had no ".", went to int(), and was rejected as not a number
    assert parse_guess("1e2") == (True, 100, None)

def test_non_numbers_are_rejected():
    for raw in ["abc", "inf", "nan"]:
        ok, value, err = parse_guess(raw)
        assert not ok
        assert value is None
        assert err == "That is not a number."

def test_blank_input_is_rejected():
    for raw in ["", "   ", None]:
        assert parse_guess(raw) == (False, None, "Enter a guess.")

def test_out_of_range_guesses_are_rejected():
    # Regression: -5, 0, and 1000 were accepted on Easy (1-20)
    for raw in ["-5", "0", "21", "1000"]:
        ok, value, err = parse_guess(raw, 1, 20)
        assert not ok
        assert value is None
        assert err == "Guess must be between 1 and 20."

def test_range_edges_are_accepted():
    assert parse_guess("1", 1, 20) == (True, 1, None)
    assert parse_guess("20", 1, 20) == (True, 20, None)

def test_decimal_that_rounds_out_of_range_is_rejected():
    # 20.5 rounds to 21, which is past Easy's top of 20
    ok, _, _ = parse_guess("20.5", 1, 20)
    assert not ok

def test_hints_compare_numbers_not_text():
    # Regression: the secret was a string on even attempts, so "9" > "50" said Too High
    assert check_guess(9, 50)[0] == "Too Low"
    assert check_guess(60, 100)[0] == "Too Low"
    assert check_guess(100, 60)[0] == "Too High"

def test_even_attempt_hint_is_correct_in_app():
    # Regression: the second guess compared against str(secret) and could give the wrong hint
    at = AppTest.from_file("../app.py").run()
    at.session_state.secret = 50
    at.run()

    at.text_input(key="guess_input_Normal").input("40")
    at.button[0].click().run()
    at.text_input(key="guess_input_Normal").input("9")
    at.button[0].click().run()

    assert at.session_state.attempts == 2
    assert "HIGHER" in at.warning[0].value

def test_invalid_input_does_not_use_an_attempt():
    # Regression: typos and out-of-range guesses still counted against the attempt limit
    at = AppTest.from_file("../app.py").run()

    for raw in ["abc", "1000", "-5", ""]:
        at.text_input(key="guess_input_Normal").input(raw)
        at.button[0].click().run()

    assert at.session_state.attempts == 0
    assert at.session_state.status == "playing"
    assert "Attempts left: 8" in at.info[0].value
