# def printOddNumbers(start, end):
#     # Ensure that start is odd, adjust if necessary
#     if start % 2 == 0:
#         start += 1

#     # Iterate through the range from start to end (inclusive) with a step of 2
#     for num in range(start, end + 1, 2):
#         print(num)

# # Example usage:
# start_number = 2
# end_number = 5
# print("Odd numbers between {} and {}:".format(start_number, end_number))
# printOddNumbers(start_number, end_number)


def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0

    # Compare each element in the triplets
    for alice_rating, bob_rating in zip(a, b):
        if alice_rating > bob_rating:
            alice_score += 1
        elif alice_rating < bob_rating:
            bob_score += 1

    return [alice_score, bob_score]

# Example usage:
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = compareTriplets(a, b)
print(result)
