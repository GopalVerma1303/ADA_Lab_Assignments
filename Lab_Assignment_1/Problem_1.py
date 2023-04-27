def count_ways(current_step, n):
    if current_step > n:
        return 0
    elif current_step == n:
        return 1
    else:
        return count_ways(current_step + 1, n) + count_ways(current_step + 2, n) + count_ways(current_step + 3, n)


# Taking input
n = int(input())

# Calling function and printing output
print(count_ways(0, n))
