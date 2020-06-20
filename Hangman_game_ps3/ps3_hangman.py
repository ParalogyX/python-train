# Hangman game
#

# -----------------------------------


import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

#secretWord = 'ff' 
#lettersGuessed = ['f']
#print(isWordGuessed(secretWord, lettersGuessed))

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    result=''
    for letter in secretWord:
        if letter in lettersGuessed:
            result += letter
        else:
            result += '_'
            
    return result

#secretWord = 'a' 
#lettersGuessed = ['l', 'e', 'k', 'a', 'p', 's']
#lettersGuessed = ['a']
#print(getGuessedWord(secretWord, lettersGuessed))

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    result = ''
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            result += letter
    return result

#tstCount = 0
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#lettersGuessed = []
#lettersGuessed = ('a b c d e f g h i j k l m n o p q r s t u v w x z').split()
#print(getAvailableLetters(lettersGuessed))

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    #introduction
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
	
    #guessing
    won = False
    lost = False
    guessesLeft = 8
    guessedLetters = []
    
    while not (won or lost):
        print('-------------')
        print('You have ' + str(guessesLeft) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(guessedLetters))
        letter = input('Please guess a letter: ').lower()
        if letter in guessedLetters:
            print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, guessedLetters))
        else:
            guessedLetters += letter
            if letter in secretWord:
                print ('Good guess: ' + getGuessedWord(secretWord, guessedLetters))
            else:
                print ('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, guessedLetters))
                guessesLeft -= 1
        
        won = isWordGuessed(secretWord, guessedLetters)
        lost = guessesLeft <= 0
        
        if won:
            print('-------------')
            print ('Congratulations, you won!')
        if lost:
            print('-------------')
            print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()

#secretWord = 'vovka'
hangman(secretWord)
