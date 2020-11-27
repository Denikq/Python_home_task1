# Problem Set 2, hangman.py
# Name: Denys Dolynniy
# Collaborators: None
# Time spent: 

# Hangman Game

import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words(): 
    #function for loading words of words.txt and creating a list of them
    print('Loading word list from file...') 
    # printing
    inFile = open(WORDLIST_FILENAME, 'r') 
    # inFile: file
    line = inFile.readline() 
    # line: string
    wordlist = line.split() 
    # wordlist: list of strings
    print(len(wordlist), 'words loaded.') 
    # printing amount of words in file words.txt
    return wordlist \
    # returns list of strings (words of words.txt)

def choose_word(wordlist): 
    # function for chosing random elements of the list wordList
    return random.choice(wordlist)
    # returns random word

wordlist = load_words() 

def is_word_guessed(secret_word, letters_guessed): 
    # function for getting boolean answer: to continue the game Hangman or not
    # creation of an empty list
    lst = []
    # for loop: iterating unique elements of letters_guessed
    for k in set(letters_guessed):
        # for loop: iterationg unique elements of secret_word
        for n in set(secret_word):
            # conditonal statement: when the user already has entered the element that is in the secret word
            if k == n:
                # adding element to the list
                lst.append(k)
    # function returns boolean qulity: True, when the user has guessed all elements of the secret word, False elsewhise
    return set(lst) == set(secret_word)

def get_guessed_word(secret_word, letters_guessed):
    # fucntion for getting curring guessed word
    guessed_word = [] 
    # creation of empty list
    for k in secret_word: 
        # for loop: iterating elements of secret_word
        if k in letters_guessed: 
            # conditional statement: when the user has guessed fixed letter 
            guessed_word.append(k)
            # adding the letter to the list guessed_word
        else: 
            # conditional statement: when the user has not guessed fixed letter yet
            guessed_word.append('_ ') 
            # add string '_ ' to the list 
    return ''.join(guessed_word) 
    # returns string of partialy or full guessed secret word

def get_available_letters(letters_guessed):
    # function for getting available letters of the alphabet for user`s input
    all_letters = string.ascii_lowercase 
    # creation a list of lowercase letters of english alphabet
    available_letters = [] 
    # creation of empty list
    for k in all_letters: 
        # for loop: iteration elements of the list all_letters
        if k not in letters_guessed:
            # conditional statemnet: when letter was not guessed by the user
            available_letters.append(k) 
            # adding the letter to the list 
    return ''.join(available_letters) 
    # returns string of not used letters by the user of english alphabet

def start_of_hangman(secret_word):
    # assegment: printing greeting, amount of letters of the secret word and amount of warnings
    start = print(f'Welcome to the game Hangman!\nI am thinking of a word that is {len(secret_word)} letters long.\nYou have 3 warnings left.\n-------------')
    return start # returns string: start of the game

def minus(argument, n): 
    # function for decreasing guesses and warnings
    return argument - n # returns int number
 
def hangman(secret_word):
    # main function hangman
    warnings_remaining = 3 
    # the user always starts with 3 warnings
    guesses_remaining = 6 
    # the user always starts with 6 possible guesses
    letters_guessed = [] 
    # creation of an empty list
    condition = True 
    # assigment: boolean True
    while condition: 
        # while loop
        # call of function
        # assigment adecvate qualities for variables
        list_of_all = helper_func(guesses_remaining, warnings_remaining, letters_guessed, secret_word)
        # game_step is the start text before each round
        # Use: tells to the user how many guesses he has and what letters he has not used yet
        game_step = list_of_all[0] 
        # variable guesses_remaining: amount of posible guesses. 
        # use: for counting totel score and for ending of the game when the user has not any posibility to guess
        guesses_remaining = list_of_all[1]
        # variable guessed_word
        # use: tell about result of the round: has the user guessed a letter of the secret word?
        # output current secret word (with '_ ')
        guessed_word = list_of_all[2]
        # change variable warnings_remaining
        warnings_remaining = list_of_all[3]
        # conditional statement for ending while loop and ending all the program
        if is_word_guessed(secret_word, letters_guessed) == True: 
            # body of if-statemnent: when the user won!
            # countinf=g total score
            total_score = guesses_remaining*len(set(secret_word))
            # change of the guessed_word
            guessed_word = print(f'Congratulations, you won! Your total score for this game is: {total_score}')
            condition = False
            # break of the while loop
            break
        elif guesses_remaining == 0:
            # body of elif-statement: when the user loosed (gusses are over)
            guessed_word = print(f'Sorry, you ran out of guesses. The word was: {secret_word}')
            condition = False
            break 
    # funciton returns information about each round
    return game_step, guessed_word

