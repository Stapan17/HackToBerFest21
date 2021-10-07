slot = [' '] *9
player_one = input('Player 1 name: ')
player_two = input('Player 2 name: ')
chance = player_one
turn = 0


def base_board():
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")


def main_board():
    print(f' {slot[0]} | {slot[1]} | {slot[2]} ')
    print("---|---|---")
    print(f' {slot[3]} | {slot[4]} | {slot[5]} ')
    print("---|---|---")
    print(f' {slot[6]} | {slot[7]} | {slot[8]} ')


def user_input():
    if turn%2==0:
        chance = player_one

    else:
        chance = player_two

    print(f"{chance}'s turn")
    option = int(input('Enter the slot to be filled: '))
    if option in range(1,10) :
        if slot[option-1] == ' ' :
            if chance == player_one :
                slot[option-1] = 'O'

            else :
                slot[option-1] = 'X'


        else :
            print("This slot is already filled, choose a different one")
            user_input()


    else :
        print("This is an invalid slot, please enter a slot between 1 to 9")
        user_input()


def win_situation():
    print(f'{chance} is the winner!')
    exit()


def win_condition():
    for n in [0,3,6]: #horizontal
        if slot[n]==slot[n+1]!=' ' and slot[n+1]==slot[n+2] :
            main_board()
            win_situation()


    for n in [0,1,2]: #vertical
        if slot[n]==slot[n+3]!=' ' and slot[n+3]==slot[n+6] :
            main_board()
            win_situation()

    for n in [0]: #leading diagonal
        if slot[n]==slot[n+4]!=' ' and slot[n+4]==slot[n+8] :
            main_board()
            win_situation()

    for n in [2]: #other diagonal
        if slot[n]==slot[n+2]!=' ' and slot[n+2]==slot[n+4] :
            main_board()
            win_situation()



if __name__ == '__main__':
    while True:
        base_board()
        print('\n')
        main_board()
        user_input()
        win_condition()
        turn = turn + 1
        if turn == 9:
            print("The Game is drawn!")
            main_board()
            exit()