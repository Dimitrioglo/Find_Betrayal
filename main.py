from random import randint

def generate_bot(x):
    fist_value = randint(1, x)
    second_value = randint(1, x)
    bot_value = ([fist_value],[second_value])
    return bot_value

def battleField():
    n = 10
    first_bot = generate_bot(n)

    second_bot_cond = False
    while second_bot_cond == False:
        second_bot = generate_bot(n)
        if second_bot != first_bot:
            second_bot_cond = True
    third_bot_cond = False

    while third_bot_cond == False:
        third_bot = generate_bot(n)
        if ((third_bot != first_bot) and (second_bot != third_bot)) :
            third_bot_cond = True

    li = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            array_value = ([i+1], [j+1])
            if (array_value == first_bot) or (array_value == second_bot) or (array_value == third_bot):
                li[i][j] = 'XXX'
            else:
                li[i][j] = '---'
        print("".join(li[i]))

battleField()

