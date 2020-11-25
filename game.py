from random import randint

class CreateBot():

    def __init__(self, bot_name, bot_color, bot_pos, bot_tip):
        self.bot_name = bot_name
        self.bot_color = bot_color
        self.bot_pos = bot_pos
        self.bot_tip = bot_tip

    def new_bot(self, arr):
        for i in range(n):
            for j in range(n):
                match_struct = ([i+1],[j+1])
                if match_struct == self.bot_pos:
                    if self.bot_tip == 'Bot':
                        arr[i][j] = 'XXX'
                    else:
                        arr[i][j] = 'YYY'

        return arr

    def print_board(self, arr):
        for i in range(n):
            for j in range(n):
                pass
            print("".join(arr[i]))
        print(' ')

    def move_bot(self, arr, arr_bots_pos, where_move):
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 'YYY':

                    match_struct = ([i+1], [j+1])
                    for a in range(n):
                        if arr_bots_pos[a] == match_struct:
                            if where_move == 'Up':
                                arr_bots_pos[a] = ([i-1], [j])
                            elif where_move == 'Down':
                                arr_bots_pos[a] = ([i+1], [j])
                            elif where_move == 'Left':
                                arr_bots_pos[a] = ([i], [j-1])
                            elif where_move == 'Right':
                                arr_bots_pos[a] = ([i], [j+1])
                    x = i
                    y = j
                    arr[i][j] = '---'

        if where_move == 'Up':
            arr[x-1][y] = 'YYY'
        elif where_move == 'Down':
            arr[x+1][y] = 'YYY'
        elif where_move == 'Left':
            arr[x][y-1] = 'YYY'
        elif where_move == 'Right':
            arr[x][y+1] = 'YYY'

        return arr_bots_pos

def generate_bot(x, unique_arr):
    fist_value = randint(1, x)
    second_value = randint(1, x)
    bot_value = ([fist_value],[second_value])
    while True:
        elem_unique = False
        for ind in range(x):
            if bot_value != unique_arr[ind]:
                elem_unique = True
            else:
                fist_value = randint(1, x)
                second_value = randint(1, x)
                elem_unique = False
                break
        if elem_unique == True:
            break

    return bot_value

n = 10

arr = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr[i][j] = '---'

bot_unique_arr = [0] * n

bot_unique_arr[0] = generate_bot(n, bot_unique_arr)
Hrummy = CreateBot('Hrummy', 'Green', bot_unique_arr[0],'Bot')
Hrummy.new_bot(arr)

bot_unique_arr[1] = generate_bot(n, bot_unique_arr)
Truffie = CreateBot('Truffie', 'Green', bot_unique_arr[1],'Bot')
Truffie.new_bot(arr)

bot_unique_arr[2] = generate_bot(n, bot_unique_arr)
Flutter = CreateBot('Flutter', 'Green', bot_unique_arr[2],'Bot')
new_arr = Flutter.new_bot(arr)

bot_unique_arr[3] = generate_bot(n, bot_unique_arr)
Slip = CreateBot('Slip', 'Green', bot_unique_arr[3],'Player')
new_arr = Slip.new_bot(arr)

Slip.print_board(new_arr)


while True:
    input_value = input()
    try:
        if input_value == 'w':
            new_bot_unique = Slip.move_bot(new_arr, bot_unique_arr, 'Up')
            Slip.print_board(new_arr)
        elif input_value == 's':
            new_bot_unique = Slip.move_bot(new_arr, bot_unique_arr, 'Down')
            Slip.print_board(new_arr)
        elif input_value == 'd':
            new_bot_unique = Slip.move_bot(new_arr, bot_unique_arr, 'Right')
            Slip.print_board(new_arr)
        elif input_value == 'a':
            new_bot_unique = Slip.move_bot(new_arr, bot_unique_arr, 'Left')
            Slip.print_board(new_arr)
        else:
            break

    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        break