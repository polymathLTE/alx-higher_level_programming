#!/usr/bin/python3
# Author - Lawal Emmanuel

# run only as script/ not when imported
if __name__ == '__main__':
    # import module(s)
    from calculator_1 import add, sub, mul, div

    # init variables
    err_msg_arg = "Usage: ./100-my_calculator.py <a> <operator> <b>"
    err_msg_opr = "Unknown operator. Available operators: +, -, * and /"
    sysa = sys.argv
    sysex = sys.exit

    # declare function
    def is_operator(op):
        """ check if argument is maths operator """
        ret = False
        opr_lst = ['+', '-', '*', '/']
        if op in opr_lst:
            ret = True
        return ret

    # define function
    def set_operator(op):
        """ sets the operator to be used """
        if op == '+':
            op = add
        elif op == '-':
            op = sub
        elif op == '*':
            op == mul
        else:
            op == div
        return op

    # checks for correct number of arguments
    if len(sysa)-1 != 3:
        print("{}".format(err_msg_arg))
        sysex(1)

    # checks for correct math operator
    opr = sysa[2]
    if not is_operator(opr):
        print("{}".format(err_msg_opr))
        sysex(1)

    # performs requested operation
    opr = set_operator(opr)
    a = int(sysa[1])
    b = int(sysa[3])
    opr_sign = sysa[2]
    print("{} {} {} = {}".format(a, opr_sign, b, opr(a, b)))
