import random

def hangman(Mylist):


    Lives = 8
    i = 0
    unguessedWord = []
    
    playWord = Mylist[random.randint(0,len(Mylist)-1)]
    print(playWord)
    for x in playWord:
        unguessedWord.append("_")



    isGameOver = False

    playWordListed = list(playWord)
    playWordListed
    playWordListedComparison = playWordListed[:]

    while i < Lives:


        

        guess = input("Please enter your letter guess : ")

        for j in range(len(playWordListedComparison)):
            if guess == playWordListedComparison[j]:
                unguessedWord[j] = guess
                playWordListedComparison[j] = '#'
                print(playWordListedComparison)
                break
                
            j += 1
        print(unguessedWord)
        print(playWordListed)
        i += 1

        if unguessedWord == playWordListed:
            isGameOver = True
            break


    if isGameOver == True:
        print("You won!!!")
    else:
        print("you lost!!!")
    
    


    







ListOfWords = ["apple", "orange", "banana"]

hangman(ListOfWords)

