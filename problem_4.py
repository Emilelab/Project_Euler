#Find the largest palindrome made from the product of two 3-digit numbers.

a = 0 #biggest palindrome

def is_it_a_palindrome(n):
    s = str(n)
    l = len(s)
    global a
    if l == 6:
        if s[0] == s[5]:
            if s[1] == s[4]:
                if s[2] == s[3]:
                    if n > a:
                        a = n
                    else: return
                else: return
            else: return
        else: return
    elif l == 5:
        if s[0] == s[4]:
            if s[1] == s[3]:
                if n > a:
                    a = n
                else: return
            else: return
        else: return
    elif l == 4:
        if s[0] == s[3]:
            if s[1] == s[2]:
                    if n > a:
                        a = n
                    else: return
            else: return
        else: return
    elif l == 3:
        if s[0] == s[2]:
            if n > a:
                a = n
            else: return
        else: return
    elif l == 2:
        if s[0] == s[1]:
            if n > a:
                a = n
            else: return
        else: return
    elif l == 1:
        if n > a:
            a = n
        else: return

y = 999
for x in range (999, 0, -1):  
    result = x*y
    is_it_a_palindrome(result)
    for y in range (999, 0, -1):       
        result = x*y
        is_it_a_palindrome(result)
print("The biggest palindrome is", a)