import numpy as np


def guess_number(number):
    count = 1
    lower_border = 1  # нижняя граница диапазона
    upper_border = 100  # верхняя граница диапазона
    predict = np.random.randint(1, 101)  # задаем случайное число, которое будем сравнивать с искомым
    while number != predict:
        count += 1
        if number > predict:  # если искомое число больше случайного числа
            lower_border = predict  # увеличиваем нижнюю границу диапазона в котором будем искать число
            predict = (lower_border + upper_border) // 2  # задаём число в новом диапазоне
        elif number < predict:  # если искомое число меньше случайного числа
            upper_border = predict  # уменьшаем верхнюю границу диапазона в котором будем искать число
            predict = (lower_border + upper_border) // 2  # задаём число в новом диапазоне
    return count


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=200)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(guess_number)
