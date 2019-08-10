""" Most common math algorithms below! """


# ---------------------------- FIBONACCI SEQUENCE ----------------------------

def fibonacci(number_of_values):
    if number_of_values < 0:
        return "wrong value!"
    elif number_of_values <= 0:
        return []
    a = 1
    b = 1
    fibonacci_list = [0]
    for i in range(number_of_values - 1):
        fibonacci_list.append(a)
        a, b = b, a + b
    return fibonacci_list


# -------------------------------- FACTORIAL ---------------------------------

def factorial_recursion(number):
    if number < 0:
        return "wrong value!"
    elif number <= 1:
        return 1
    else:
        return number * factorial_recursion(number - 1)


def factorial_while_loop(number):
    if number < 0:
        return "wrong value!"
    result = 1
    while number >= 1:
        result *= number
        number -= 1
    return result


def factorial_for_loop(number):
    if number < 0:
        return "wrong value!"
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


# ------------------------- GREATEST COMMON DIVISOR --------------------------

def greatest_common_divisor_for_loop(x, y):
    if x > y:
        small = y
    else:
        small = x
    gcd = None
    for i in range(1, abs(small) + 1):
        if x % i == 0 and y % i == 0:
            gcd = i
    return gcd


def greatest_common_divisor_while_loop(x, y):
    while y > 0:
        x, y = y, x % y
    return x


# ---------------------------- COLLATZ CONJECTURE ----------------------------

collatz_list = []


def collatz_conjecture_recursion(number):
    if number < 1:
        return collatz_list
    elif number == 1:
        collatz_list.append(number)
        return collatz_list
    elif number % 2:
        collatz_list.append(number)
        return collatz_conjecture_recursion(number * 3 + 1)
    else:
        collatz_list.append(number)
        return collatz_conjecture_recursion(number // 2)


def collatz_conjecture_while_loop(number):
    if number < 1:
        return []
    collatz_result = []
    while number != 1:
        if number % 2:
            collatz_result.append(number)
            number = number * 3 + 1
        else:
            collatz_result.append(number)
            number = number // 2
    collatz_result.append(1)
    return collatz_result


print(fibonacci(15))
# print(factorial_recursion(15))
# print(factorial_while_loop(15))
# print(factorial_for_loop(15))
# print(greatest_common_divisor_for_loop(15, 65))
# print(greatest_common_divisor_while_loop(15, 65))
# print(collatz_conjecture_recursion(75))
# print(collatz_conjecture_while_loop(75))
