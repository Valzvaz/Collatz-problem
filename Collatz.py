def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = 3 * number + 1
            print(number)
while True:
    print('Put the number...')
    try:
        n = int(input())
        collatz(n)
    except ValueError:
        print("That wasn't integer!")
