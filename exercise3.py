s = input()
s1 = s
c = 0
if (s.find('E') == len(s) - 1 - s.find('3') or s.find('E')== len(s)//2 or s.find('3')== len(s)//2) or (s.find('J') == len(s) - 1 - s.find('L') or s.find('L')== len(s)//2 or s.find('J')== len(s)//2) or (s.find('S') == len(s) - 1 - s.find('2') or s.find('S')== len(s)//2 or s.find('2')== len(s)//2) or (s.find('Z') == len(s) - 1 - s.find('5') or s.find('Z')== len(s)//2 or s.find('5')== len(s)//2):
    s=s.replace('E','3')
    s=s.replace('J','L')
    s=s.replace('S','2')
    s=s.replace('Z','5')
    if s == s[::-1]:
        print(s1 + ' is a mirrored string.')
    else:
        print(s1 + ' is not a palindrome.')
elif s == s[::-1] and (s.find('A') or s.find('H') or s.find('I') or s.find('M') or s.find('O') or s.find('T') or s.find('U') or s.find('V') or s.find('W') or s.find('X') or s.find('Y') or s.find('1') or s.find('8') != -1):
    if s.find('A') != -1:
        c += 1
    if s.find('H') != -1:
        c += 1
    if s.find('I') != -1:
        c += 1
    if s.find('M') != -1:
        c += 1
    if s.find('O') != -1:
        c += 1
    if s.find('T') != -1:
        c += 1
    if s.find('U') != -1:
        c += 1
    if s.find('V') != -1:
        c += 1
    if s.find('W') != -1:
        c += 1
    if s.find('X') != -1:
        c += 1
    if s.find('Y') != -1:
        c += 1
    if s.find('1') != -1:
        c += 1
    if s.find('8') != -1:
        c += 1
    if len(s)%2 == 1 and c == (len(s)+1)/2:
        print(s1 + ' is a mirrored palindrome.')
    elif len(s)%2 == 0 and c == len(s)/2:
        print(s1 + ' is a mirrored palindrome.')
    else:
        print(s1 + ' is a regular palindrome.')
else:
    if s!=s[::-1]:
        print(s1 + ' is not a palindrome.')
