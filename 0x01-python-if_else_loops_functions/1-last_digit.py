#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
msg = ["Last digit of", "is"]
con_msg = ["and is greater than 5", "and is 0", "and is less than 6 and not 0"]
ls_digit = int(abs(number) % 10)
if number < 0:
    ls_digit = ls_digit * -1;

#check for given conditions
if ls_digit > 5:
    print ("{} {} {} {} {}".format(msg[0], number, msg[1], ls_digit, con_msg[0]))
if ls_digit == 0:
    print ("{} {} {} {} {}".format(msg[0], number, msg[1], ls_digit, con_msg[1]))
if ls_digit < 6 and ls_digit != 0:
    print ("{} {} {} {} {}".format(msg[0], number, msg[1], ls_digit, con_msg[2]))
