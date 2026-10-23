# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.
- Utalized the same prompt to generate all 11 test cases.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
|1. Numbers Outside Range|Generate three potential edge case inputs that might break my game. Generate pytests to verify that my app handles these inputs correctly|test_out_of_range_guesses_are_rejected, test_range_edges_are_accepted, test_decimal_that_rounds_out_of_range_is_rejected, test_invalid_input_does_not_use_an_attempt|Yes: -5, 0, 21, 1000 are rejected on Easy; 1 and 20 are accepted; 20.5 rounds to 21 and is rejected |These pytests were created to ensure a guessed value remains inside the valid range. For example, if ur playing on easy (range 1-20) and u guess 50,  a message will pop up correcting ur input, and an attempt wont be removed. These tests check if the guess is properly handled|
|2. Decimal or Unusual Number Format|Same prompt as above|test_decimal_guesses_round_to_nearest_whole_number, test_halves_round_up, test_scientific_notation_is_accepted, test_non_numbers_are_rejected, test_blank_input_is_rejected|Yes: 19.99 → 20, 19.4 → 19, 2.5 → 3, 7.5 → 8, 1e2 → 100. abc, inf, nan, "", " " and None are all rejected with the right message|These pytests were created to test whether or not the user inputs a valid entry, and if so, its properly handled. If decimals or scientific notation are given as input, the number is rounded to the nearest whole number/converted to an integer value and compared to the secret. If unusual inputs are given, these are rejected and no attempt is used|
|3. Hints Always Compare Numbers|Same prompt as above|test_hints_compare_numbers_not_text, test_even_attempt_hint_is_correct_in_app|Yes: With the secret set to 50, guessing 40 and then 9 gives "Go HIGHER" on the second (even-numbered) guess|On even attempts the guess is converted to a string and compared with the secret. When the # of digits differ, a comparison such as '9 > 50' will test as true. These tests now ensure that this is no longer the case and all guesses are compared numerically|
---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
