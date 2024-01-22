#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    new_list = []
    for i in range(0, list_length):
        try:
            say = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            say = 0
        except ZeroDivisionError:
            print("division by 0")
            say = 0
        except IndexError:
            print("out of range")
            say = 0
        finally:
            new_list.append(say)
    return (new_list)
