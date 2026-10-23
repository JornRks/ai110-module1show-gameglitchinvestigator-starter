# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
When I first ran the game, everything looked good visually, the UI was normal. The game also operated as normal, allowing me to complete a playthrough. However, as I played I noticed a few issues I will list below.
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
|Guess a value out of range |Game rejects guess as out of range |Guess was accepted |None |
|Enter a decimal value |Guess is rounded to the nearest whole number |Decimals places are cut of and guess is treated as just the whole part of the guess |None |
|Changes difficulty |Secret number changes to match the range |Secret number is only selected once, not changing with the respective difficulty range |None |
|Attempts/Ending a game |The game displays you have zero attempts left when displaying you lost the game |The game announces you have lost/ran out of guesses, but displays u have 1 left |None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude in VScode for this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
My AI agents explanation of a bug: 'The attempts counter started at 1 instead of 0. The display works out attempts left as attempt_limit - attempts. On Normal that was 8 - 1 = 7 before you'd made any guesses, as if one attempt was already used.
One provided suggestion that was correct was Claude's fix of my attempts left bug. It explained that st.session_state.attempts started at 1, rather than 0. This meant the display showed 8 - 1 = 7, even before the user made their first guess. I verified this was correct by not only creating a pytest for the repaired bug, but also checking in the game itself. 
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
One suggestion I did not accept was the first pytest Claude created for my check_guess bug, this was was because 3 of my tests kept failing. I found it was due to the pytest expecting a single string retured, while my check_guess function returned a tuple of 2 strings. I then explained this error to Claude, and it changed the expected return in my pytest to a tuple as well. I then ran pytest again, and each test passed. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? I decided a bug was really fixed after I verified the created pytest as correct, and ran this on my code, only accepting all passes. After this, I ran the app via streamlit and verified the bugs were fixed while playing the game. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
One test I ran was using pytest and it was named _test_hints_point_twords_secret. This test checked if the check_guess function would correctly return the proper hint, given both, if a guess was too high/low. This test showed me that my code was correctly comparing guesses, diplaying the proper content, and returning the appropriate hints.  
- Did AI help you design or understand any tests? How?
Yes, AI helped me understand the pytest I used to test my attempts left bug. I didn't understand how this was being checked, so I had it explain how it uses test_attempts_left_starts_at_full_limit and test_player_gets_all_attempts_before_losing. One checks if the value of 'attempts' is 0 when a new game starts, and the other simulates 7 wrong guesses and checks if the game is still ongoing and if the user gets one more till losing.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns the apps script everytime the user interacts with certain elements. This means important game elements such as score, history, and attempts could be reset each time a guess is submitted. A session state allows me store relevant game information in between these reruns such as the secret number, attempts, score, and game status. Without me using this session state, this information would reset each time the script reruns. I must initialize and update these values using session state in order for my game to run as expected.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - One habit from this project that I will reuse in future labs/projects is the use of my AI coding agent to generate pytests. This will allow me to easily and efficently test my code and logic in the future.
- What is one thing you would do differently next time you work with AI on a coding task?
  - If there is one thing I would do differently, it would be to give my AI agent more specific and procedural tasks. This would prevent my agent from editing certain code that I dont want edited and prevent over-engineering of simple tasks.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - This project changed the way I think about AI generated code, as I can not only use AI to create new code, but simultaniously use AI to check the code it just created. Im positive that the use of Claude to generate pytests will become incredibly useful in the future. 
