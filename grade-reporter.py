# Starting list of scores (unmodified)
scores = [72, 45, 90, 61, 38]

# Initialize trackers for pass/fail counts and total sum
passes = 0
fails = 0
total_score = 0

# Loop through each score to evaluate grades and update counts
for score in scores:
    total_score += score
    
    # Grade assignment logic
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
        
    # Pass/Fail counter
    if score >= 50:
        passes += 1
    else:
        fails += 1
        
    print(f"Score: {score} - Grade: {grade}")

# Calculate average rounded to 1 decimal place
average = round(total_score / len(scores), 1)

# Summary display
print("-" * 20)
print(f"Passed: {passes}")
print(f"Failed: {fails}")
print(f"Average: {average}")
