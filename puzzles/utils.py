# utils.py

def check_puzzle_ans(ans):
    ans_passed = ans
    ans_correct = 'winogrono'
    if ans_passed == ans_correct:
        return True
    else:
        return False


def check_puzzle_crossed_lines(name):
    name_passed = name
    name_correct = 'sfinks'
    if name_passed == name_correct:
        return True
    else:
        return False


def check_puzzle_fourth_key(k4):
    key_passed = k4
    key_correct = 'kościół'
    if key_passed == key_correct:
        return True
    else:
        return False


def check_puzzle_three_keys(k1, k2, k3):
    keys_passed = [k1, k2, k3]
    keys_correct = ['cmentarz', 'więzienie', 'szpital']
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
    what_passed = what
    what_correct = 'człowiek'
    if what_passed == what_correct:
        return True
    else:
        return False

