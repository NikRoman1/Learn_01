# import time
#
# # Функция для вычисления чисел Фибоначчи без мемоизации
# def fibonacci(n):
#     print(n)
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         a = fibonacci(n - 1) + fibonacci(n - 2)
#         print(n, a)
#         return a
#
# # Функция для вычисления чисел Фибоначчи с мемоизацией
# def fibonacci_memo(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#
#     memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
#     print(n, memo[n])
#     return memo[n]
#
# # Измерение времени выполнения функции без мемоизации
# start_time = time.time()
# fi = fibonacci(10)  # Вычислим для n = 30, чтобы не занимать слишком много времени
# time_without_memo = time.time() - start_time
# print(f"Время без мемоизации: {time_without_memo:.6f} секунд {fi}")
#
# # Измерение времени выполнения функции с мемоизацией
# start_time = time.time()
# fim = fibonacci_memo(10)  # Вычислим для n = 30
# time_with_memo = time.time() - start_time
# print(f"Время с мемоизацией: {time_with_memo:.6f} секунд {fim}")



# def filter_odd_numbers(numbers):
#     return list(filter(lambda x: x%2, numbers))
#
# odd_numbers = filter_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(odd_numbers)  # Ожидаемый вывод: [1, 3, 5, 7, 9]



# def my_power(base: float, exp: int):
#     if exp == 0:
#         return 1
#     return base * my_power(base, exp - 1)
#
# result = my_power(3, 5)
# print(result) #Ожидаемый вывод: 8



# def my_generator():
#     for a in range('a', 'z'):
#         yield a


# # gen = my_generator()
# for i in range('a', 'z'):
#     print(i)
# print(12)
# # gen = my_generator()
# # print(next(gen))  # Вывод: 1
# # print(next(gen))  # Вывод: 2
# # print(next(gen))  # Вывод: 3
# # print(next(gen))  # Вывод: 3



# def counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     return increment
#
# my_counter = counter()
# print(my_counter())  # Вывод: 1
# print(my_counter())  # Вывод: 2
# print(my_counter())  # Вывод: 2
# print(my_counter())  # Вывод: 2
# my_counter = counter()
# print(my_counter())  # Вывод: 1
# print(my_counter())  # Вывод: 2
# print(my_counter())  # Вывод: 2



# def logger(prefix):
#     def log_message(message):
#         print(f"\033[31m[", end='')
#         print(f"{prefix}] \033[0m{message}")
#     return log_message
#
# info_logger = logger("INFO")
# error_logger = logger("ERROR")
#
# info_logger("Это информационное сообщение.")
# error_logger("Это сообщение об ошибке.")
# info_logger("Это информационное сообщение 2.")
# info_logger("Это информационное сообщение 3.")
# # Вывод:
# # [INFO] Это информационное сообщение.
# # [ERROR] Это сообщение об ошибке.


# Декораторы
#import time

# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#
#         start_time = time.time()
#         print(*args)
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         # раскраска текста
#         print(f"\033[31m\033[43m[", end='') if end_time - start_time > 0.01 else print(f"\033[32m[", end='')
#         print(f"Время выполнения функции '{func.__name__}': {end_time - start_time:.6f} секунд")
#         print(f"\033[0m[", end='')
#         return result
#     return wrapper
#
# @timing_decorator
# def compute_square(n):
#     return sum([i ** 2 for i in range(n)])
#
# # Вызов функции
# print(compute_square(10000))


# Заглушка
# def dumb(func):
#     def damb_wraper(*args, **kwargs):
#         1+1
#         #print(*args, 'XEXE')
#     return damb_wraper
#
# @dumb
# def qwert(a: str = '' ):
#     print(a, 'sdfesr')
#     return None
#
# qwert('asd')



# import keyboard

# while True:
#     keyboard.wait("1")
#     keyboard.write("\n The key '1' was pressed!")

# recorded_events = keyboard.record("esc")
# keyboard.play(recorded_events)




