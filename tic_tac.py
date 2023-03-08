a = list(" " * 9)
step = 0
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
possible_values = [1, 2, 3]


def print_game():
    print('-' * 9)
    for i in range(3):
        print("| {} {} {} |".format(a[0 + 3 * i], a[1 + 3 * i], a[2 + 3 * i]))
    print('-' * 9)


print_game()

while True:
    x, y = input().split()
    if int(x) not in numbers or int(y) not in numbers:
        print("You should enter numbers!")
    elif int(x) not in possible_values or int(y) not in possible_values:
        print("Coordinates should be from 1 to 3!")
    elif a[(int(x) - 1) * 3 + (int(y) - 1)] != ' ':
        print("This cell is occupied! Choose another one!")
    else:
        if step % 2 == 0:
            a[(int(x) - 1) * 3 + (int(y) - 1)] = 'X'
            step += 1
        elif step % 2 == 1:
            a[(int(x) - 1) * 3 + (int(y) - 1)] = 'O'
            step += 1
        print_game()
        winner_position = [a[:3], a[3:6], a[6:], a[0:9:3], a[1:9:3], a[2:9:3], a[0:9:4], a[2:7:2]]
        if ['X', 'X', 'X'] in winner_position:
            print("X wins")
            break
        elif ['O', 'O', 'O'] in winner_position:
            print("O wins")
            break
        elif a.count(" ") == 0:
            print("Draw")
            break
