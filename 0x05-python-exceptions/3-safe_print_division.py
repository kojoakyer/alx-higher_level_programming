#!/usr/bin/python3

def safe_print_division(a, b):

    try:
        say = a / b
    except (TypeError, ZeroDivisionError):
        say = None
    finally:
        print("Inside result: {}".format(say))
    return (say)
