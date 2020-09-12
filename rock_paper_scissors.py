import random
from word2number import w2n

options = ["rock","paper","scissor"]
program_win = 0
user_win = 0
both_equal = 0
turn = 0
result = ""
num_of_games = 0
#unpacking
rock,paper,scissor = options

def terminal_commands():
    '''Show user which command to type.'''
    print(''' 
Welcome To Rock, Paper and Scissor Game.
    Type Help To Get Full Information
    ''')
    while True:
        user_input = input(">> ").lower()
        if user_input == "start":
            play_game()
        elif user_input == "exit":
            break
        else:
            print('''
------------------------------------------------------------------------------------------------------------------
Help    ---->       To Get Availible Commands
Start   ---->       To Start The Game
exit    ---->       To Exit  Game Terminal   
''')


def make_move():
    ''' This function is resposible to take user input for rock, paper or scissor and return user input '''
    while True:
        u_move = input("what is in your mind? (rock, paper or scissor) : ")
        u_move = u_move.lower()
        if not move_validaty(u_move):
            print ('''
                You can only choose between:
                Rock        Or      (r)
                Paper       Or      (p)
                Scissor     Or      (s)
            ''')
        else:
            break
    return collect_result(u_move)

def move_validaty(move):
    ''' This function is resposible to check if the user input for rock, scissor and paper is valid or not and return True or False. '''
    found = False
    for full_name in options:
        if move == full_name:
            found =  True
    return found


def collect_result(u_move):
    '''This function check the user input with the computer predictions and calculate the win numbers'''
    global program_win
    global user_win
    global both_equal
    data = None
    winner = None
    program_move = random.choice(options)
    if u_move == program_move:
        both_equal +=1
    else:
        if u_move == scissor:
            if program_move == paper:
                user_win += 1
            elif program_move == rock:
                program_win +=1
        elif u_move == paper:
            if program_move == scissor:
                program_win += 1
            elif program_move == rock:
                user_win +=1
        elif u_move == rock:
            if program_move == scissor:
                user_win += 1
            elif program_move == paper:
                program_win +=1
    print(f"Programm have choosed: {program_move}")


def check_winner(u_win,p_win):
    '''This function check who is the winner'''
    status = None
    if u_win == p_win:
        status = "Equal"
    elif u_win > p_win:
        status = "Congratulations User is the Winner"
    else:
        status = "Oops! better Luck Next Time"
    data = dict([('Games Played',num_of_games),("User Wins",user_win),("Program Wins",program_win),('Equal',both_equal),("status",status)])
    return data


def try_again():
    '''Play The game after it has been finished'''
    while True:
        again = input("Play Again? (Yes/Y)or(No/N): ").lower()
        if again == "y" or again == "yes":
            global program_win 
            global user_win 
            global both_equal 
            global turn 
            global result
            program_win , user_win, turn , both_equal = 0,0,0,0
            result = ""
            play_game()
            break
        elif again == "n" or again == "no":
            terminal_commands()
            break
        else: 
            print('''
------------------------------------------------------------------------------------------------------------------
Yes(Y)  ---->       Play Again
No(N)   ---->       Return to Terminal
 
            ''')


def play_game():
    '''Play the game and if game is finished then call try again mehtod and it prints the final result.'''
    global turn
    global num_of_games
    while True:
        try:
            num_of_games = int( w2n.word_to_num(input("\nPlease Type the number of games You want to play: ",)))
            while turn < num_of_games:
                make_move()
                turn +=1
            print(''' 
----------------------------------------------------------------------------------------------------------------
Game Completed

Result:
''')
            print(check_winner(user_win,program_win),end="\n \n")
            try_again()
            break
        except ValueError:
            print("Add Only number to the system")


terminal_commands()