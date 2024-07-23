#  https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true

n = int(input())
s = set(map(int, input().split()))
commands_count=int(input())
for _ in range(commands_count):
    command=input().split()
    if command[0]=='pop':
        s.pop()
    elif command[0]=='remove':
        value=int(command[1])
        s.remove(value)
    elif command[0]=='discard':
        value=int(command[1])
        s.discard(value)
print(sum(s))
