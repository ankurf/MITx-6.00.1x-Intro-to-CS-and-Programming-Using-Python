##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/Week_4/Problem_Set_4/
##
##Word Game Part 2

from ps4a import *
import time



#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    
    # Create a new variable to store the best word seen so far (initially None)  
    
    # For each word in the wordList
    
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        
            # Find out how much making that word is worth
            
            # If the score for that word is higher than your best score
            
                # Update your best score, and best word accordingly
                

    # return the best word you found.
    
    score = {}
    try:
        for word in wordList:
            if isValidWord(word, hand, wordList):
                score[word] = score.get(word, 0) + getWordScore(word, n)
        return max(score, key = score.get)    
    except:
        return None


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    total_score = 0
    hand_copy = hand.copy()
    while True:
        print 'Current Hand:', 
        displayHand(hand_copy)
        compWord = compChooseWord(hand_copy, wordList, n)
        if compWord != None:
            total_score += getWordScore(compWord, n)
            print '"'+ str(compWord) + '"', 'earned', getWordScore(compWord, n), 'points.', 'Total:', total_score, 'points'
            hand_copy = updateHand(hand_copy, compWord)
            if calculateHandlen(hand_copy) == 0:
                print 'Total score:', total_score, 'points.'
                break
        else:
            print 'Total score:', total_score, 'points.'
            break
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    #print "playGame not yet implemented." # <-- Remove this when you code this function
    while True:
        i = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if i == 'n':
            while True:
                i_uc = raw_input('Enter u to have yourself play, c to have the computer play: ')
                if i_uc == 'u':
                    n = HAND_SIZE
                    hand = dealHand(n)
                    playHand(hand, wordList, n)
                    break
                elif i_uc == 'c':
                    n = HAND_SIZE
                    hand = dealHand(n)
                    compPlayHand(hand, wordList, n)
                    break
                else:
                    print 'Invalid command.'
        elif i == 'r':
            while True:
                try:
                    len(hand) > 0
                    i_uc = raw_input('Enter u to have yourself play, c to have the computer play: ')
                    if i_uc == 'u':
                        playHand(hand, wordList, n)
                        break
                    elif i_uc == 'c':
                        compPlayHand(hand, wordList, n)
                        break
                    else:
                        print 'Invalid command.'
                except:
                    print 'You have not played a hand yet. Please play a new hand first!'
                    break         
        elif i == 'e':
            break
        else:
            print 'Invalid command.'
            print

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)



