def pick_secret():
    '''bez argumentów
        wybiera randomowo słow0
        return str: word'''
    import random
    temp_lista = []
    with open('proverbs.txt') as file:
        for line in file:
            line = line.strip()
            temp_lista.append(line)
    return random.choice(temp_lista)


def get_hashed(sentence):
    ''' arg: word
        zamienia word na  _ _
        zatrzymuje spacje jako spacje
        return str: hashed_password'''
    wordh = ""
    for i in range(len(sentence)):
        if sentence[i] == chr(32):
            wordh += " "
        else:
            wordh += "."
    return wordh


def uncover(hash_passw, passw, lett):
    ''' arg: jak wyżej
        zamiania odgadnieta na literę
        return: zmodyfikowane hashed_password'''
    temporary = ""
    for i in range(len(passw)):
        if lett == passw[i] and not(hash_passw[i].isalpha()):
            temporary += passw[i]
        else:
            if passw[i] == chr(32):
               temporary += ' '
            else:
                temporary += hash_passw[i]
    return temporary


def update(used_lett, lett):
    ''' dodaje litery do used_letters
        return: updated used_letters'''
    used_lett.append(lett)
    print("list of used letters:", end = " ")
    for item in used_lett:
        print( item, end = " ")
    print("")


def is_win(hash_passw, passw):
    ''' sprawdza czy są identyczne
        zwraca: TRUE'''
    if hash_passw == passw:
        return False
    else:
        return True


def is_loose(life):
    ''' if life_points == 0
        return: bool (TRUE)'''
    if life == 0:
        return False
    else:
        return True


def get_input():
    '''reads user input until only letters
        return: str (validated input)'''
    wsad = input("\nGuess the proper letter:")
    wsad = wsad.upper()
    return wsad   

# ===========


password = ""
hashed_password = ""
used_letters = []
life_points = 5
player_in = ""

password = pick_secret().upper()
hashed_password = get_hashed(password)
print("\nTry to uncode the secret English proverb (only 5 mistakes allowed)\n")
print(hashed_password)
print('')
while is_loose(life_points) and is_win(hashed_password, password):
    player_in = get_input()
    if password.find(player_in) < 0:
        life_points -= 1
        print(hashed_password)
        print("You may still make " + str(life_points) + " mistakes")
        update(used_letters, player_in)
    else:
        hashed_password = uncover(hashed_password, password, player_in)
        print(hashed_password)
        update(used_letters, player_in)
if life_points == 0:
    print("\nUnfortunately, you are the looser. Game Over")
    print("The salution was: " + password)
else:
    prob = 5 - life_points
    print("\nCongratulation!!! You make only " + str(prob) + " mistakes to guess coded proverb")
    print(password)