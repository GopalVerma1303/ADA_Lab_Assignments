# Taking input
N = int(input())

# Initializing variables
total_bricks = 0
round_number = 1

# Loop to simulate the process of putting the bricks
while total_bricks < N:
    patlu_bricks = round_number
    motu_bricks = round_number * 2
    total_bricks += patlu_bricks + motu_bricks
    if total_bricks >= N:
        print("Motu")
        break
    round_number += 1
    if total_bricks >= N:
        print("Patlu")
        break
