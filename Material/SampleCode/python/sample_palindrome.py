s = "malaalam"
l = len(s)

left = l//2
right = l//2
if l%2==0:
    right = right-1

for i in range(l//2):
    if s[left] == s[right]:
        left -= 1
        right += 1
        continue
    else:
        print("Not a palindrome")
        break
else:
    print("Palindrome")