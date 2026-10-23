import math


#FIX: Refactored from app.py to here using AI agent.
#Updated the difficulty settings so hard has a range 1-100 rather than 1-50
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


#FIX: Refactored from app.py to here using AI agent.
def parse_guess(raw: str, low: int = None, high: int = None):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw.strip() == "":
        return False, None, "Enter a guess."

    #FIX: decimals were truncated with int(float(raw)), so "19.99" became 19, and
    # "1e2" was rejected because it had no ".". Whole numbers still parse with int();
    # anything else float() accepts is rounded to the nearest whole number (half up,
    # so 2.5 -> 3, unlike Python's round() which gives 2).
    try:
        value = int(raw)
    except ValueError:
        try:
            value = math.floor(float(raw) + 0.5)
        except Exception:
            return False, None, "That is not a number."

    #FIX: out-of-range guesses like -5 or 1000 were accepted and only got a
    # "higher"/"lower" hint. Now they are rejected when a range is given.
    if low is not None and high is not None and not (low <= value <= high):
        return False, None, f"Guess must be between {low} and {high}."

    return True, value, None

#FIX: Refractored from app.py to here using AI agent.
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    #FIX: removed the TypeError fallback that compared str(guess) to a string secret.
    # Text comparison goes character by character, so "9" > "50" and "60" > "100",
    # giving "Too High" for guesses that were too low. Both values are ints now.
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


#FIX: Refactored from app.py to here using AI agent.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
