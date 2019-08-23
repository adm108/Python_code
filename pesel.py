""" Program will tell you your date of birth (with day of the week),
sex and correctness of your PESEL number """

import datetime


def male_or_female(pesel):
    if pesel[9] in "02468":
        return "female"
    return "male"


def correctness_of_pesel(pesel):
    if (int(pesel[0]) + 3 * int(pesel[1]) + 7 * int(pesel[2]) +
        9 * int(pesel[3]) + int(pesel[4]) + 3 * int(pesel[5]) +
        7 * int(pesel[6]) + 9 * int(pesel[7]) + int(pesel[8]) +
            3 * int(pesel[9]) + int(pesel[10])) % 10 == 0:
        return True
    return False


def month_of_birth(pesel):
    months_dic = {1: "January", 2: "February", 3: "March",
                  4: "April", 5: "May", 6: "June", 7: "July",
                  8: "August", 9: "September", 10: "October",
                  11: "November", 12: "December"}
    x = int(pesel[2:4])
    if x in range(0, 13):
        return months_dic[x]
    elif x in range(21, 33):
        return months_dic[x - 20]
    elif x in range(41, 53):
        return months_dic[x - 40]
    else:
        return months_dic[x - 80]


def month_of_birth_2(pesel):
    x = int(pesel[2:4])
    if x in range(0, 13):
        return x
    elif x in range(21, 33):
        return x - 20
    elif x in range(41, 53):
        return x - 40
    else:
        return x - 80


def year_of_birth(pesel):
    x = int(pesel[2:4])
    y = pesel[0:2]
    if x in range(0, 13):
        return "19" + y
    elif x in range(21, 33):
        return "20" + y
    elif x in range(41, 53):
        return "21" + y
    else:
        return "18" + y


def which_day(year, month, day):
    day_dic = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday",
               4: "Friday", 5: "Saturday", 6: "Sunday"}
    x = datetime.datetime(year, month, day)
    y = x.weekday()
    return day_dic[y]


if __name__ == '__main__':
    print("Hello!\nWelcome to PESEL program. \nEnter your PESEL number and "
          "the program will tell you your date of birth, "
          "sex and correctness of your PESEL.")
    while True:
        try:
            print()
            my_pesel = int(input("Enter your PESEL number: "))
            if len(str(my_pesel)) != 11:
                print("Wrong value. PESEL should has 11 digits. Try again.")
                pass
            elif correctness_of_pesel(str(my_pesel)) is False:
                print("Your PESEL is incorrect. It's probably a clerk's "
                      "mistake :).")
                pass
            else:
                print()
                print("Your PESEL is correct.")
                print("You were born on {}, {}th {} in {}.".format(
                    which_day(int(year_of_birth(str(my_pesel))),
                              month_of_birth_2(str(my_pesel)),
                              int(str(my_pesel)[4:6])), str(my_pesel)[4:6],
                    month_of_birth(str(my_pesel)),
                    year_of_birth(str(my_pesel))))
                print("You are {}.".format(male_or_female(str(my_pesel))))
        except ValueError:
            print("Wrong value. PESEL should contains only digits. Try again.")
            pass
        shall_continue = input("\nDo you want to continue [y / n]: ")
        if shall_continue != "y":
            break
