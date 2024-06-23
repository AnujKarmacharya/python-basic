import random
cnt=True

print(""""Hello!!
Wecome to hangman""")

while cnt:

    attempt=10
    to_guess=[]
    guessed_words=[]
    guess_word=[]
    words=["kangroo","australia","vehicle"]
    ch=(random.choice(words))
    print(f"Hint:  Your word have {len(ch)} letters")
    

    for i in ch:
        guess_word.append("-")
        to_guess.append(i)

    while attempt!=0 and "-" in guess_word:

        inp=input("Enter a word:-")
        inp=inp.lower()
        
        if (len(inp)>1):
            print("Enter only one word")

        elif not inp.isalpha():
            print("You can only enter words")

        elif inp in guessed_words:
            print("Enter you have already guessed the word")

        else:
            guessed_words.append(inp)

            for i in range(len(to_guess)):

                if inp == to_guess[i]:
                    guess_word[i]=inp
                    print(guess_word)

            if inp not in to_guess:
                attempt-=1
                print("Word not found")
                print(f"You have {attempt} attempt left:")

    if "-" not in guess_word:
        print("Congratulation!! You won")
    
    if(attempt==0):
        print("Nice Try!! Better luck next time:")
    

    test=input("Do you want to continue:Y/N:-")
    if test.lower()=="y":
        cnt=True
    elif test.lower()=="n":
        cnt=False