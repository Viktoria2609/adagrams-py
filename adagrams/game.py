from random import randint


def draw_letters():
    letter_pool = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'D', 'D',
 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'F', 'F', 'G', 'G', 'G',
 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', 'L', 'L', 'L', 'L',
 'M', 'M', 'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P',
 'P', 'Q', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T',
 'T', 'U', 'U', 'U', 'U', 'V', 'V', 'W', 'W', 'X', 'Y', 'Y', 'Z']
    #create a list
    drawn_letters = []
    for i in range(10):
        if len(letter_pool) == 0:
           break

        index = randint(0, len(letter_pool) - 1)  
        drawn_letters.append(letter_pool[index])  
        letter_pool.pop(index)  

    return drawn_letters 

def uses_available_letters(word, letter_bank):
   
    letters_bank_copy = list(letter_bank)
    word = word.upper()
    for letter in word:
        if letter not in letters_bank_copy:
          return False
        letters_bank_copy.remove(letter)
    return True

def score_word(word):
    Score_chart = {
        "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
        "D": 2, "G": 2,
        "B": 3, "C": 3, "M": 3, "P": 3,
        "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
        "K": 5,
        "J": 8, "X": 8,
        "Q": 10, "Z": 10
    }

    word = word.upper()  
    total_score = 0  

    
    for letter in word:  
        if letter in Score_chart:  
            total_score += Score_chart[letter] 
        else:
            total_score += 0  

    
    if len(word) >= 7 and len(word) <= 10:
        total_score += 8  

    return total_score 


def get_highest_word_score(word_list):
    pass