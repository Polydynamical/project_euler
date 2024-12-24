is_palindrome = lambda s: True if s[::-1] == s else False
m = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if is_palindrome(str(i * j)):
            m = max(m, i * j)
print(m)
