char_sequence  = input().strip()
max_length  = 1
current_length  = 1
for i in range (1, len(char_sequence)):
    if char_sequence[i] == char_sequence[i-1]:
        current_length +=1
    else:
        current_length =1

    max_length = max(max_length, current_length)

print(max_length)
