# utils.py

import os


def check_puzzle_ans(ans):
    ans_passed = ans.lower()
    ans_correct = os.getenv("OGRO")
    if ans_passed == ans_correct:
        return True
    else:
        return False


def check_puzzle_crossed_lines(name):
    name_passed = name.lower()
    name_correct = os.getenv("NAME")
    if name_passed == name_correct:
        return True
    else:
        return False


def check_puzzle_fourth_key(k4):
    key_passed = k4.lower()
    key_correct = os.getenv("CROS")
    if key_passed == key_correct:
        return True
    else:
        return False


def check_puzzle_three_keys(k1, k2, k3):
    keys_passed = [k1, k2, k3]
    keys_passed = [k.lower() for k in keys_passed]
    key_correct_1 = os.getenv("KEY1")
    key_correct_2 = os.getenv("KEY2")
    key_correct_3 = os.getenv("KEY3")
    keys_correct = [key_correct_1, key_correct_2, key_correct_3]
    keys_used = []
    for key in keys_passed:
        if key in keys_used:
            return False
        else:
            keys_used.append(key)
            if not key in keys_correct:
                return False
    return True


def check_what_puzzle(what):
    what_passed = what.lower()
    what_correct = os.getenv("WHAT")
    if what_passed == what_correct:
        return True
    else:
        return False