def helper_func(guesses_remaining, warnings_remaining, letters_guessed, secret_word):
    # helper_func determine the most difficult operations of each round
    # in variable game_step there are start information for the user (amount of guesses remaining and availavle letters)
    game_step = print(f'You have {guesses_remaining} guesses left.\nAvailable Letters: {get_available_letters(letters_guessed)}')
    # the user input the letter. 
    # use function lower() in order to trasnform register of the letter
    choice_the_element = str(input('Please, guess a letter: ')).lower()
    # conditional statement
    # use: cheaking user`s inut
    if choice_the_element.isalpha():
        # when the user has entered a letter from english alphabet
        if choice_the_element in letters_guessed:
            # when the user have entered one element two times
            # decrease amount of warnings
            warnings_remaining = minus(warnings_remaining, 1)
            # conditional statement: when warnings are over
            if warnings_remaining < 0:
                # we cannnot output negative amount of warnings
                warnings_remaining = 0
            # in variable result tells to the user that he already has entered this lette and tells how many warnings he has
            result = f"Oops! You've already guessed that letter. You now have {warnings_remaining} warnings left."
        else:
            # when the user correctly enterd the letter (we don`t know yet result of the round)
            # add element the user has entered to the lise letter_guessed (used letters)
            letters_guessed.append(choice_the_element)
            if choice_the_element not in secret_word:
                # when the letter is not in the secret word
                # tell to the user that he has loosed this round
                result = 'Oops! That letter is not in my word'
                # conditional statement: different element decrease guesses in a different way
                if choice_the_element in ['a', 'e', 'o', 'i']:
                    # when the letter was a vowel (not 'u' or 'y'!)
                    # decrease guesse by 2
                    n = 2
                else:
                    # when the letter was not a vowel
                    # decrease guesses by one
                    n = 1      
                # decreasing of guesses remaining
                guesses_remaining = minus(guesses_remaining, n)
            else:
                # when the user has won the round (correstly guessed the letter)
                # in variavbl result there are a little congratulation
                result = 'Good guess'
    else:
        # when the user has entered something wrong
        # function minus in order to lower quality of warnings for the user
        warnings_remaining = minus(warnings_remaining, 1)
        # when warnings are a negative number (they are over)
        if warnings_remaining <= 0:
            # decrease guesses remainig by one
            guesses_remaining = minus(guesses_remaining, 1)
            # warnings cannot be negative
            warnings_remaining = 0
        # assigment to variavle result warning attention and tell amount of warnings
        result = f'That is not a valid letter. You have {warnings_remaining} warnings left.'
    # use of another conditional statement (before if we were checking isalpha of choice_the_element)
    # the user has to enter only one element
    if len(choice_the_element) != 1:
        # when the user entered wrong long of the element
        # decreasing amount of warnings
        warnings_remaining = minus(warnings_remaining, 1)
        # change result: tell to the user about unvalid element
        result = f'That is not a valid letter. You have {warnings_remaining} warnings left'
    # call of the function assignes to the variable guess
    # it`s current condition of the secret word
    guess = get_guessed_word(secret_word, letters_guessed)
    # varuavle guessed_word is result of user`s inputing and current contion of the secret word
    guessed_word = print(f'{result}: {guess} \n-------------')
    # creation of the list
    lst = [game_step, guesses_remaining, guessed_word, warnings_remaining]
    # function returns list of three importan elements for using them in hangman funtion
    return lst

