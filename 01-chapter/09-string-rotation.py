
def is_substring(string: str, substr: str) -> bool:
    return substr in string


def string_rotation(string1: str, string2: str) -> bool:
    if len(string1) != len(string2) or len(string1) < 1:
        return False

    return is_substring(string1 + string1, string2)


if __name__ == '__main__':
    # Should be true
    print(string_rotation('waterbottle', 'erbottlewat'))
    print(string_rotation('waterbottle', 'ttlewaterbo'))
    print(string_rotation('melancia', 'ciamelan'))
    print(string_rotation('abacaxi', 'caxiaba'))
    print(string_rotation('arara', 'raara'))
    print(string_rotation('ba', 'ab'))
    # Should be false
    print(string_rotation('waterbottle', 'terwabottle'))
    print(string_rotation('embuguacu', 'pariescro'))
    print(string_rotation('melancia', 'abacaxi'))
    print(string_rotation('', ''))
    print(string_rotation('a', 'b'))
