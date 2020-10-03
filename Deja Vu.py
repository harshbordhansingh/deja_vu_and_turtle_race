def function(s):
    p = -1
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                p = i
                break
        if p != -1:
            break
    return p


if __name__ == '__main__':
    char = input()
    pos = function(char)
    if pos == -1:
        print("Unique")
    else:
        print("Deja vu")