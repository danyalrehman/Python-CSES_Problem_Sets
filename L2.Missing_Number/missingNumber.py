n = int(input()) # take input, n
missingArray = list(map(int, input().strip().split()))[:n-1] # take input and convert to an array form

print(-sum(missingArray) + int(n * (n + 1) / 2)) # O(N) approach by finding the sum of the array and subtracting it from the summation formula
