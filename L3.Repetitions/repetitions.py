dnaSequence = list(input())

maxSubstring = 1
dnaType, subsequenceCount = dnaSequence[0], 1
for idx, dna in enumerate(dnaSequence[1:], start=1):
	if dna == dnaType:
		subsequenceCount += 1
	else:
		subsequenceCount = 1
		dnaType = dna
	maxSubstring = max(maxSubstring, subsequenceCount)

print(maxSubstring)
