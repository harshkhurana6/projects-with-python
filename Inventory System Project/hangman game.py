#importing random modulue
import random

#Now we will make the user enter his/her name
name=input("What is your name?:")
print("Good Luck!"+name)

words=["ranbow","computer","science","programming","python","mathematics","player","condition","revrse","water","board","geeks"]

#fuction will choose one random word
#word from this list of words
word = random.choice(words)

print("Guess the Characters")
guesses=''
turns=12

while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")

            #for every failure
            #1 will be incremented in failure
            failed+=1

    if failed==0:
        #user will win
        print("You win")
        print("The word is:",word)
        break
    guess=input("guess a character:")
    guesses+=guess

    if guess not in word:
        turns-=1
        print("Wrong")

        print("You have",+turns,"more guesses")

        if turns==0:
            print("You lose")
