# put your python code here
a = int(input().strip())
b = int(input().strip())
a, b = min(a, b), max(a, b)

values = [x for x in range(a, b + 1) if x % 3 == 0]

print(sum(values) / len(values))