def match_with_gaps(my_word, other_word):
    # function for learning possible word of given pattern
    # argument my_word is a pattern
    # we need to know boolean answer for the question:
    # can other_word be created from my_word by replacing '_ ' on some letter?
    if len(my_word.replace(' ', '')) == len(other_word):
        # at first, arguments must have equal amount of elements
        # creation of two lists from given arguments (we cannot iterete strings)
        my_word = list(my_word.replace(' ', ''))
        other_word = list(other_word)
        # creation of an empty list
        lst1 = []
        # for loop: use indexes in range from 0 to len(my_word)
        for i in range(len(my_word)):
            # conditional statement 
            # if-statement: when the user has not guessed the letter of secret_word
            if my_word[i] == '_':
                # on the undefined place there is already used letter
                if other_word[i] not in my_word:
                    # adding the element to the list
                    lst1.append(my_word[i])
            # elif-statement: letters are identical
            elif my_word[i] == other_word[i]:
                # adding the element to the list
                lst1.append(my_word[i])
        # funcion returns boolean quality 
        # lists lst1 and my_word have to be equal for boolean True
        return lst1 == my_word
    else:
        # when words are not of the same long it is evident that we cannot do needed operation
        # returns boolean False
        return False

def show_possible_matches(my_word):
    # function for finding possible matches for my_word with words of wordlist
    possible_matches = []
    # creation of an empty list
    for k in wordlist:
        # for loop: iterate elements (words) of the wordlist
        if match_with_gaps(my_word, k) == True:
            # when my_word and k-word can be matched: add k-word to the list of possible matches
            possible_matches.append(k)
    # conditional statement: when in wordlist are no possible matches
    if possible_matches == []:
        # function returns string
        return 'No matches found'
    # when there are possible matches
    else:
        # function returns strnig of possible matches (function join transform the list)
        return ' '.join(possible_matches)

def hangman_with_hints(secret_word):
    # main function hangman with hints
    warnings_remaining = 3
    # the user always starts with 3 warnings
    guesses_remaining = 6 
    # the user always starts with 6 possible guesses
    letters_guessed = []
    # craeation of an empty list
    condition = True
    # asiigment: boolean True
    while condition:
        # while loop with condition (condition is a variable condition that is equal to boolean True)
        # call of function
        # assigment adecvate qualities for variables
        list_of_all = helper_func_hints(guesses_remaining, warnings_remaining, letters_guessed, secret_word)
        # game_step is the start text before each round
        # Use: tells to the user how many guesses he has and what letters he has not used yet
        game_step = list_of_all[0]
        # variable guesses_remaining: amount of posible guesse. 
        # use: for counting totel score and for ending of the game when the user has not any posibility to guess
        guesses_remaining = list_of_all[1]
        # variable guessed_word
        # use: tell about result of the round: has the user guessed a letter of the secret word?
        # output current secret word (with '_ ')
        guessed_word = list_of_all[2]
        # change variavle warnings_remainings, because it could decrease
        warnings_remaining = list_of_all[3]
        letters_guessed = list_of_all[4]
        # conditional statement for ending while loop and ending all the program
        if is_word_guessed(secret_word, letters_guessed) == True: 
            # body of if-statemnent: when the user won!
            # counting total score
            total_score = guesses_remaining*len(set(secret_word))
            # change of the guessed_word
            guessed_word = print(f'Congratulations, you won! Your total score for this game is: {total_score}')
            condition = False
            # break of the while loop
            break
        elif guesses_remaining == 0:
            # body of elif-statement: when the user loosed (gusses are over)
            guessed_word = print(f'Sorry, you ran out of guesses. The word was: {secret_word}')
            condition = False
            break 
    # funciton returns information about each round
    return game_step, guessed_word
    
