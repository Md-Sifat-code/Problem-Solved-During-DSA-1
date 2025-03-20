n = int(input())
arr = list(map(int,input().split()))
l,r =0, n-1
sortedarr = sorted(arr)
while l < n and arr[l] == sortedarr[l]:
    l+=1

while r > l and arr[r] == sortedarr[r]:
    r-=1
if l == n:
    print("yes")
    print(1,1)
    exit()
arr[l:r+1] = arr[l:r+1][::-1]

if arr == sortedarr:
    print("yes")
    print(l+1, r+1)
else:
    print("no")
