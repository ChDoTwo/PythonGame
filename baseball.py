from random import randint


def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")

    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    while len(new_guess) < 3:
        num = int(input("{}번째 숫자를 입력하세요: ".format(len(new_guess)+1)))
        if num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")    
        elif num < 0 or num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(num)

    return new_guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(len(solution)):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count


ANSWER = generate_numbers()
tries = 0
while True:
    USER = take_guess()
    strike, ball = get_score(USER, ANSWER)
    print("{}S {}B".format(strike, ball))
    print()
    if strike == 3:
        print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries + 1))
        break
    else:
        tries += 1
    