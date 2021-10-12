import random as rd
'''
Rock beats Scissors
Scissors beats Paper
Paper beats Rock
'''

scissor = 's'
rock = 'r'
paper = 'p'

ai_choice = (scissor , rock , paper)


win = 0
loss = 0
draw = 0

player = input('What is your name, player?\n')

def rock_paper_scissors_game(win,loss,draw):
    globals()
    for i in range(3):
        result = "".join(rd.choice(ai_choice))
        user_choice = input("Please choose either (r)ock , (p)aper, or (s)cissor:  ")
        if result == 's':
            print('Computer chose Scissors')            
            if user_choice == 'r':
                win += 1
                print(player + " won this round!\n")
            elif user_choice == 's':
                draw += 1
                print(player + ", this is a draw !\n")
            else:
                loss += 1
                print(player + " lost this round!\n")
        elif result == 'r':
            print('Computer chose Rock')
            if user_choice == 'p':
                win += 1
                print(player + " won this round!\n")
            elif user_choice == 'r':
                draw += 1
                print(player + ", this is a draw !\n")                
            else:
                loss += 1
                print(player + " lost this round!\n")
        elif result == 'p':
            print('Computer chose Paper')
            if user_choice == 's':
                win += 1
                print( player + " won this round!\n")
            elif user_choice == 'p':
                draw += 1
                print( player + ", this is a draw !\n")            
            else:
                loss += 1
                print(player + " lost this round!\n")    
    
    
    print("Total Wins=" +str(win))
    print("Total Losses=" + str(loss))
    print()
    return win , loss , draw

def did_user_win(win,loss,draw):
    win , loss , draw = rock_paper_scissors_game(win,loss,draw)
    if win >= 2 and loss < 2:
        retry = input("Conrgatulations, " + player + ", you won the game!\nWould you like to continue? y/n\n")
        if retry.lower() == 'y':
            win = 0
            loss = 0
            draw = 0
            did_user_win(win,loss,draw)
        else:
            print('Thank you, ' +player+' for playing')
    elif win == 1 or loss == 1 and draw >= 1:
        retry = input("Looks like it was a draw, " + player + ".\nWould you like to continue? y/n\n")
        if retry.lower() == 'y':
            win = 0
            loss = 0
            draw = 0
            did_user_win(win,loss,draw)
        else:
            print('Thank you, ' +player+' for playing')
    elif win == 2 and draw == 1:
        retry = input("Conrgatulations, " + player + ", you won the game!\nWould you like to continue? y/n\n")
        if retry.lower() == 'y':
            win = 0
            loss = 0
            draw = 0
            did_user_win(win,loss,draw)
        else:
            print('Thank you, ' +player+' for playing')
    else:
        retry = input("Sorry, " + player + ", you didn't win, would you like to retry? y/n\n")
        if retry.lower() == 'y':
            win = 0
            loss = 0
            draw = 0
            did_user_win(win,loss,draw)
        else:
            print('Thank you, ' +player+', for playing')


def main():
    did_user_win(win,loss,draw)
    
if __name__ == "__main__":
    main()