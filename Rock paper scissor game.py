import random

GAME_CHOICES = ("r", "p", "s")  # Rock, Paper, Scissors

RULES = {
    ('p', 'r'): 'p',
    ('p', 's'): 's',
    ('r', 's'): 'r',
}

scoreboard = {
    'user': 0,
    'system': 0
}

def get_user_choice():
    user_input = input('Enter your choice please (r, p, s): ')
    if user_input not in GAME_CHOICES:
        print("Oops!!, wrong choice, try again please...")
        return get_user_choice()
    return user_input


def get_system_choice():
    return random.choice(GAME_CHOICES)


def find_winner(user, system):
    match = {user, system}
    if len(match) == 1:
        return None
    return RULES[tuple(sorted(match))]


def update_scoreboard(result):
    if result['user'] == 3:
        scoreboard['user'] += 1
        msg = 'You win'
    else:
        scoreboard['system'] += 1
        msg = 'You lose'
    print("#" * 30)
    print("##", f'user: {scoreboard["user"]}'.ljust(24), "##")
    print("##", f'system: {scoreboard["system"]}'.ljust(24), "##")
    print("##", f'last game: {msg}'.ljust(24), "##")
    print("#" * 30)

    if scoreboard['user'] == game_times:
        print("YOU WIN".center(30,"*"))
        exit()
    if scoreboard['system'] == game_times:
        print("YOU LOSE".center(30,"*"))
        exit()
def play():
    result = {'user': 0, 'system': 0}
    while result['user'] < 3 and result['system'] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = find_winner(user_choice, system_choice)

        if winner == user_choice:
            msg = 'You win'
            result['user'] += 1
        elif winner == system_choice:
            msg = 'You lose'
            result['system'] += 1
        else:
            msg = "Draw"
        print(f"user: {user_choice}\t system: {system_choice}\t result: {msg}")

    update_scoreboard(result)
    play_again()


def play_again():
    choice = input("Do you want to play again? (y/n)")
    if choice == 'y' or choice == 'yes':
        play()
    elif choice == 'n' or choice == 'no':
        exit()
    else:
        print("Invalid input!\tPlease say y(yes) or n(no). ")
        play_again()
def game_times_func():
    try: 
        global game_times 
        game_times = int(input("How many times do you want to play for a win? "))
    except: 
        print("Invalid input, please try again.")
        game_times_func()

if __name__ == '__main__':
    game_times_func()
    play()
