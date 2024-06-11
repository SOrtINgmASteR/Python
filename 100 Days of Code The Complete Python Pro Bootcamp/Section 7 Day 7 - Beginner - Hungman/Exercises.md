<h2 style = "text-align : center;"> Day - 7 (Hangman)</h2>  

<h3 style="text-align:center;">Step - 1 : </h3>  

- First make ASCII art of hangman text to print in beginning.  
- Then make ASCII art of different stages of hanging a man.


<h3 style="text-align:center;">Step - 2 : </h3>  

- First take a list of words.  
- declare a list variable `chosen_word` and choose a random word from the word list using `random.choice(word_list)` & store it in the list variable.  
- Then declare a list variable of same length for the `guess_word` & fill it with underscores (`_`).
- Declare another variable `life_remaining` for keeping track of the remaining life.


<h3 style="text-align:center;">Step - 3 : </h3>  

- Take a letter input from the user, using variable `guess_letter`.
- Then iterate over the `chosen_word`. If `guess_letter` matches `chosen_word[i]`, then assign `guess_word[i]` to `guess_letter`. Also keep a variable `match_letter = True / False` for tracking the letter is matched or not.  
- After this iteration print the `guess_word` list.
- If the letter hadn't matched decrease the `life_remaining` by one & print the hang-man according to the `life_remaining`.


<h3 style="text-align:center;">Step - 4 : </h3>  

- Repeat **Step - 3** until  `chosen_word` is not same as `chosen_word` and `life_remaining` is greater than 0.
- If `chosen_word` is same as `chosen_word` and `life_remaining` is greater than 0 then the user has won.
- If `chosen_word` is not same as `chosen_word` and `life_remaining` is lesser or equal to zero the user loose.

