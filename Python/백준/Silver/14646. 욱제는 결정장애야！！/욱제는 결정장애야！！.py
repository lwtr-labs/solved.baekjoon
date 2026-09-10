import sys

input = sys.stdin.readline

n = int(input())

result = list(map(int, input().strip().split()))

check = set()
onBoard = 0
max = 0

for i in result:
    if i not in check:
        check.add(i)
        onBoard += 1
        if max < onBoard:
            max = onBoard
    else:
        onBoard -= 1


print(max)