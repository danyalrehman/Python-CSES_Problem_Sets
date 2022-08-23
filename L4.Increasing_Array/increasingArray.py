n = int(input())
inputArray = list(map(int, input().strip().split()))

nMoves = 0
for idx, value in enumerate(inputArray[1:], start=1):
	if value < inputArray[idx - 1]:
		nMoves += abs(value - inputArray[idx - 1])
		inputArray[idx] = inputArray[idx - 1]
print(nMoves)
