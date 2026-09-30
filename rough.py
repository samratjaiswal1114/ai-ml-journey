def swap_case(s):
    if s == s.upper():
        return s.lower()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)