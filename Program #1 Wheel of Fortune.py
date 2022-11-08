# All phrases that are prepared to be choosed
phrase = ["Rosebud", "Less is more", "Inconceivable!", "Never going to give you up",
          "The unexamined life is not worth living",
          "My name is Inigo Montoya, you killed my father, prepare to die!"]


# Get user input and choose the phrase, and return chosen phrase
def choose_phrase():
    user_input = int(input()) % 6
    game_phrase = phrase[user_input - 1]
    return game_phrase.upper()


# Change phrase to '_' and ' '
def cover_phrase(phrase):
    new_phrase = []
    for index in range(len(phrase)):
        if phrase[index] == '!':
            new_phrase.append('!')
        elif phrase[index] == ',':
            new_phrase.append(',')
        elif phrase[index] != ' ':
            new_phrase.append('_')
        else:
            new_phrase.append(' ')
    return new_phrase


# Update answer
def update_covered_phrase(game_phrase, new_phrase, ch):
    count = 0
    for index in range(len(game_phrase)):
        if ch == game_phrase[index]:
            new_phrase[index] = ch
            count += 1
    return count


def convert(list):
    str = ''
    for ch in list:
        str += ch
    return str


def print_multi_lines(phrase):
    if len(phrase) > 39:
        print(phrase[0:25])
        print(phrase[26:47])
        print(phrase[48:])
    elif len(phrase) == 39:
        print(phrase[0:19])
        print(phrase[20:])
    else:
        print(phrase)


# Count how many times the letter shows in this phrase
def user_choose(letter, count_num, total, user_vowel = 'True'):
    if user_vowel == 'True':
        if count_num == 0:
            total -= 100
            print(f"There are no {letter}'s.")
            print_multi_lines(convert(covered_phrase))
            print(f'You have ${total}')
        
        else:
            total += count_num * 50
            print(f"There are {count_num} {letter}'s.")
            print_multi_lines(convert(covered_phrase))
            print(f'You have ${total}')

    else:
        total -= 50
        print(f"There are {count_num} {letter}'s.")
        print_multi_lines(convert(covered_phrase))
        print(f'You have ${total}')
        
    return total


# Check if user input 'g' or 'v'
def get_known_command(user_input):
    while (True):
        if user_input in ('g', 'v'):
            break
        print("I don’t know that command. Please enter ‘g’ or ‘v’:")
        user_input = input().lower()
    return user_input


# Begin the game
print('Welcome to Wheel of Fortune! Enter a number to begin the game.')
total_money = 200
chosen_phrase = choose_phrase()
covered_phrase = cover_phrase(chosen_phrase)
print_multi_lines(convert(covered_phrase))
print(f'You have ${total_money}')

while total_money > 0 and chosen_phrase != convert(covered_phrase):
    
    # Guess or buy a vowel
    print("Guess a letter ('g') or buy a vowel ('v')? ", end='')
    user_guess_buy = input().lower()
    user_verified = get_known_command(user_guess_buy)

    # Guess a letter
    if user_verified == 'g':
        print('Letter? ', end='')
        user_guess_letter = input().upper()
        count = update_covered_phrase(chosen_phrase, covered_phrase, user_guess_letter)
        total_money = user_choose(user_guess_letter, count, total_money)

    # Buy a vowel
    elif user_verified == 'v':
        print('What vowel do you buy? ', end='')
        user_buy_vowel = input().upper()
        count = update_covered_phrase(chosen_phrase, covered_phrase, user_buy_vowel)
        total_money = user_choose(user_buy_vowel, count, total_money, user_vowel = 'False')

# Check win or lose
if total_money <= 0:
    print('Sorry you lose the game...')

else:
    print('YOU HAVE WON WHEEL OF FORTUNE!')
    print(f'And you have won ${total_money}.')
