# Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# 25164150

sq = 0
su = 0
for i in range(1, 101):
    sq = sq + i**2
    su = su + i
print(abs(sq - su**2))    