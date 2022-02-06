# Wordle Clone
# (c) Michael Tucker 2022

import random

# Loads and returns a word list of specified wordlength from a specified file
def loadWordList(fileName, wordLength):
    wordList = []

    with open(fileName) as f:
        contents = f.read()
    words = contents.splitlines()

    for word in words:
        if len(word) == wordLength:
            wordList.append(word.upper())

    return wordList

# Checks a guessed word against the wordle, returns true if correct
def checkWordle(guess, wordle):
    if guess == wordle:
        return True

    result = ''

    for i in range(len(guess)):
        if guess[i] == wordle[i]:
            result += '^'
        elif guess[i] in wordle:
            result += '*'
        else:
            result += '-'

    print(result)
    return False

# Plays the wordle game
def play(wordLength, turns, wordle, wordList):
    turn = 1

    while(turn <= turns):
        guess = input('Guess #'+str(turn)+':\n')
        guess = guess.upper()

        if len(guess) != len(wordle):
            print('Guess is not correct length')
        elif guess not in wordList:
            print('Invalid guess')
        else:
            turn += 1
            if (checkWordle(guess, wordle)):
                print('WINNER :)')
                break

    if turn > turns:
        print('GAME OVER :(')
        print(wordle)

# Game setup
def main():
    print("WORDLE")

    wordLength = 0
    while wordLength < 3 or wordLength > 12:
        wordLength = int(input('Word Length: '))
        if wordLength < 3 or wordLength > 12:
            print("Invalid Word Length")

    turns = 0
    while turns < 2:
        turns = int(input('Number of Turns: '))
        if turns < 2:
            print("Invalid Number of Turns")

    possibleWordles = loadWordList('10k_words.txt',wordLength)
    wordle = possibleWordles[random.randrange(len(possibleWordles))]
    wordle = wordle.upper()

    wordList = set(loadWordList('engmix.txt',wordLength) + possibleWordles)
    play(wordLength, turns, wordle, wordList)


main()
