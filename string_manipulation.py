# *******      TASK 5       *******
# ******* Compulsory Task 3 *******
# *******  manipulation.py  *******
# ------------ xxx ----------------

# Here we have utilize different string methods

str_manip = input("Enter any Sentence : ")

# Finding length of the str_manip
print(f"The length of your sentence is {len(str_manip)}")

# Finding last letter of the sentence and replacing it's all occurrence with @
last_letter = str_manip[-1]
print(f"The last letter is {last_letter} and new sentence is {str_manip.replace(last_letter, '@')} ")

# Printing out last three letter of the sentence in reverse order
print(f"The last 3 character in backward order are {str_manip[:-4:-1]}")

# Creating and outputting the word from first 3 and last 2 letter from the sentence
five_letter_word = str_manip[0:3] + str_manip[-2:]
print(f"The Five letter word is : {five_letter_word}")

# Stripping character in the front and back of the word or sentences
hero = "$$$Superman$$$"
hero = hero.strip("$")
print(hero)

# This section invoves replacing and reversing string variables

english_alphabet = "The!quick!brown!fox!jumps!over!the!lazy!dog!"

# Replacing letters from the string
english_alphabet = english_alphabet.replace("!", " ")
print("Replaced String : \n",english_alphabet)

# Changing letters to uppercase alphabet
print("Uppercase String : \n",english_alphabet.upper())

# Reversing the String
print("Reversed String is :\n",english_alphabet[::-1])

