"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
import numpy as np
number = np.random.randint(1, 101)  # загадали число

def random_predict(number):
    count = 1
    lower_value = 1
    upper_value = 100
    predict = 50
    while number != predict:
        predict = (lower_value + upper_value) // 2
        count += 1
        if number > predict:
            lower_value = (lower_value + upper_value) // 2 + 1
        elif number < predict:
            upper_value = (lower_value + upper_value) // 2 - 1
    return (count)  # выход из цикла, если угадали

def score_game(random_predict) -> int:
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)

if __name__ == "__main__":
    # RUN
    score_game(random_predict)