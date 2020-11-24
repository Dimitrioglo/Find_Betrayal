from random import randint

class CreateBot():

    def __init__(self, bot_name, bot_color, bot_pos):
        self.bot_name = bot_name
        self.bot_color = bot_color
        self.bot_pos = bot_pos

    def new_bot(self, arr):
        for i in range(n):
            for j in range(n):
                match_struct = ([i+1],[j+1])
                if match_struct == self.bot_pos:
                    arr[i][j] = 'XXX'

        return arr

    def print_bot(self, arr):
        for i in range(n):
            for j in range(n):
                pass
            print("".join(arr[i]))
        print(' ')

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

bot_unique_arr = [0] * n
bot_unique_arr[0] = generate_bot(n, bot_unique_arr)

Hrummy = CreateBot('Hrummy', 'Green', bot_unique_arr[0])

arr = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr[i][j] = '---'

Hrummy.new_bot(arr)

bot_unique_arr[1] = generate_bot(n, bot_unique_arr)
Truffie = CreateBot('Truffie', 'Green', bot_unique_arr[1])
Truffie.new_bot(arr)

bot_unique_arr[2] = generate_bot(n, bot_unique_arr)
Flutter = CreateBot('Flutter', 'Green', bot_unique_arr[2])
new_arr = Flutter.new_bot(arr)

Flutter.print_bot(new_arr)
