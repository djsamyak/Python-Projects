input_array = [1,4,1,2,7,5,2]
# 1 1 2 2 5 7

counts = [0]*10
for _ in input_array:
    counts[_] += 1

for _ in range(1,len(counts)):
    counts[_] += counts[_-1]

sortedw = [0] * (max(input_array)+1)

for _ in input_array:
    sortedw[counts[_]] = _
    counts[_] -= 1

sortedw.pop(0)

print(sortedw)
    