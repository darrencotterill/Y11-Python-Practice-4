from testhelper import test
import requests
import random
import time

url = "https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words_alpha.txt"

# Get a list of all english words
words_list = requests.get(url).content.split()
all_words = []
nine_letter_words = []

#Select the words that are >2 letters and all the nine letter words
for word in words_list:
    if len(word) > 2 and len(word) < 10:
        all_words.append(word.decode('ascii'))
    if len(word) == 9:
        nine_letter_words.append(word.decode('ascii'))

word_to_guess = nine_letter_words[random.randint(0,len(nine_letter_words))]

start_time = time.time()
score = 0

def draw_word_grid(w):
    str_var = list(w)
    print (str_var)
    random.shuffle(str_var)
    shuffled = "".join(str_var)

draw_word_grid(word_to_guess)

while (time.time() < (start_time + 60)):
    # Replace the code below with your code 
    word = input("Guess:")
    print(word)

print ("You scored: " + str(score))    




    
    
