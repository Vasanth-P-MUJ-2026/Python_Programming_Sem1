palindromes = []
# find all 3-digit palindromes
for num in range(100, 1000):
    if str(num) == str(num)[::-1]:
        palindromes.append(num)

#calculate sum and average
sum_palindromes = sum(palindromes)
avg_palindromes = sum_palindromes / len(palindromes)

#store result in tuple
result = (sum_palindromes, avg_palindromes)

#display the tuple
print(result)
