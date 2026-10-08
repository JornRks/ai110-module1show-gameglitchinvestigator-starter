# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
When I first ran the game, everything looked good visually, the UI was normal. However, as I played I noticed a few issues I will list below.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1. When I first ran the game, it displayed I had 7 guesses left, when in reality I should have 8 left. 
2. As I was making my guesses, the hints displayed were incorrect/reversed. When I guessed too high, it would tell me to guess higher, and vice versa. The hints should be displaying the opposite.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Attempts/Starting a game |Attempts left should display 8 |Attempts left is 7 |None |
|Entered a guess below the secret number |Display 'Go HIGHER!' |Displayed 'Go LOWER!' |None |
|Click New Game after a win or loss |Attempts, status, history, and score reset |Only the attempts and secret number reset |None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
