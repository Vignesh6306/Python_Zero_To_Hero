def greetings():
    print("Welcome to the game ")
    global name, Age
    name = input("Enter Your name : ")
    Age = int(input("Enter your Age : "))

def Game_1(Answer = 'Apple'):
    global Score_1
    print("Guess the word")
    Hint = '''
    It is a 5 letter word 
    The word starts with A and ends with E
    '''
    print(Hint)
    guess = input("Enter your guess : ")
    if(guess == Answer):
        print("Your answer is correct")
        Score_1 = 1
    else:
        print("Your answer is wrong")

def Game_2():
    n = int(input("Enter the Number to Know its Multiples of (1-10) "))
    i = 0
    global Score_2
    Score_2 = 1
    while(i <= 10):
        print(n, '*', i, '=', (n*i))
        i += 1

def Game_3():
    print("What is the Answer for (4*5)+(3*10)-10")
    q = int(input("Enter your Answer : "))
    global Score_3

    if(q == 40):
        print("Your answer is correct")
        Score_3 = 1
    else:
        print("Try again")



def result():
    greet = greetings()
    print(greet)

    g1 = Game_1()
    print(g1)

    g2 = Game_2()
    print(g2)

    g3 = Game_3()
    print(g3)

    print("___Your Result___")
    print(name, Age, sep = '\n')
    Score = Score_1 + Score_2 + Score_3
    print('Total Score = ', Score)

result()







