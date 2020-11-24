from random import randint

def generate_bot(x):
    fist_value = randint(1, x)
    second_value = randint(1, x)
    bot_value = ([fist_value],[second_value])
    return bot_value

def press_key(ind1, ind2, li):
    while True:
        input_value = input()
        try:  # used try so that if user pressed other than the given key error will not be shown
            if input_value == 'w':
                print('')
                for index1 in range(10):
                    for index2 in range(10):
                        if(li[index1][index2] == 'YYY'):
                            li[index1][index2] = '---'
                        elif (li[index1][index2] == '---') and (index1 == ind1 - 1) and (index2 == ind2):
                            li[index1][index2] = 'YYY'

                    print("".join(li[index1]))
                ind1 -= 1
            elif input_value == 'a':
                print('')
                for index1 in range(10):
                    for index2 in range(10):
                        if (li[index1][index2] == 'YYY'):
                            li[index1][index2] = '---'
                        elif (li[index1][index2] == '---') and (index2 == ind2 - 1) and (index1 == ind1):
                            li[index1][index2] = 'YYY'
                            ind2 -= 1
                    print("".join(li[index1]))
            elif input_value == 's':
                print('')
                for index1 in range(10):
                    for index2 in range(10):
                        if (li[index1][index2] == 'YYY'):
                            li[index1][index2] = '---'

                        elif (li[index1][index2] == '---') and (index2 == ind2) and (index1 == ind1 + 1):
                            li[index1][index2] = 'YYY'
                    print("".join(li[index1]))
                ind1 += 1
            elif input_value == 'd':
                print('')
                for index1 in range(10):
                    for index2 in range(10):
                        if (li[index1][index2] == 'YYY'):
                            li[index1][index2] = '---'
                        elif (li[index1][index2] == '---') and (index2 == ind2 + 1) and (index1 == ind1):
                            li[index1][index2] = 'YYY'

                    print("".join(li[index1]))
                ind2 += 1
            else:
                print("Oops! incorrect value")
                break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            break

def battleField():
    n = 10
    first_bot = generate_bot(n)

    while True:
        second_bot = generate_bot(n)
        if second_bot != first_bot:
            break

    while True:
        third_bot = generate_bot(n)
        if ((third_bot != first_bot) and (second_bot != third_bot)) :
            break

    while True:
        player  = generate_bot(n)
        if ((player != first_bot) and (player != second_bot) and (player != third_bot)) :
            break


    li = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            array_value = ([i+1], [j+1])
            if (array_value == first_bot) or (array_value == second_bot) or (array_value == third_bot):
                li[i][j] = 'XXX'
            elif array_value == player:
                li[i][j] = 'YYY'
                x = i
                y = j
            else:
                li[i][j] = '---'
        print("".join(li[i]))

    press_key(x, y, li)

battleField()

