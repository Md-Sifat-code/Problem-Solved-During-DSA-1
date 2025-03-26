st = "abcabcbb"
n = len(st)
maxlength = 0
charSet = set()
left = 0
for right in range(n):
    while st[right] in charSet:
        charSet.remove(st[left])
        left+=1
    charSet.add(st[right])
    maxlength = max(maxlength, right-left +1)

print(maxlength)