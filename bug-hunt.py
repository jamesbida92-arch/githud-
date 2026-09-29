Gcount = 1
total = 0

# BUG: Added a colon ':' at the end of the line to fix a SyntaxError.
# BUG: Changed condition from 'count < 5' to 'count <= 5' (or 'count < 6') to include 5 in the sum, fixing a logic error where the total was incorrectly 10 instead of 15.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Wrapped 'total' in str() to convert the int to a string for concatenation, fixing a TypeError when adding string and int types together.
print("Sum of 1 to 5 is: " + str(total))
