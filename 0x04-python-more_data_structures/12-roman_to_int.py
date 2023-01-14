#!/usr/bin/python3
# Author - Lawal Emmanuel

def roman_to_int(roman_string):
    """function that converts roman numeral to integer"""
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num_count = 0
    last_rom = ''
    for i in roman_string:
        if num_count != 0 and rom_num.get(i) > rom_num.get(last_rom):
            num_count += (rom_num.get(i) - rom_num.get(last_rom)*2)
            last_rom = i
        else:
            num_count += rom_num.get(i)
            last_rom = i
    return num_count
