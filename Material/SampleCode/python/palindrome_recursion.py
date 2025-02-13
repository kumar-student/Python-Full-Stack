def palindrome(s):
    if len(s) <= 1:
        return True
    return s[0]==s[-1] and palindrome(s[1:-1])

s = "malayalam"
is_palindrome = palindrome(s)
print(is_palindrome)