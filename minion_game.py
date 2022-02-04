import string

S = "Rhythms"




def minion_game(string):
    VOWEL = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    STUART = 0
    KEVIN = 0
    for i in range(len(string)):
        if S[i] in VOWEL:
            KEVIN += len(string) - i
            print((S[i]))

        if S[i] not in VOWEL:
            STUART += len(string) - i

    if STUART > KEVIN:
        print("Stuart " + str(STUART))
    elif KEVIN > STUART:
        print("Kevin " + str(KEVIN))
    else:
        print("Draw")


minion_game(S)
