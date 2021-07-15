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
    for letter in secret_word:
        if  letter not in letters_guessed:
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
    guess = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guess = guess + letter
        else:
            guess = guess + '_ '
    return guess


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_left = string.ascii_lowercase
    for letter in letters_guessed:
        letters_left = letters_left.replace(letter, '')
    return letters_left

def hangman(secret_word):
    
    # secret_word: string, the secret word to guess.
    # Starts up an interactive game of Hangman.
    # * At the start of the game, let the user know how many 
    #   letters the secret_word contains and how many guesses s/he starts with
    # * The user should start with 6 guesses
    # * Before each round, you should display to the user how many guesses
    #   s/he has left and the letters that the user has not yet guessed.
    print("",\
          '\n'+ "Welcome to Hangman game. Your task is to guess the letters of the secret word to free the hangman.", \
              '\n' + "The secret word is " + str(len(secret_word)) + " letters long! Guess it and you go free ;)", \
              '\n'+ "Note: you only have 8 wrong guesses")
    guesses_left = 8
    warnings = 3
    
    letters_guessed = ''
    letters_left = get_available_letters(letters_guessed)
    while  guesses_left > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        print("---------")
        print("You have " + str(guesses_left) + " left.")
        print("Available letters: " + str(letters_left) )
        guess = input("Guess a letter ")
        if guess.isalpha()==False:
            if warnings > 0:
                warnings = warnings -1
                print("Oops! That is not a valid letter. You have " + str(warnings) + " warnings left")
            elif guesses_left > 0:
        
                print( "Oops! That is not a valid letter." + '\n' + get_guessed_word(secret_word, letters_guessed))
                print("You now have no warnings left so you lose one guesss")
                guesses_left = guesses_left - 1
                print(" You now have " + str(guesses_left) + " guesses left")
        else:
            letter = guess.lower()
            if letter in letters_guessed:
                if warnings > 0:
                    warnings = warnings -1
                    print( "You have already guessed this letter, sorry " + '\n' + get_guessed_word(secret_word, letters_guessed))
                    print(" You now have " + str(warnings) + " warnings left")
                else:
                    print( "You have already guessed this letter, sorry" + get_guessed_word(secret_word, letters_guessed))
                    print("You now have no warnings left so you lose one guesss")
                    guesses_left = guesses_left - 1
                    print(" You now have " + str(guesses_left) + " guesses left")
                
            elif letter in secret_word:
                letters_guessed = letters_guessed + letter
                print("Good guess! " + get_guessed_word(secret_word, letters_guessed))
                letters_left = letters_left.replace(letter,'')
                if is_word_guessed(secret_word, letters_guessed) == True:
                    print ("Congrats, you won!")
                    break
            else:
                print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                guesses_left = guesses_left - 1
                letters_guessed = letters_guessed + letter
                letters_left = letters_left.replace(letter, '')
    if is_word_guessed(secret_word, letters_guessed) == False:
        print ("Sorry, you ran out of guesses. The word was '" + str(secret_word) + "' . " )        
        
    
    


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
    match_letters = []
    match_results =  []
    matched = False
    my_word = my_word.replace(" ",'')
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            char = my_word[i]
            if str.isalpha(char) == True:
                match_results.append(char == other_word[i])
                if char == other_word[i]:
                    match_letters.append(other_word[i])
        for i in range(len(my_word)):
            
            char = my_word[i]
            if str.isalpha(char) == False:
                
                match_results.append(other_word[i] not in match_letters)
                                              
        
        if False not in match_results:
                matched = True
                
    return matched
                             

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
              Keep in mind that in hangman when a letter is guessed, all the positions
              at which that letter occurs in the secret word are revealed.
              Therefore, the hidden letter(_ ) cannot be one of the letters in the word
              that has already been revealed.

    '''
    possible_matches = str()
    for word in wordlist:
        if match_with_gaps(my_word, word) == True:
            possible_matches += word + ' '
        
    if possible_matches == '':
        print('No matches found')
    else:
        return possible_matches
            


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
    warnings = 3
    guesses_left = 6
    
    vowels = ['a', 'e', 'i' , 'o', 'u']
    letters_guessed = []
    unique_letters=[]    
    
    print('Welcome to Hangman game. Your task is to guess the letters of the secret word to free the hangman',\
          '\n' + 'you can get help by typing "*" ', \
          '\n' + 'I am thinking of a word that is', \
          len(secret_word), 'letters long.', \
          '\n' + 'You have', warnings, 'warnings left.', \
          '\n' + '-------------', \
          '\n' + 'You have', guesses_left, 'guesses left.', \
          '\n' + 'Available letters:', \
          get_available_letters(letters_guessed))
    
    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters.append(letter)
    number_unique_letters = len(unique_letters)
    
    
    
    while guesses_left > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        char = input('Please guess a letter: ')
        
        if char != '*' and str.isalpha(char) == False or char in letters_guessed:
            if warnings > 0:
                warnings -= 1
                if char in letters_guessed:
                    print("Oops! You've already guessed that letter. " + \
                          'You have', warnings \
                          , 'warnings left:' \
                          , get_guessed_word(secret_word, letters_guessed))
                else:
                    print('Oops! That is not a valid letter. ' + \
                          'You have', warnings \
                          , 'warnings left:' \
                          , get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_left -= 1
                if char in letters_guessed:
                    print("Oops! You've already guessed that letter. " + \
                          'You have no warnings left so you lose ' + \
                          'one guess:' \
                          , get_guessed_word(secret_word, letters_guessed))
                else: 
                    print('Oops! That is not a valid letter. ' + \
                          'You have no warnings leftso you lose ' + \
                          'one guess:' \
                          , get_guessed_word(secret_word, letters_guessed))

        elif char == '*':
            print('Possible word matches are:' \
                  '\n' + show_possible_matches(\
                        get_guessed_word(secret_word, letters_guessed)))
            
        else:
            letter = str.lower(char)
            letters_guessed.append(letter)
        
            if letter in secret_word:
                print('Good guess:', \
                      get_guessed_word(secret_word, letters_guessed))
            elif letter in vowels and guesses_left > 1 :
                guesses_left -= 2
                print('Oops! That letter is not in my word:', \
                      get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_left -= 1
                print('Oops! That letter is not in my word:', \
                      get_guessed_word(secret_word, letters_guessed))
            
        
        if is_word_guessed(secret_word, letters_guessed) == False and guesses_left > 0:
            print('-------------', '\n' + 
                  'You have', guesses_left, \
                  'guesses left.', '\n' + 'Available letters:', \
                  get_available_letters(letters_guessed))
        elif guesses_left == 0:
             print('-------------', '\n' + 
                  'Sorry, you ran out of guesses. The word was' \
                  , str(secret_word) + '.')
        else: 
            total_score = guesses_left * number_unique_letters
            print('-------------', '\n' + 
                  'Congratulations, you won!', '\n' + 
                  'Your total score for this game is:', total_score)




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":s
#     # pass

#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
