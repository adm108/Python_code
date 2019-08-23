""" Would you like to see a binary, octal, hexadecimal and roman number
versions of your arabic (decimal) number? Check this out! """


def arabic_to_rom(number):
    roman = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L",
             90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
    result_string = ""
    while number > 0:
        value = find_max_in_dic(roman.keys(), number)
        result_string += roman[value]
        number -= value
    return result_string


def find_max_in_dic(dic, number):
    result = None
    for value in dic:
        if number >= value:
            result = value
        else:
            break
    return result


def arabic_to_binary(number):
    my_list = []
    while number > 0:
        if number % 2 == 0:
            my_list.append(0)
            number = number / 2
        else:
            my_list.append(1)
            number = number // 2
    result = ""
    for element in reversed(my_list):
        result = result + str(element)
    return result


def binary_to_arabic(number):
    result = 0
    for index, item in enumerate((number[::-1])):
        if item == 1:
            result = result + 2 ** index
        else:
            continue
    return result


def binary_to_hex(number):
    binary = []
    for item in number:
        binary.append(int(item))

    if len(binary) % 4 == 1:
        for index in range(0, 3):
            binary.insert(0, 0)
    elif len(binary) % 4 == 2:
        for index in range(0, 2):
            binary.insert(0, 0)
    elif len(binary) % 4 == 3:
        for index in range(0, 1):
            binary.insert(0, 0)

    number_holder = []
    decimal_set = []
    hex_number = ""

    while len(binary) != 0:
        for index in range(0, 4):
            number_holder.append(binary.pop(0))
        decimal_set.append(binary_to_arabic(number_holder))
        number_holder = []

    for index in decimal_set:
        if index == 10:
            hex_number += "A"
        elif index == 11:
            hex_number += "B"
        elif index == 12:
            hex_number += "C"
        elif index == 13:
            hex_number += "D"
        elif index == 14:
            hex_number += "E"
        elif index == 15:
            hex_number += "F"
        else:
            hex_number += str(index)

    return hex_number


def binary_to_oct(number):
    binary = []
    for item in number:
        binary.append(int(item))

    if len(binary) % 3 == 1:
        for index in range(0, 2):
            binary.insert(0, 0)
    elif len(binary) % 3 == 2:
        for index in range(0, 1):
            binary.insert(0, 0)

    number_holder = []
    decimal_set = []
    oct_number = ""

    while len(binary) != 0:
        for index in range(0, 3):
            number_holder.append(binary.pop(0))
        decimal_set.append(binary_to_arabic(number_holder))
        number_holder = []

    for index in decimal_set:
        oct_number += str(index)

    return oct_number


if __name__ == "__main__":
    print("Hello in arabic number converter.\n\nYou can put a positive "
          "number and the program show you: binary, octal, hexadecimal "
          "and roman versions of your number. \nRemember! If you put a "
          "number greater than 3999 converter will not show you result "
          "of room number. The largest number that can be represented "
          "in this notation is 3999.\n")
    while True:
        try:
            my_number = int(input("Give a positive number: "))
            if my_number < 0:
                print("\nWrong value. Enter a positive number!\n")
                continue
            elif my_number < 3999:
                print(f"\nBinary number of {str(my_number)} is: "
                      f"{arabic_to_binary(my_number)}")
                print(f"Octal number of {str(my_number)} is: "
                      f"{binary_to_oct(arabic_to_binary(my_number))}")
                print(f"Hex number of {str(my_number)} is: "
                      f"{binary_to_hex(arabic_to_binary(my_number))}")
                print(f"Roman number of {str(my_number)} is: "
                      f"{arabic_to_rom(my_number)}")
            else:
                print(f"\nBinary number of {str(my_number)} is: "
                      f"{arabic_to_binary(my_number)}")
                print(f"Octal number of {str(my_number)} is: "
                      f"{binary_to_oct(arabic_to_binary(my_number))}")
                print(f"Hex number of {str(my_number)} is: "
                      f"{binary_to_hex(arabic_to_binary(my_number))}")
                print("The largest number that can be represented in roman "
                      "notation is 3999!")
        except ValueError:
            print("\nWrong value. Try again.\n")
            continue

        shall_continue = input("\nDo you want to continue [y / n] : ")
        print()
        if shall_continue != "y":
            break
