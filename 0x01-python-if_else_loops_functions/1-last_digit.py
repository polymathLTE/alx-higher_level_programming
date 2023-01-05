#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
msg = ["Last digit of", "is"]
con_msg = ["and is greater than 5", "and is 0", "and is less than 6 and not 0"]
ls_dgt = int(abs(number) % 10)
if number < 0:
    ls_dgt = ls_digit * -1

# check for given conditions
if ls_dgt > 5:
    print("{} {} {} {} {}".format(msg[0], number, msg[1], ls_dgt, con_msg[0]))
if ls_dgt == 0:
    print("{} {} {} {} {}".format(msg[0], number, msg[1], ls_dgt, con_msg[1]))
if ls_dgt < 6 and ls_dgt != 0:
    print("{} {} {} {} {}".format(msg[0], number, msg[1], ls_dgt, con_msg[2]))
