n = int(input())

for _ in range(n):
    word = input().strip()          # strip just in case
    length = len(word)
    
    if length > 10:
        abbr = word[0] + str(length - 2) + word[-1]
        print(abbr)
    else:
        print(word)