def helper_func_hints(guesses_remaining, warnings_remaining, letters_guessed, secret_word):
    # helper_func_hints determine the most difficult operations of each round (has a possibity to tell hints for the user)
    # in variable game_step there are start information for the user (amount of guesses remaining and availavle letters)
    game_step = print(f'You have {guesses_remaining} guesses left.\nAvailable Letters: {get_available_letters(letters_guessed)}')
    # the user input the letter. 
    # use function lower() in order to trasnform register of the letter
    choice_the_element = str(input('Please, guess a letter: ')).lower()
    # conditional statement
    # use: cheaking user`s input
    if choice_the_element.isalpha():
        # when the user has entered a letter from english alphabet
        if choice_the_element in letters_guessed:
            # when the user have entered one element two times
            # decrease amount of warnings
            warnings_remaining = minus(warnings_remaining, 1)
            # conditional statement: when warnings are over
            if warnings_remaining < 0:
                # we cannnot output negative amount of warnings
                warnings_remaining = 0
                # warnings cannot be negative
            # in variable result tells to the user that he already has entered this lette and tells how many warnings he has
            result = f"Oops! You've already guessed that letter. You now have {warnings_remaining} warnings left."
        else:
            # when the user correctly enterd the letter (we don`t know yet result of the round)
            # add element the user has entered to the lise letter_guessed (used letters)
            letters_guessed.append(choice_the_element)
            if choice_the_element not in secret_word:
                # when the letter is not in the secret word
                # tell to the user that he has loosed this round
                result = 'Oops! That letter is not in my word'
                # conditional statement: different element decrease guesses in a different way
                if choice_the_element in ['a', 'e', 'o', 'i']:
                    # when the letter was a vowel (not 'u' or 'y'!)
                    # decrease guesse by 2
                    n = 2
                else:
                    # when the letter was not a vowel
                    # decrease guesses by one
                    n = 1      
                # decreasing of guesses remaining
                guesses_remaining = minus(guesses_remaining, n)
            else:
                # when the user has won the round (correstly guessed the letter)
                # in variavbl result there are a little congratulation
                result = 'Good guess'
    elif choice_the_element == '*':
        # elif-stetement: when the user wants to know possible matches (the user has to enter '*')
        # change result: instead of result of the round the user sees possible matches for the secret word
        result = f'Possible word mathces are: {show_possible_matches(get_guessed_word(secret_word, letters_guessed))} for'           
    else:
        # when the user has entered something wrong
        # function minus in order to lower quality of warnings for the user
        warnings_remaining = minus(warnings_remaining, 1)
        # when warnings are a negative number (they are over)
        if warnings_remaining <= 0:
            # decrease guesses remainig by one
            guesses_remaining = minus(guesses_remaining, 1)
            # change amount of warnings to zero to show the user that he has to be more concentrated on correct inputing
            warnings_remaining = 0
        
        # assigment to variavle result warning attention and tell amount of warnings
        result = f'That is not a valid letter. You have {warnings_remaining} warnings left.'
    # use of another conditional statement (before if we were checking isalpha of choice_the_element)
    # the user has to enter only one element
    if len(choice_the_element) != 1:
        # when the user entered wrong long of the element
        # decreasing amount of warnings
        warnings_remaining = minus(warnings_remaining, 1)
        # change result: tell to the user about unvalid element
        result = f'That is not a valid letter. You have {warnings_remaining} warnings left'
    # call of the function assignes to the variable guess
    # it`s current condition of the secret word
    guess = get_guessed_word(secret_word, letters_guessed)
    # varuavle guessed_word is result of user`s inputing and current contion of the secret word
    guessed_word = print(f'{result}: {guess} \n-------------')
    # creation of the list 
    lst = [game_step, guesses_remaining, guessed_word, warnings_remaining, letters_guessed]
    # function returns list of three importan elements for using them in hangman funtion
    return lst

if __name__ == '__main__':
    secret_word = choose_word(wordlist)
    start_of_hangman(secret_word)
    #hangman(secret_word)
    #if you want to play with hints uncoment next row:
    hangman_with_hints(secret_word)


