import random
from words import words
from hangman_visuals import lives_visual_dict
import string
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_upppercase)
    used_letter = set()

    lives = 7
    
    while len(word_letters) > 0:
        print('you have used these letters: ',''.join(used_letter))
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print(lives_visual_dict[lives])
        print ('Current word: ','.join(word_list)')
        user_letter = input(' guess a letter').upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(' ')
            else:
                lives = lives-1
                print('\nYour letter,', user_letter, 'is not in the word.')
        elif user_letter in used_letter:
            print('you have already used that character.Please try again')

    else:
        print('invalid character.please try again')

    if lives == 0:
        print(lives_visual_dict[lives])
        print('you died',word)
    else:
        print('you did it!',word)

    if __name__ == '__main__':
        hangman()