
def create_p_array(s: str) -> list[int]:
    """Creating pi-array"""
    m = len(s)
    i = 1
    j = 0
    p = [0] * m
    while i < m:
        if s[i] == s[j]:
            p[i] = j + 1
            i += 1
            j += 1
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1
    return p


def is_found_str(text: str, s: str) -> bool:
    """Algorithm KMP (Knuth-Morris-Pratt) to find sub str into str"""
    n = len(text)
    m = len(s)
    p = create_p_array(s)
    i = 0
    j = 0
    while i < n and m:
        if text[i] == s[j]:
            i += 1
            j += 1
            if j == m:
                return True
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1
    return False


if __name__ == '__main__':
    print(is_found_str(text='Hello, is word in this string', s='word'))
