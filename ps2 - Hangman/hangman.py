# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True
            


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    output = ""
    for char in secret_word:
        if char in letters_guessed:
            output += char
        else:
            output += "_ "
    return output


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    output = []
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in  string.ascii_lowercase:
        output += char
    for char in letters_guessed:
        output.remove(char)
    return "".join(output)  
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    print("You have 3 warnings left.")
    print("-------------")
    letters_guessed = []
    warnings = 3
    guesses = 6
    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("You have",guesses,end="")
        print(" guesses left" if guesses > 1 else " guess left")
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ")
        if not guess.isalpha():
            print("Oops! That is not a valid letter.",end="")
            if(warnings > 0):
                warnings -= 1
            else:
                guesses -= 1
            print("You have",warnings,end="")
            print(" warning left:" if warnings == 1 else " warnings left:",end="")
        
        elif guess.lower() in letters_guessed:
            print("Oops! You've already guessed that letter.",end="")
            if(warnings > 0):
                warnings -= 1
            else:
                guesses -= 1
            print("You have",warnings,end="")
            print(" warning left:" if warnings == 1 else " warnings left:",end="")
        elif not guess.lower() in secret_word:
            print("Oops! That letter is not in my word:",end="")
            letters_guessed += guess.lower()
            guesses -= 1
            if guess.lower() in "aeiou":
                guesses -= 1
        else:
            print("Good guess:",end="")
            letters_guessed += guess.lower()
        print(get_guessed_word(secret_word,letters_guessed))
        print("-------------")
    if(guesses > 0):
        print("Congratulations, you won!")
        print("Your total score for this game is:", guesses*len(set(secret_word)))
    else:
        print("Sorry, you ran out of guesses. The word was ",secret_word,".",sep="")

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_without_spaces = ""
    for char in my_word:
        if char != " ":
            my_word_without_spaces += char
    if len(my_word_without_spaces) != len(other_word):
        return False
    for i in range(len(other_word)):
        if other_word[i] != my_word_without_spaces[i] and my_word_without_spaces[i] != "_":
            return False
        elif my_word_without_spaces[i] == "_" and other_word[i] in my_word_without_spaces:
            return False
    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matches = ""
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matches += word + " "
        
    print(matches) if matches != "" else print("No matches found")
                


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    print("You have 3 warnings left.")
    print("-------------")
    letters_guessed = []
    warnings = 3
    guesses = 6
    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("You have",guesses,end="")
        print(" guesses left" if guesses > 1 else " guess left")
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ")
        if guess == "*":
            show_possible_matches(get_guessed_word(secret_word,letters_guessed))
        elif not guess.isalpha():
            print("Oops! That is not a valid letter.",end="")
            if(warnings > 0):
                warnings -= 1
            else:
                guesses -= 1
            print("You have",warnings,end="")
            print(" warning left:" if warnings == 1 else " warnings left:",end="")
        
        elif guess.lower() in letters_guessed:
            print("Oops! You've already guessed that letter.",end="")
            if(warnings > 0):
                warnings -= 1
            else:
                guesses -= 1
            print("You have",warnings,end="")
            print(" warning left:" if warnings == 1 else " warnings left:",end="")
        elif not guess.lower() in secret_word:
            print("Oops! That letter is not in my word:",end="")
            letters_guessed += guess.lower()
            guesses -= 1
            if guess.lower() in "aeiou":
                guesses -= 1
        else:
            print("Good guess:",end="")
            letters_guessed += guess.lower()
        print(get_guessed_word(secret_word,letters_guessed))
        print("-------------")
    if(guesses > 0):
        print("Congratulations, you won!")
        print("Your total score for this game is:", guesses*len(set(secret_word)))
    else:
        print("Sorry, you ran out of guesses. The word was ",secret_word,".",sep="")
    


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
